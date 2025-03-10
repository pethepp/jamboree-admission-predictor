import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

# Load the dataset and preprocess it
df = pd.read_csv('Jamboree_Admission.csv').drop(columns=['Serial No.'])

# Clean and preprocess the data
df.rename(columns={'Chance of Admit ': 'Chance_of_Admit', 'LOR ': 'LOR'}, inplace=True)
X = df.drop('Chance_of_Admit', axis=1)
y = df['Chance_of_Admit']

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

# Train the Ridge Regression model
ridge = Ridge(alpha=5.0)
ridge.fit(X_scaled_df, y)

# Save the model and scaler as pickle files
pickle.dump(ridge, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

# Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """
    Render the front-end HTML page
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle the prediction API request
    """
    try:
        # Receive input data from frontend
        data = request.get_json()
        gre = float(data['GRE Score'])
        toefl = float(data['TOEFL Score'])
        rating = float(data['University Rating'])
        sop = float(data['SOP'])
        lor = float(data['LOR'])
        cgpa = float(data['CGPA'])
        research = int(data['Research'])

        # Load the model and scaler
        model = pickle.load(open('model.pkl', 'rb'))
        scaler = pickle.load(open('scaler.pkl', 'rb'))

        # Prepare input for prediction
        input_data = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)
        response = {
            'Chance of Admit': round(prediction[0], 4),
            'Model': 'Ridge Regression',
            'Confidence': 'High'
        }

        return jsonify(response)

    except Exception as e:
        # Handle any unexpected error
        return jsonify({'error': str(e)})

@app.route('/health', methods=['GET'])
def health():
    """
    Health check API
    """
    return jsonify({'status': 'running'})


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000, debug=False)


FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your local project directory to /app
COPY . .

# Install all dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly copy the model files to persist them
COPY model.pkl model.pkl
COPY scaler.pkl scaler.pkl

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "app.py"]


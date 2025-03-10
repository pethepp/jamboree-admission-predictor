# 🎓 Jamboree Admission Predictor

This is a **Machine Learning Web Application** built using **Flask, Python, and Scikit-Learn** to predict the **chances of admission** of students applying for higher studies. The model is trained using the famous **Jamboree Education dataset**, which contains various features like GRE Score, TOEFL Score, University Rating, CGPA, and Research Experience to predict the probability of admission.



## 📊 Project Overview
This project aims to predict the chances of admission for students applying to graduate schools. Based on their:
- GRE Score
- TOEFL Score
- University Rating
- Statement of Purpose (SOP)
- Letter of Recommendation (LOR)
- CGPA
- Research Experience

The model will provide a **probability score** for admission.

---

## 🚀 Tech Stack
The project uses the following technologies:

| Component      | Technology Used          |
|----------------|-------------------------|
| Backend        | Flask (Python)           |
| Machine Learning | Scikit-Learn, Pandas     |
| Frontend       | HTML, CSS, JavaScript    |
| Model Deployment | Render.com              |
| Version Control | Git, GitHub             |

---

## 🧠 How the Model Works
The model is built using the **Linear Regression Algorithm**, which works as follows:
- It takes inputs like GRE, TOEFL, CGPA, and Research Experience.
- Based on the historical data, it predicts the **probability of admission**.
- The higher the probability, the more likely the candidate will get admitted.

---

## 📜 Dataset Used
The dataset used in this project is publicly available and widely known as the **Jamboree Admission Dataset**. It contains the following columns:

| Feature                | Description                                                  |
|-----------------------|-------------------------------------------------------------|
| GRE Score              | GRE scores of applicants                                     |
| TOEFL Score            | TOEFL scores of applicants                                   |
| University Rating      | University rating (1 to 5)                                   |
| SOP                    | Statement of Purpose strength (1 to 5)                       |
| LOR                    | Letter of Recommendation strength (1 to 5)                   |
| CGPA                   | Undergraduate CGPA                                           |
| Research               | Whether the applicant has research experience (0 or 1)      |

---

## ✅ How to Run This Project Locally
If you'd like to run this project locally on your machine, follow these steps:

### 📥 Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/jamboree-admission-predictor.git
cd jamboree-admission-predictor
```

### 📜 Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
```

### 📦 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 💻 Step 4: Run the Flask Application
```bash
python app.py
```

Your app will run on: [http://localhost:5000](http://localhost:5000)

---

## 💻 Deployment
The app has been deployed live using **Render.com**. You can access it here:
👉 **Live Link:** [https://jamboree-predictor.onrender.com](https://jamboree-predictor.onrender.com)

Every time a new code push is made to GitHub, Render automatically deploys the latest version of the app.

---

## 📷 Screenshots
### Home Page
![Home Page](https://via.placeholder.com/600x300?text=Home+Page)

### Prediction Output
![Prediction](https://via.placeholder.com/600x300?text=Prediction+Output)

_(You can update these screenshots later once you host the app)_

---

## 📂 Project Structure
```
Jamboree_Education
│
├── app.py         <-- Flask App
├── model.pkl      <-- Trained Machine Learning Model
├── requirements.txt <-- Dependencies for deployment
├── templates
│   ├── index.html <-- Frontend UI
├── static
│   ├── images
│       ├── logo.png <-- Jamboree Logo
```

---

## 👨‍💻 Contributing
If you'd like to improve the project, feel free to:
1. Fork the repository.
2. Make changes.
3. Create a pull request.

We would love to see your contributions!

---

## ⭐ Acknowledgements
This project is inspired by **Jamboree Education** and aims to help students predict their chances of admission.

If you found this project helpful, don't forget to ⭐ star the repository!

---

## 📧 Contact
If you have any questions or need support, reach out to me at:
- 📧 **Email:** your-email@gmail.com
- 💻 **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)
- 🐍 **GitHub:** [Your GitHub](https://github.com/YourUsername)

---

✅ **Happy Learning & Building! 🚀😊**


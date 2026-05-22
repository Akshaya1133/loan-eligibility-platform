# AI Loan Eligibility Prediction Platform

An AI-powered Flask web application that predicts loan eligibility using Machine Learning based on user financial and personal details.

## Features

✅ User Registration & Login Authentication  
✅ Secure Password Hashing  
✅ AI-based Loan Eligibility Prediction  
✅ Confidence Score Display  
✅ Modern Responsive UI  
✅ Dashboard for Users  
✅ Flask + SQLAlchemy Backend  
✅ Machine Learning Model using Random Forest  
✅ Deployed on Render  

---

## Tech Stack

### Frontend
- HTML5
- CSS3
- Responsive UI Design

### Backend
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Werkzeug

### Machine Learning
- Pandas
- Scikit-learn
- Joblib
- Random Forest Classifier

### Database
- SQLite

### Deployment
- GitHub
- Render

---

## Project Workflow

1. User registers an account
2. User logs into dashboard
3. User enters loan details
4. Machine Learning model processes input
5. Prediction result shown:
   - Loan Approved ✅
   - Loan Rejected ❌
6. Confidence score displayed

---

## Input Parameters Used

- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Gender
- Marital Status
- Dependents
- Education
- Self Employment Status
- Property Area

---

## Machine Learning Model

Model Used:
**Random Forest Classifier**

Model Accuracy:
**78%**

Dataset:
Bank loan approval historical dataset

---

## Project Structure

```bash
loan-eligibility-platform/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── loan.csv
│
├── model/
│   ├── loan_model.pkl
│   └── columns.pkl
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── predict.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
└── utils/
    └── predictor.py
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/Akshaya1133/loan-eligibility-platform.git
cd loan-eligibility-platform
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Deployment

Deployed using Render cloud platform.

---

## Future Improvements

- Email OTP verification
- Admin dashboard
- Loan history tracking
- PDF loan report download
- Database migration to PostgreSQL
- Explainable AI recommendations
- EMI calculator integration

---

## Author

**Akshaya B S**  
MCA Student | AI & Full Stack Enthusiast

GitHub:
https://github.com/Akshaya1133

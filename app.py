import pandas as pd
import joblib

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'loan_secret_key_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Load ML model
model = joblib.load("model/loan_model.pkl")
columns = joblib.load("model/columns.pkl")

# Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# USER MODEL
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE DB TABLES FOR RENDER
with app.app_context():
    db.create_all()


# HOME
@app.route('/')
def home():
    return render_template('index.html')


# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists")
            return redirect(url_for('register'))

        new_user = User(
            full_name=full_name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))

        flash("Invalid credentials")

    return render_template('login.html')


# DASHBOARD
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


# PREDICT
@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        input_data = {
            'ApplicantIncome': float(request.form['ApplicantIncome']),
            'CoapplicantIncome': float(request.form['CoapplicantIncome']),
            'LoanAmount': float(request.form['LoanAmount']),
            'Loan_Amount_Term': float(request.form['Loan_Amount_Term']),
            'Credit_History': float(request.form['Credit_History']),
            'Gender_Male': 1 if request.form['Gender'] == 'Male' else 0,
            'Married_Yes': 1 if request.form['Married'] == 'Yes' else 0,
            'Dependents_1': 1 if request.form['Dependents'] == '1' else 0,
            'Dependents_2': 1 if request.form['Dependents'] == '2' else 0,
            'Dependents_3': 1 if request.form['Dependents'] == '3' else 0,
            'Education_Not Graduate': 1 if request.form['Education'] == 'Not Graduate' else 0,
            'Self_Employed_Yes': 1 if request.form['Self_Employed'] == 'Yes' else 0,
            'Property_Area_Semiurban': 1 if request.form['Property_Area'] == 'Semiurban' else 0,
            'Property_Area_Urban': 1 if request.form['Property_Area'] == 'Urban' else 0
        }

        input_df = pd.DataFrame([input_data])

        for col in columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[columns]

        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)

        confidence = round(max(probability[0]) * 100, 2)

        result = "Loan Approved ✅" if prediction[0] == 1 else "Loan Rejected ❌"

        return render_template(
            'result.html',
            result=result,
            confidence=confidence
        )

    return render_template('predict.html')


# LOGOUT
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
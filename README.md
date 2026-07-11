# AI Career Guidance System

## Overview

The **AI Career Guidance System** is a web-based application developed using **Python, Flask, Machine Learning, SQLite, HTML, and CSS**. The system helps students identify suitable career paths based on their interests, skills, favorite subjects, and aptitude.

It also provides user authentication, a study planner, motivational quotes, and progress tracking to support students in achieving their career goals.

---

## Features

* User Registration and Login
* AI-Based Career Prediction
* Study Planner
* Progress Tracker
* Daily Motivation Quotes
* Secure Session Management
* SQLite Database Integration
* Responsive User Interface

---

## Technologies Used

* Python 3.12
* Flask
* Scikit-learn
* Pandas
* NumPy
* SQLite
* HTML5
* CSS3
* Joblib

---

## Project Structure

```text
AI-Career-Guidance-System/
│
├── app.py
├── run.py
├── train_model.py
├── predict.py
├── requirements.txt
├── career_dataset.csv
├── career_model.pkl
├── encoders.pkl
├── career_encoder.pkl
├── database.db
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── career.html
│   ├── planner.html
│   ├── motivation.html
│   └── progress.html
│
└── static/
    ├── style.css
    └── images/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aswini-codes/AI-Career-Guidance-System-project.git
```

Move into the project directory:

```bash
cd AI-Career-Guidance-System-project
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Train the machine learning model:

```bash
python train_model.py
```

Run the application:

```bash
python app.py
```

Or run with Waitress:

bash
python run.py

Open your browser and visit:
http://127.0.0.1:5000

## Machine Learning

The application uses a **Decision Tree Classifier** to recommend career options based on:

* Interest
* Skill
* Subject
* Aptitude

The trained model is stored using **Joblib**.

## Database

SQLite is used to store:

* User registration details
* Login information
* Study planner tasks
* Progress information

## Future Enhancements

* Admin Dashboard
* Email Notifications
* Resume Builder
* Online Career Courses
* Personality Assessment
* Career Roadmap Generator

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import joblib
import pandas as pd
from voice import speak
app = Flask(__name__)
app.secret_key = "career_guidance_secret"

# Load ML model
model = joblib.load("career_model.pkl")
encoders = joblib.load("encoders.pkl")
career_encoder = joblib.load("career_encoder.pkl")


# Database Connection
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create tables if not exists
def create_tables():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS planner(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        task TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


create_tables()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (name, email, password)
            )
            conn.commit()

        except:
            conn.close()
            return "Email already exists."

        conn.close()
        return redirect('/login')

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cur.fetchone()
        conn.close()

        if user:
            session['email'] = email
            session['name'] = user['name']
            return redirect('/dashboard')

        return "Invalid Login"

    return render_template("login.html")


@app.route('/dashboard')
def dashboard():

    if 'email' not in session:
        return redirect('/login')

    return render_template(
        "dashboard.html",
        name=session['name']
    )
@app.route('/career', methods=['GET', 'POST'])
def career():

    prediction = None

    if request.method == 'POST':

        interest = request.form['interest']
        skill = request.form['skill']
        subject = request.form['subject']
        aptitude = request.form['aptitude']

        try:
            # Create DataFrame with feature names
            values = pd.DataFrame([{
                "Interest": encoders['Interest'].transform([interest])[0],
                "Skill": encoders['Skill'].transform([skill])[0],
                "Subject": encoders['Subject'].transform([subject])[0],
                "Aptitude": encoders['Aptitude'].transform([aptitude])[0]
            }])

            # Predict career
            pred = model.predict(values)[0]

            # Decode prediction
            prediction = career_encoder.inverse_transform([pred])[0]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template(
        "career.html",
        prediction=prediction
    )


@app.route('/planner', methods=['GET', 'POST'])
def planner():

    if 'email' not in session:
        return redirect('/login')

    conn = get_db()
    cur = conn.cursor()

    if request.method == 'POST':

        task = request.form['task']

        cur.execute(
            "INSERT INTO planner(email,task,status) VALUES(?,?,?)",
            (session['email'], task, "Pending")
        )

        conn.commit()

    cur.execute(
        "SELECT * FROM planner WHERE email=?",
        (session['email'],)
    )

    tasks = cur.fetchall()

    conn.close()

    return render_template(
        "planner.html",
        tasks=tasks
    )

@app.route('/progress')
def progress():

    if 'email' not in session:
        return redirect('/login')

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM planner WHERE email=?",
        (session['email'],)
    )

    total = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM planner WHERE email=? AND status='Completed'",
        (session['email'],)
    )

    completed = cur.fetchone()[0]

    conn.close()
    return render_template(
        "progress.html",
        total=total,
        completed=completed
    )
@app.route('/motivation', methods=['GET', 'POST'])
def motivation():

    quotes = [
        "Success comes from consistency.",
        "Believe in yourself.",
        "Study today, lead tomorrow.",
        "Every expert was once a beginner.",
        "Never stop learning."
    ]

    if request.method == "POST":
        quote = request.form["quote"]
        speak(quote)

    return render_template(
        "motivation.html",
        quotes=quotes
    )
    return render_template(
        "motivation.html",
        quotes=quotes
    )


if __name__ == "__main__":
    app.run(debug=True)
                



import joblib

# Load saved files
model = joblib.load("career_model.pkl")
encoders = joblib.load("encoders.pkl")
career_encoder = joblib.load("career_encoder.pkl")


def predict_career(interest, skill, subject, aptitude):
    try:
        # Convert user input into numeric values
        interest = encoders["Interest"].transform([interest])[0]
        skill = encoders["Skill"].transform([skill])[0]
        subject = encoders["Subject"].transform([subject])[0]
        aptitude = encoders["Aptitude"].transform([aptitude])[0]

        # Predict
        prediction = model.predict([[interest, skill, subject, aptitude]])[0]

        # Convert prediction back to career name
        career = career_encoder.inverse_transform([prediction])[0]

        return career

    except Exception as e:
        return f"Error: {e}"


# Test the model
if __name__ == "__main__":
    interest = input("Enter Interest: ")
    skill = input("Enter Skill: ")
    subject = input("Enter Subject: ")
    aptitude = input("Enter Aptitude (High/Medium/Low): ")

    result = predict_career(interest, skill, subject, aptitude)

    print("\nRecommended Career:")
    print(result)
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("career_dataset.csv")

# Features and Target
X = data[["Interest", "Skill", "Subject", "Aptitude"]]
y = data["Career"]

# Label Encoders
encoders = {}

for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    encoders[column] = le

career_encoder = LabelEncoder()
y = career_encoder.fit_transform(y)

# Train Model
model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42
)

model.fit(X, y)

# Save Model
joblib.dump(model, "career_model.pkl")
joblib.dump(encoders, "encoders.pkl")
joblib.dump(career_encoder, "career_encoder.pkl")

print("===================================")
print("Model Trained Successfully")
print("Files Created:")
print("1. career_model.pkl")
print("2. encoders.pkl")
print("3. career_encoder.pkl")
print("===================================")
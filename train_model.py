import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("career_dataset.csv")

# Features and Target
X = data[["Interest", "Skill", "Subject", "Aptitude"]].copy()
y = data["Career"]

# Label Encoders
encoders = {}

for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    encoders[column] = le

career_encoder = LabelEncoder()
y = career_encoder.fit_transform(y)

# Train Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save Model
joblib.dump(model, "career_model.pkl")
joblib.dump(encoders, "encoders.pkl")
joblib.dump(career_encoder, "career_encoder.pkl")

print("===================================")
print("Random Forest Model Trained Successfully")
print("Files Created:")
print("1. career_model.pkl")
print("2. encoders.pkl")
print("3. career_encoder.pkl")
print("===================================")
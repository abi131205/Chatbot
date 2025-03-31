import os

import joblib
import numpy as np

# Load model
model_path = "disease_prediction_model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found.")

model = joblib.load(model_path)

# Define test input
symptoms = [1, 0, 1, 0, 1]

# Debugging: Print type of symptoms
print(f"Received symptoms type: {type(symptoms)} - Value: {symptoms}")

# Convert to NumPy array
symptoms_array = np.array(symptoms).reshape(1, -1)

# Debugging: Check model input type
print(f"Model input type: {type(symptoms_array)}")

# Make a prediction
try:
    disease = model.predict(symptoms_array)[0]
    print(f"Predicted disease: {disease}")
except Exception as e:
    print(f"Error during prediction: {str(e)}")

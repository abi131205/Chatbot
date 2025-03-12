import os
from flask import Flask, request, jsonify
import joblib

# Load model
model = joblib.load("disease_prediction_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = data.get('symptoms')
    disease = model.predict([symptoms])[0]
    return jsonify({'disease': disease})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import joblib

# Load model
model = joblib.load("disease_prediction_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my chatbot API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = data.get('symptoms')
    disease = model.predict([symptoms])[0]
    return jsonify({'disease': disease})

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))  # Render assigns a port automatically
    app.run(host='0.0.0.0', port=port)

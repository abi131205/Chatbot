import os
from flask import Flask, request, jsonify
import joblib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load model
model = joblib.load("disease_prediction_model.pkl")

app = Flask(__name__)

# ✅ Only ONE @app.route('/') to avoid conflicts
@app.route('/')
def home():
    return "Welcome to my chatbot API!"

# ✅ Prediction Route (Ensuring JSON input)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'symptoms' not in data:
        return jsonify({'error': 'Missing symptoms field'}), 400

    symptoms = data['symptoms']
    
    try:
        disease = model.predict([symptoms])[0]
        return jsonify({'disease': disease})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ Only ONE `if __name__ == '__main__'` block
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

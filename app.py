import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy chatbot responses
def chatbot_response(message):
    responses = {
        "hi": "Hello! How can I assist you with your medical concerns?",
        "hello": "Hi there! What symptoms are you experiencing?",
        "fever": "A fever may indicate an infection. Do you have any other symptoms?",
        "cold": "You might have a common cold. Stay hydrated and rest.",
    }
    return responses.get(message.lower(), "I'm not sure. Please provide more details.")

# Dummy disease prediction based on symptoms
def predict_disease(symptoms):
    symptom_set = set(symptoms)
    if "fever" in symptom_set and "cough" in symptom_set:
        return {"disease": "Flu or common cold"}
    elif "headache" in symptom_set and "nausea" in symptom_set:
        return {"disease": "Migraine"}
    elif "chest pain" in symptom_set and "shortness of breath" in symptom_set:
        return {"disease": "Possible heart issue - Seek medical attention!"}
    else:
        return {"disease": "No specific match found. Please consult a doctor."}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    return jsonify({"reply": chatbot_response(user_message)})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    symptoms = data.get("symptoms", [])
    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400
    return jsonify(predict_disease(symptoms))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

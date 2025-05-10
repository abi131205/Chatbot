# 🩺 AI Medical Diagnosis Chatbot

An AI-powered medical diagnosis chatbot built using Rasa, machine learning, and a custom frontend. The chatbot allows users to enter symptoms and receive predictions for possible diseases along with advice and precautions.

---

## 📌 Project Overview

This chatbot helps users understand potential medical conditions based on their symptoms. It uses a trained ML model to predict diseases and leverages Rasa's natural language processing capabilities to handle user conversations. The backend stores interactions, and a simple frontend allows user-friendly input.

---

## 🎯 Features

- 🤖 Conversational AI built with Rasa
- 🧠 Disease prediction based on symptoms using a trained ML model
- 💊 Provides description, precautions, and medicines
- 📚 Trained on a labeled medical dataset
- 🗃️ SQLite database integration for logging interactions
- 💻 Basic frontend interface (GUI/Web)
- 📦 Docker support for easy deployment

---

## 🛠️ Tech Stack

| Layer         | Tools / Frameworks                        |
|--------------|--------------------------------------------|
| Frontend     | Python GUI (Tkinter or Web Interface)     |
| Backend      | Python, SQLite                            |
| Chatbot      | Rasa (NLU + Core), Custom Actions         |
| ML Model     | Scikit-learn, TensorFlow (model.h5 / .pkl)|
| Deployment   | Docker                                    |

---

## 📂 Project Structure

Chatbot/
├── actions/ # Custom actions (Python logic)
├── data/ # NLU training data, stories, rules
├── models/ # Trained Rasa model
├── my-backend/ # Backend logic and DB
├── my-frontend/ # GUI/Web interface
├── domain.yml # Intents, responses, entities
├── config.yml # Rasa config
├── Dockerfile # Deployment
├── medical_chatbot_dataset.csv # Dataset used for model training
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 How to Run the Project

### 🧪 Prerequisites

- Python 3.8+
- Rasa: `pip install rasa`
- Docker (optional)
- Other dependencies (use `requirements.txt` if included)

### ⚙️ Steps

1. **Clone the repo:**
   ```bash
   git clone https://github.com/abi131205/Chatbot
   cd Chatbot
Train the Rasa model:

bash
Copy
Edit
rasa train
Run the actions server:

bash
Copy
Edit
rasa run actions
Start the chatbot:

bash
Copy
Edit
rasa shell
(Optional) Run the GUI or frontend in my-frontend/:

bash
Copy
Edit
python chatbot_gui.py
(Optional) Build Docker container:

bash
Copy
Edit
docker build -t medical-chatbot .
docker run -p 5005:5005 medical-chatbot
🧠 Sample Interaction
vbnet
Copy
Edit
User: Hi
Bot: Hello! Please describe your symptoms.
User: I have a headache and fever
Bot: Based on your symptoms, you may have: Migraine
Bot: Suggested medicines: Paracetamol
Bot: Precautions: Stay hydrated and rest well.
📈 Future Enhancements
Voice assistant integration

Multilingual support

REST API for mobile app use

Improved web UI with React/Flask

Feedback and user rating system

📚 Dataset Source
The chatbot is trained on a custom CSV medical dataset mapping symptoms to diseases.

If the dataset is externally sourced, please credit here.

👨‍💻 Author
Abishek S – GitHub Profile

📜 License
This project is for educational purposes. If you plan to deploy publicly, ensure proper data privacy and medical disclaimer compliance.

yaml
Copy
Edit

---

Would you like me to create and commit this `README.md` to your GitHub repo via a PR or just send it as a downloadable file?

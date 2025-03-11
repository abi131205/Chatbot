import joblib
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Load trained model
model = joblib.load("disease_prediction_model.pkl")

# Create chatbot
chatbot = ChatBot("MedicalBot")

# Training chatbot with basic responses
trainer = ListTrainer(chatbot)
trainer.train([
    "Hello",
    "Hi there! How can I assist you?",
    "What should I do if I have a fever?",
    "You should take rest, drink fluids, and consult a doctor.",
    "I have a headache and fever",
    "Let me analyze your symptoms."
])

# Chat function
while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Bot: Take care! Goodbye!")
        break

    predicted_disease = model.predict([user_input])[0]
    response = chatbot.get_response(user_input)
    
    print(f"Bot: {response}")
    print(f"Bot: Based on your symptoms, you might have {predicted_disease}. Please consult a doctor.")

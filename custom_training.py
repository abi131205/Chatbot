from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("TestBot", database_uri="sqlite:///database.sqlite3")

trainer = ListTrainer(chatbot)

# Custom training data
conversation = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm good, thanks! How can I help you?",
    "What is your name?",
    "I'm TestBot, your chatbot assistant.",
    "Goodbye",
    "See you later!"
]

trainer.train(conversation)

print("Training complete!")

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ✅ Create the chatbot instance FIRST
chatbot = ChatBot("TestBot")

# ✅ Then create the trainer using the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# ✅ Train the chatbot using the built-in English dataset
trainer.train("chatterbot.corpus.english")

# ✅ Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":  # Exit condition
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)

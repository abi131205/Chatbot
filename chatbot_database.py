from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "TestBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm sorry, but I don't understand.",
            'maximum_similarity_threshold': 0.75
        }
    ]
)


trainer = ListTrainer(chatbot)

# Custom conversation dataset
conversation = [
    "Hello",
    "Hi there! How can I help you?",
    "What is your name?",
    "I am TestBot, your chatbot assistant.",
    "How are you?",
    "I'm a bot, but I'm doing great! What about you?",
    "Tell me a joke",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Goodbye",
    "See you later! Have a great day."
]

trainer.train(conversation)

while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Bot:", response)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break

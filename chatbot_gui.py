from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tkinter as tk
from tkinter import scrolledtext

# Initialize Chatbot with SQLite database
chatbot = ChatBot(
    "TestBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)

# GUI Functionality
def send_message():
    user_input = user_entry.get()
    chat_area.insert(tk.END, f"You: {user_input}\n")
    response = chatbot.get_response(user_input)
    chat_area.insert(tk.END, f"Bot: {response}\n\n")
    user_entry.delete(0, tk.END)

# Create GUI Window
root = tk.Tk()
root.title("Chatbot GUI")
root.geometry("500x500")

# Chat Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_area.pack(padx=10, pady=10)

# Input Box
user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the GUI
root.mainloop()

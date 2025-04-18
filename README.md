# 🤖 Chatbot Application

A complete chatbot system built with:

- 🧠 **Rasa** for NLP and intent classification  
- 💬 **React** for the frontend user interface  
- 🗃️ **SQLite** for storing conversations  
- ⚙️ **Flask** (`app.py`) for backend API bridging  

---

## 📁 Project Structure

Chatbot/ ├── .rasa/ # Rasa configuration ├── .venv/ # Python virtual environment (local) ├── .vscode/ # VS Code editor settings ├── actions/ # Custom Rasa actions ├── archive/ # Deprecated utilities/scripts ├── data/ # NLU, stories, rules ├── models/ # Trained Rasa models ├── my-backend/ # Rasa backend ├── my-frontend/ # React frontend ├── tests/ # Unit tests ├── app.py # Flask middleware API ├── db.sqlite3 # SQLite database ├── .env.example.txt # Sample environment variables └── README.md # This file

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1️⃣ Backend (Rasa)

```bash
cd my-backend/
pip install -r requirements.txt

# Train the chatbot
rasa train

# Start custom actions (in a new terminal)
rasa run actions

# Start Rasa server with API enabled
rasa run --enable-api
2️⃣ Frontend (React)
bash
Copy
Edit
cd ../my-frontend/
npm install
npm start
Now open 👉 http://localhost:3000 in your browser.

3️⃣ Bridge API Server (Flask)
This Flask server connects the React frontend with Rasa backend:

bash
Copy
Edit
# From the root directory
python app.py
You should see this JSON response in Postman or browser:

json
Copy
Edit
{
  "message": "API is running!"
}
🔐 Environment Setup
Create a .env file (if needed) from the example file:

bash
Copy
Edit
cp .env.example.txt .env
Inside .env:
ini
Copy
Edit
API_KEY=your_api_key_here
DATABASE_URL=sqlite:///db.sqlite3
The python-dotenv package loads these automatically in app.py.

📦 Archived Scripts (Reference Only)
Found in /archive folder:

auto_fix_rasa.py

check_columns.py

clean_requirements.py

fix_rasa_conflicts.py

database.sqlite3 (deprecated)

These are not actively used, but saved for debugging/version control.

🧪 Testing
Test Rasa:
bash
Copy
Edit
rasa shell
Test React frontend:
bash
Copy
Edit
npm test
🛠️ Tech Stack
Backend:

Rasa

Flask

SQLAlchemy

python-dotenv

Frontend:

React

Axios

TailwindCSS (optional)

react-icons

🤝 Contributing
Pull requests are welcome!
For major changes, open an issue first to discuss what you’d like to change.

📄 License
MIT License
Free to use for personal and commercial projects.

✨ Author
Built with ❤️ by @abi131205

yaml
Copy
Edit

---

Would you like me to:
- Push this cleaned-up version to your GitHub via PR?
- Move to the **next missing file**: `SECURITY.md`?
- Or help with something else like tests or model explanation?

Just say the word.
# 🤖 Chatbot Application

A complete chatbot system built with:

- 🧠 **Rasa** for NLP and intent classification  
- 💬 **React** for the frontend user interface  
- 🗃️ **SQLite** for storing conversations  
- ⚙️ **Flask** (`app.py`) for backend API bridging  

---

## 📁 Project Structure

```plaintext
Chatbot/
├── .rasa/               # Rasa configuration
├── .venv/               # Python virtual environment (local)
├── .vscode/             # VS Code editor settings
├── actions/             # Custom Rasa actions
├── archive/             # Deprecated utilities/scripts
├── data/                # NLU, stories, rules
├── models/              # Trained Rasa models
├── my-backend/          # Rasa backend
├── my-frontend/         # React frontend
├── tests/               # Unit tests
├── app.py               # Flask middleware API
├── db.sqlite3           # SQLite database
├── .env.example.txt     # Sample environment variables
└── README.md            # This file
 🚀 Getting Started
1️⃣ Backend (Rasa)
bash
Copy
Edit
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
Found in the /archive folder:

auto_fix_rasa.py

check_columns.py

clean_requirements.py

fix_rasa_conflicts.py

database.sqlite3 (deprecated)

These are not actively used but saved for debugging/version control.

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

### **`SECURITY.md`**:

```markdown
# 🔐 Security Policy

## Supported Versions

This project is under active development. We currently support only the latest version.

| Version  | Supported |
| -------- | --------- |
| Latest   | ✅        |
| < Latest | ❌        |

---

## 📢 Reporting a Vulnerability

If you find a **security vulnerability** or issue in this project:

- **Please DO NOT** open a public issue.
- Instead, **email the maintainer directly** at:

📧 **abi131205 [at] gmail [dot] com**

Include the following in your message:
- Clear description of the issue
- Steps to reproduce (if possible)
- Any screenshots or logs
- Suggestions (optional)

We’ll respond as soon as possible (within a few days) and handle the issue privately and respectfully.

---

## 🙏 Thanks

Thank you for helping make this project safer for everyone! 💙

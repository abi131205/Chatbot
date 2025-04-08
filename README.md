# 🤖 Chatbot Application

A complete chatbot system built with:

- 🧠 **Rasa** for NLP and intent classification  
- 💬 **React** for frontend user interface  
- 🗃️ **SQLite** for conversation data storage  
- ⚙️ **Flask** or **FastAPI** backend (`app.py`) as API interface  

---

## 📁 Project Structure

```
Chatbot/
├── .rasa/                 # Rasa config
├── .venv/                 # Virtual environment (not pushed to Git)
├── .vscode/               # VS Code settings
├── Chatbot/               # Possibly React build or helper dir
├── actions/               # Rasa custom actions
├── archive/               # Archived/deprecated scripts
├── data/                  # NLU, stories, and rules data
├── models/                # Rasa trained models
├── my-backend/            # Backend setup (Rasa)
├── my-frontend/           # React-based frontend
├── tests/                 # Test scripts (if any)
├── app.py                 # Flask/FastAPI backend API
├── db.sqlite3             # Active database
├── .env.example.txt       # Environment variable sample
└── README.md              # You're here!
```

---

## 🚀 Getting Started

### 1️⃣ Backend (Rasa)

```bash
cd my-backend/
pip install -r requirements.txt

# Train the model
rasa train

# Start the action server (new terminal)
rasa run actions

# Start the Rasa HTTP server
rasa run --enable-api
```

---

### 2️⃣ Frontend (React)

```bash
cd ../my-frontend/
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

### 3️⃣ Backend Bridge API (`app.py`)

```bash
# From root folder
python app.py
```

Expected output:
```json
{
  "message": "API is running!"
}
```

---

## 🔐 Environment Setup

Create a `.env` file in `my-backend/` (or where needed):

```ini
API_KEY=your_api_key_here
DATABASE_URL=sqlite:///db.sqlite3
```

Use `python-dotenv` to load these in your app if required.

---

## 🧹 Archived Scripts (Not Needed Anymore)

These were moved to `/archive` during cleanup:

- `auto_fix_rasa.py`
- `check_columns.py`
- `database.sqlite3` (old)
- `clean_requirements.py`
- `fix_rasa_conflicts.py`

They’re kept for reference but not used in production.

---

## 🧪 Testing

To test your chatbot in terminal:

```bash
rasa shell
```

Frontend tests (if any):

```bash
npm test
```

---

## 🛠️ Dependencies

Backend:
- `rasa`
- `flask` or `fastapi`
- `sqlalchemy`
- `python-dotenv`

Frontend:
- `react`
- `axios`
- `styled-components` *(optional)*

---

## 📄 License

MIT License  
Free for personal and commercial use.

---

## ✨ Author

Made with ❤️ by [@abi131205](https://github.com/abi131205)


# 🤖 Chatbot Application

A complete chatbot system built with:

- 🧠 **Rasa** for NLP and intent classification  
- 💬 **React** for the frontend user interface  
- 🗃️ **SQLite** for storing conversations  
- ⚙️ **Flask** or **FastAPI** (`app.py`) for backend API bridging  

---

## 📁 Project Structure

```
Chatbot/
├── .rasa/                 # Rasa configuration
├── .venv/                 # Python virtual environment
├── .vscode/               # VS Code editor settings
├── actions/               # Custom Rasa actions
├── archive/               # Archived/deprecated utilities
├── data/                  # Training data: NLU, stories, rules
├── models/                # Trained Rasa models
├── my-backend/            # Rasa backend project
├── my-frontend/           # React frontend
├── tests/                 # Unit tests (optional)
├── app.py                 # Flask/FastAPI middleware API
├── db.sqlite3             # SQLite database
├── .env.example.txt       # Sample environment variables
└── README.md              # This file
```

---

## 🚀 Getting Started

### 1️⃣ Backend (Rasa)

```bash
cd my-backend/
pip install -r requirements.txt

# Train the chatbot model
rasa train

# Start custom actions (in a separate terminal)
rasa run actions

# Start Rasa server with API enabled
rasa run --enable-api
```

---

### 2️⃣ Frontend (React)

```bash
cd ../my-frontend/
npm install
npm start
```

Then open 👉 [http://localhost:3000](http://localhost:3000) in your browser.

---

### 3️⃣ Bridge API Server (`app.py`)

This is the Flask or FastAPI server acting as a bridge between frontend and backend.

```bash
# From the root directory
python app.py
```

Expected response in browser or Postman:

```json
{
  "message": "API is running!"
}
```

---

## 🔐 Environment Setup

Create a `.env` file in `my-backend/` or root as needed:

```ini
API_KEY=your_api_key_here
DATABASE_URL=sqlite:///db.sqlite3
```

You may use `python-dotenv` or similar tools to load environment variables into `app.py`.

---

## 📦 Archived Scripts (For Reference Only)

Located in the `/archive` folder:

- `auto_fix_rasa.py`
- `check_columns.py`
- `clean_requirements.py`
- `fix_rasa_conflicts.py`
- `database.sqlite3` (deprecated)

Not actively used but preserved for version tracking.

---

## 🧪 Testing

To test Rasa directly:

```bash
rasa shell
```

To test React frontend (if configured):

```bash
npm test
```

---

## 🛠️ Tech Stack

### Backend:
- `rasa`
- `flask` or `fastapi`
- `sqlalchemy`
- `python-dotenv`

### Frontend:
- `react`
- `axios`
- `tailwindcss` *(optional)*
- `react-icons`

---

## 📄 License

MIT License  
Free to use for personal and commercial projects.

---

## ✨ Author

Built with ❤️ by [@abi131205](https://github.com/abi131205)

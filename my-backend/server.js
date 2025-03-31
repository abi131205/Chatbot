require("dotenv").config();
const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");

const app = express();

// ✅ Consolidated CORS Configuration (Only Use This)
app.use(cors({
  origin: ["http://localhost:3000", "https://chatbot-nhw1.onrender.com"] ,// Allow frontend
  methods: ["GET", "POST", "OPTIONS"], // Allowed methods
  allowedHeaders: ["Content-Type", "Authorization"], // Allow headers
  credentials: true 
}));

// ✅ Manually Set Headers (Extra Fix)
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "https://localhost:3000"); // Allow frontend
    res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
    res.header("Access-Control-Allow-Credentials", "true");
    next();
});

app.use(express.json());

// ✅ Root Route to Verify Deployment
app.get("/", (req, res) => {
  res.send("✅ Chatbot backend is running!");
});

// ✅ Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("✅ MongoDB connected successfully!"))
  .catch((err) => console.error("❌ MongoDB connection error:", err));

// ✅ Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));

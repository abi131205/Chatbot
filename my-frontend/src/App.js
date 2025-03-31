import React, { useState } from "react";
import axios from "axios"; // Import axios for API calls

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://127.0.0.1:5000";

const App = () => {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [symptoms, setSymptoms] = useState([]);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // ✅ Fetch API root message (Testing connection)
  const fetchWelcomeMessage = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/`);
      setResult(response.data);
    } catch (error) {
      setResult({ error: "Failed to fetch data" });
    }
  };

  // ✅ Send a message to the chatbot
  const sendMessage = async () => {
    if (!message.trim()) return; // Prevent empty messages

    setLoading(true);
    setChatHistory((prev) => [...prev, { sender: "user", text: message }]);

    try {
      // 🔹 Call the chatbot API (New `/chat` endpoint)
      const res = await axios.post(`${API_BASE_URL}/chat`, { message });

      setChatHistory((prev) => [...prev, { sender: "bot", text: res.data.reply }]);
    } catch (error) {
      setChatHistory((prev) => [...prev, { sender: "bot", text: "Something went wrong!" }]);
    }

    setMessage("");
    setLoading(false);
  };

  // ✅ Predict disease based on symptoms
  const handlePredict = async () => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_BASE_URL}/predict`, { symptoms });
      setResult(response.data);
    } catch (error) {
      setResult({ error: "Prediction failed" });
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">AI Medical Chatbot</h1>

      {/* Chat Display */}
      <div className="w-1/2 bg-white p-4 rounded shadow-md h-96 overflow-y-auto">
        {chatHistory.length === 0 ? (
          <p className="text-gray-500">Start a conversation...</p>
        ) : (
          chatHistory.map((chat, index) => (
            <div key={index} className={`flex ${chat.sender === "user" ? "justify-end" : "justify-start"}`}>
              <p className={`p-2 rounded w-fit mt-1 ${chat.sender === "user" ? "bg-blue-500 text-white" : "bg-gray-300"}`}>
                <strong>{chat.sender === "user" ? "You" : "Bot"}:</strong> {chat.text}
              </p>
            </div>
          ))
        )}
      </div>

      {/* User Input */}
      <textarea
        className="border p-2 w-1/2 rounded mt-4"
        rows="3"
        placeholder="Ask a medical question..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      {/* Send Button */}
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded mt-2 disabled:opacity-50"
        onClick={sendMessage}
        disabled={loading}
      >
        {loading ? "Sending..." : "Send"}
      </button>

      {/* Symptoms Input */}
      <input
        type="text"
        className="border p-2 w-1/2 rounded mt-4"
        placeholder="Enter symptoms (comma separated)..."
        onChange={(e) => setSymptoms(e.target.value.split(","))}
      />

      {/* Predict Button */}
      <button
        className="bg-green-500 text-white px-4 py-2 rounded mt-2 disabled:opacity-50"
        onClick={handlePredict}
        disabled={loading}
      >
        {loading ? "Predicting..." : "Predict Disease"}
      </button>

      {/* API Test Button */}
      <button className="bg-gray-500 text-white px-4 py-2 rounded mt-2" onClick={fetchWelcomeMessage}>
        Test API Connection
      </button>

      {/* Prediction Result */}
      {result && <pre className="mt-4 p-2 bg-white rounded">{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
};

export default App;

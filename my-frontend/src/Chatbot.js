import React, { useState } from "react";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, { text: input, sender: "user" }]);
    setInput("");
  };

  return (
    <div className="max-w-xl mx-auto mt-10 p-4 border rounded-lg shadow-lg">
      <div className="h-80 overflow-y-auto border-b p-3">
        {messages.map((msg, index) => (
          <div key={index} className={msg.sender === "user" ? "text-right" : "text-left"}>
            <p className={msg.sender === "user" ? "bg-blue-500 text-white p-2 rounded-lg inline-block" : "bg-gray-200 p-2 rounded-lg inline-block"}>
              {msg.text}
            </p>
          </div>
        ))}
      </div>
      <div className="flex mt-4">
        <input
          type="text"
          className="flex-1 p-2 border rounded-lg"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="bg-blue-500 text-white p-2 ml-2 rounded-lg" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;

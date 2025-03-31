import axios from "axios";

// Automatically use local backend during development, and a deployed URL in production
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://127.0.0.1:5000"; 

export const getData = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/`); // ✅ Fetch data from backend
    return response.data;
  } catch (error) {
    console.error("❌ Error fetching data:", error.message);
    return { error: "Failed to fetch data" };
  }
};

export const predictDisease = async (symptoms) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/predict`, { symptoms }); // ✅ Predict disease
    return response.data;
  } catch (error) {
    console.error("❌ Error predicting disease:", error.response?.data || error.message);
    return { error: error.response?.data || "Unknown error" };
  }
};

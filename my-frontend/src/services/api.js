import axios from "axios";

const API_BASE_URL = "https://your-app-name.onrender.com"; // Replace with your Render backend URL

export const getData = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/your-endpoint`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

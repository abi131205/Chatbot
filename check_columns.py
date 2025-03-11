import pandas as pd

# Load the dataset
file_path = "medical_chatbot_dataset.csv"
data = pd.read_csv(file_path)

# Print the actual column names
print("Dataset Columns:", data.columns.tolist())

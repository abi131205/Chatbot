import pandas as pd # type: ignore
import nltk # type: ignore
import string
from nltk.corpus import stopwords # type: ignore
from nltk.tokenize import word_tokenize # type: ignore
from textblob import TextBlob # type: ignore

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load dataset
data = pd.read_csv("medical_chatbot_dataset.csv")

# Function to correct spelling
def correct_spelling(text):
    return str(TextBlob(text).correct())

# Function to preprocess text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = correct_spelling(text)  # Correct spelling mistakes
    words = word_tokenize(text)  # Tokenize words
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    return " ".join(words)

# Apply preprocessing
data['Symptoms'] = data['Symptoms'].apply(clean_text)

# Save processed data
data.to_csv("processed_medical_chatbot_dataset.csv", index=False)
print("Preprocessing Enhanced!")
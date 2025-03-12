import pandas as pd # type: ignore
import tensorflow as tf # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense, Embedding, Bidirectional # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv("processed_medical_chatbot_dataset.csv")
print(data.head())

# Tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data['Symptoms'])
X = tokenizer.texts_to_sequences(data['Symptoms'])
X = pad_sequences(X, maxlen=10)

# Encode labels
label_mapping = {disease: i for i, disease in enumerate(data['Possible_Diagnosis'].unique())}
y = data['Possible_Diagnosis'].map(label_mapping)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build LSTM Model
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=10),
    Bidirectional(LSTM(64, return_sequences=True)),
    Bidirectional(LSTM(32)),
    Dense(32, activation='relu'),
    Dense(len(label_mapping), activation='softmax')
])

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save model & tokenizer
model.save("disease_prediction_model.h5")
joblib.dump(tokenizer, "tokenizer.pkl")
joblib.dump(label_mapping, "label_mapping.pkl")

print("Deep Learning Model Trained!")
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense, Embedding, Bidirectional # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv("processed_medical_chatbot_dataset.csv")
print(data.head())

# Tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data['Symptoms'])
X = tokenizer.texts_to_sequences(data['Symptoms'])
X = pad_sequences(X, maxlen=10)

# Encode labels
label_mapping = {disease: i for i, disease in enumerate(data['Possible_Diagnosis'].unique())}
y = data['Possible_Diagnosis'].map(label_mapping)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build LSTM Model
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=10),
    Bidirectional(LSTM(64, return_sequences=True)),
    Bidirectional(LSTM(32)),
    Dense(32, activation='relu'),
    Dense(len(label_mapping), activation='softmax')
])

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save model & tokenizer
model.save("disease_prediction_model.h5")
joblib.dump(tokenizer, "tokenizer.pkl")
joblib.dump(label_mapping, "label_mapping.pkl")

print("Deep Learning Model Trained!")

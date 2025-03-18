essential = {
    "Flask", "gunicorn", "python-dotenv", "requests",
    "SQLAlchemy", "pymongo", "nltk", "spacy", "transformers",
    "rasa", "chatterbot", "tensorflow", "scikit-learn"
}

with open("clean_requirements.txt") as f, open("requirements.txt", "w") as out:
    for line in f:
        package = line.split("==")[0].strip()  # Extract package name and remove spaces
        if package in essential:
            out.write(line)

print("Script finished. Check requirements.txt")

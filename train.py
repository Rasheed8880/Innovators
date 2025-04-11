import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Sample data (replace with real medical fake/real dataset)
data = {
    "text": [
        "Vaccines cause autism.",
        "The CDC confirms masks reduce COVID-19 transmission.",
        "Drinking bleach cures coronavirus.",
        "Handwashing prevents infection.",
        "5G spreads viruses.",
        "WHO recommends regular physical activity for health."
    ],
    "label": [0, 1, 0, 1, 0, 1]  # 0 = Fake, 1 = Real
}

df = pd.DataFrame(data)

# Split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)

# Vectorize
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained and saved to model/model.pkl")

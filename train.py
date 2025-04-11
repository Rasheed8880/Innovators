import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# ✅ Correct dataset: 50 texts and 50 labels
data = {
    "text": [
        "Vaccines cause autism.",
        "The CDC confirms masks reduce COVID-19 transmission.",
        "Drinking bleach cures coronavirus.",
        "Handwashing prevents infection.",
        "5G spreads viruses.",
        "WHO recommends regular physical activity for health.",
        "COVID-19 vaccines contain microchips for government tracking.",
        "A healthy diet boosts your immune system.",
        "Wearing garlic necklaces prevents flu.",
        "Antibiotics do not work against viral infections.",
        "Essential oils cure cancer.",
        "Regular sleep improves mental health.",
        "Bill Gates created COVID-19 to profit from vaccines.",
        "HIV cannot be transmitted through casual contact.",
        "You can detox your body by drinking only juice for 7 days.",
        "Measles vaccination prevents deadly outbreaks.",
        "The moon’s phase affects virus spread.",
        "Getting the flu shot reduces risk of serious illness.",
        "COVID-19 can be cured by drinking hot water every hour.",
        "Exercise reduces the risk of heart disease.",
        "Holding your breath for 10 seconds can diagnose COVID-19.",
        "Washing fruits and vegetables reduces pesticide intake.",
        "Sunlight exposure helps produce vitamin D.",
        "Magnet therapy can treat chronic diseases.",
        "Smoking herbal blends is safer than tobacco.",
        "Vaccines are thoroughly tested for safety and effectiveness.",
        "Wearing masks leads to carbon dioxide poisoning.",
        "WHO states that vaccines undergo multiple trial phases.",
        "Taking antibiotics before COVID-19 infection prevents it.",
        "Obesity is a major risk factor for severe COVID-19 outcomes.",
        "COVID-19 is a hoax created by pharmaceutical companies.",
        "Breastfeeding boosts babies’ immune systems.",
        "Eating spicy food kills COVID-19 virus.",
        "Proper sanitation helps prevent waterborne diseases.",
        "The polio vaccine has helped eradicate polio in many countries.",
        "Rubbing alcohol on the skin protects from airborne viruses.",
        "HPV vaccines prevent certain types of cancers.",
        "The COVID-19 vaccine changes your DNA.",
        "Mental health support improves patient recovery rates.",
        "Inhaling steam prevents coronavirus infection.",
        "Medical research is peer-reviewed for accuracy.",
        "Microwaving food makes it radioactive.",
        "A balanced diet helps maintain overall health.",
        "Taking mega doses of Vitamin C cures COVID-19.",
        "Public health guidelines help control disease outbreaks.",
        "Eating silver particles boosts immunity.",
        "Wearing tight clothes increases blood circulation.",
        "Zinc supplements help reduce cold symptoms.",
        "Natural immunity is better than vaccination.",
        "Vaccination helps create herd immunity."
    ],
    "label": [
        0, 1, 0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 1, 0, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1, 1, 0,
        1, 0, 1, 0,
        1, 0, 1, 0,
        0, 1, 0, 0, 1, 1  # ✅ Last label corrected to make it 50
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorize the text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train the model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained and saved to model/model.pkl")

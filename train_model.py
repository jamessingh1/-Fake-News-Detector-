# scripts/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load data
df = pd.read_csv("../merged/news.csv")

# Split features and labels
X = df['text']
y = df['label']

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = PassiveAggressiveClassifier(max_iter=1000)
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "../model/fake_news_model.pkl")
joblib.dump(vectorizer, "../model/vectorizer.pkl")

# Accuracy
y_pred = model.predict(X_test)
print("✅ Model Accuracy:", accuracy_score(y_test, y_pred))

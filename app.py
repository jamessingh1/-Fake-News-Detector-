# streamlit_app/app.py

import streamlit as st
import joblib

# Load model
model = joblib.load("../model/fake_news_model.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")

st.title("📰 Fake News Detection App")

text_input = st.text_area("Enter News Article Text Below:")

if st.button("Check News"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        text_vec = vectorizer.transform([text_input])
        prediction = model.predict(text_vec)[0]
        label = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
        st.success(f"Prediction: {label}")

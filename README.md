
# 📰 Fake News Detector with Streamlit

A professional machine learning project that detects **Fake News** using Natural Language Processing (NLP) and provides a modern **Streamlit UI** for user interaction. The model is trained on real and fake news articles and classifies whether the given news is genuine or misleading.

---

## 📁 Project Structure

```
Fake_News_Detection/
│
├── data/                  # Raw dataset files
│   ├── Fake.csv
│   └── True.csv
│
├── merged/                # Final combined dataset
│   └── news.csv
│
├── model/                 # Trained ML model & vectorizer
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
│
├── scripts/               # Backend logic and training scripts
│   ├── merge_datasets.py
│   └── train_model.py
│
├── streamlit_app/         # Streamlit frontend interface
│   └── app.py
│
├── requirements.txt       # Project dependencies
├── .gitignore             # Files to ignore in Git
└── README.md              # You're here!
```

---

## 🚀 Features

- Clean and labeled dataset merge from `Fake.csv` and `True.csv`
- Text preprocessing and TF-IDF feature extraction
- Supervised learning (Logistic Regression) for classification
- Interactive fake news checker using Streamlit
- Trained model stored with `joblib` for quick re-use

---

## ⚙️ How to Run

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/jamessingh1/-Fake-News-Detector-.git
cd Fake_News_Detection
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧠 3. Merge & Train Model

```bash
cd scripts
python merge_datasets.py
python train_model.py
```

### 🖥️ 4. Launch Streamlit App

```bash
cd ../streamlit_app
streamlit run app.py
```

> ✅ The Streamlit interface will open in your browser at `http://localhost:8501`.

---

## 🧪 Sample Input

> *Enter a news article or snippet in the text box to check if it’s real or fake.*

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- TF-IDF Vectorizer

---

## 📌 Dataset Source

- **Fake.csv** & **True.csv** from Kaggle:  
  [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## 🙋‍♂️ Author

**James Singh**  
[GitHub Profile](https://github.com/jamessingh1)

---

## 📝 License

This project is licensed under the MIT License.

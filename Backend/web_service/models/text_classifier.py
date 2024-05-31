import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# 간단한 텍스트 요약 함수
def summarize_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text[:500]  # 요약본으로 500자 제한

# 간단한 텍스트 분류 함수 (사전 학습된 모델이 있다고 가정)
def classify_text(text):
    model = joblib.load('models/nb_model.pkl')
    vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]

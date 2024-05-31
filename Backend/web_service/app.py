# app.py

from flask import Flask, request, jsonify, render_template
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from models.text_classifier import classify_text, summarize_text

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_urls():
    urls = request.json.get('urls', [])
    results = []
    for url in urls:
        summary = summarize_text(url)
        classification = classify_text(summary)
        results.append({'url': url, 'summary': summary, 'classification': classification})
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

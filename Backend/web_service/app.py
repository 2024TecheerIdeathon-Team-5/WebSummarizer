from flask import Flask, request, jsonify, render_template
import mysql.connector
import os
from dotenv import load_dotenv
from models.text_classifier import classify_text, summarize_text
from summarize import summarize_url
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)

load_dotenv()

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB")
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_url_route():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        summary = summarize_url(url)
        return jsonify({'url': url, 'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/articles', methods=['GET'])
def get_articles():
    conn = None
    cursor = None
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Query to select all articles
        cursor.execute("SELECT * FROM Article")
        articles = cursor.fetchall()

        return jsonify({'articles': articles}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


@app.route('/articles/<int:id>', methods=['DELETE'])
def delete_article(id):
    conn = None
    cursor = None
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Delete the article with the given ID
        cursor.execute("DELETE FROM Article WHERE id = %s", (id,))
        conn.commit()

        return jsonify({'message': 'Article deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5002)

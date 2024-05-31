from flask import Flask, request, jsonify, render_template
import mysql.connector
from dbconfig import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
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
def summarize_url_route():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        summary = summarize_url(url)
        return jsonify({'url': url, 'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/prob')
def prob():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM bookmark")
        bookmark = cursor.fetchall()
        
        cursor.execute("SELECT * FROM category")
        category = cursor.fetchall()
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    
    return render_template('prob.html', bookmark=bookmark, category=category)

if __name__ == '__main__':
    app.run(debug=True)

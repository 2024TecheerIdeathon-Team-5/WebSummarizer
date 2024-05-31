from flask import Flask, request, jsonify, render_template
import mysql.connector
from dbconfig import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from summarize import summarize_url

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
        result = summarize_url(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_article/<int:id>', methods=['DELETE'])
def delete_article(id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
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

@app.route('/articles', methods=['POST'])
def save_summary():
    data = request.json
    title = data.get('title')
    summary = data.get('summary')
    url = data.get('url')
    image_url = data.get('image_url')
    category = data.get('category')

    if not url or not summary or not category or not title or not image_url:
        return jsonify({'error': 'All fields are required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Article (title, summary, url, image_url, category)
            VALUES (%s, %s, %s, %s, %s)
        """, (title, summary, url, image_url, category))
        conn.commit()
        return jsonify({'message': 'Data saved successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)})
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

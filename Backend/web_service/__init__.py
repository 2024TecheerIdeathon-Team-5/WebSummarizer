from flask import Flask
import mysql.connector

def create_app():
    app = Flask(__name__)
    
    # 블루프린트 인스턴스 가져오기
    from .views import views
    
    # 플라스크 앱에 등록하기
    app.register_blueprint(views, url_prefix='/')
    
    def create_table():
        print('aa')
        conn = mysql.connector.connect('db.sql')
        cursor = conn.cursor()
        cursor.execute( # bookmark 테이블 생성
            '''
            CREATE TABLE IF NOT EXISTS bookmark (
                id INTEGER PRIMARY KEY,
                `title` varchar(255),
                `url` varchar(255) NOT NULL,
                `summary` text,
                `category_id` int
            )
            '''
        )
        cursor.execute( # category 테이블 생성
            '''
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY,
                `name` varchar(255),
                `parent_id` int
            )
            '''
        )
        conn.close()

    create_table()
    print('Database connection established and tables checked/created.')
    
    return app
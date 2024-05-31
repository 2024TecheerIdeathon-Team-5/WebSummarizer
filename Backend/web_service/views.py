# from flask import Blueprint, render_template
# from app import get_db_connection

# views = Blueprint('views', __name__)

# # @views.route('/prob')
# # def prob():
# #     conn = None
# #     cursor = None
# #     try:
# #         conn = get_db_connection()
# #         cursor = conn.cursor()
        
# #         cursor.execute("SELECT * FROM bookmark")
# #         bookmark = cursor.fetchall()
        
# #         cursor.execute("SELECT * FROM category")
# #         category = cursor.fetchall()
# #     finally:
# #         if cursor is not None:
# #             cursor.close()
# #         if conn is not None:
# #             conn.close()
    
# #     return render_template('prob.html', bookmark=bookmark, category=category)
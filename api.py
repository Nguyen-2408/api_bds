from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Thay đổi các thông số kết nối PostgreSQL của bạn
db_connection = {
    'dbname': 'tintucbds',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': '5432',
}

@app.route('/tintuc', methods=['GET'])
def get_users():
    try:
        conn = psycopg2.connect(**db_connection)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tintucnhadat;")
        news = cursor.fetchall()

        return {'news': news}

        # Chuyển đổi kết quả thành danh sách từ điển
        # news_list = [{
        #     news['title'] ,
        #     main_image ,
        #     area ,
        #     price ,
        #     price_per_m2 ,
        #     bedrooms ,
        #     toilet ,
        #     locations ,
        #     description ,
        #     agent_name ,
        #     last_updated 

        #     } 
        #     for user in news]

        return jsonify(news)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
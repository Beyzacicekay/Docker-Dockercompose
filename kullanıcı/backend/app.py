from flask import Flask, jsonify
import psycopg2
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        database=os.environ.get("DB_NAME", "mydb"),
        user=os.environ.get("DB_USER", "myuser"),
        password=os.environ.get("DB_PASSWORD", "mypass"),
        port=os.environ.get("DB_PORT", 5432)
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    cur.execute("INSERT INTO users (name) VALUES ('Emre'), ('Zeynep') ON CONFLICT DO NOTHING;")
    conn.commit()
    cur.close()
    conn.close()

@app.route('/users')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM users;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([row[0] for row in results])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

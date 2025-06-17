from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            dbname="proje",
            user="admin",
            password="secret",
            host="db",  # docker-compose'daki servis adı
            port="5432"
        )
        return "✅ PostgreSQL bağlantısı başarılı!"
    except Exception as e:
        return f"🚨 Bağlantı hatası: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

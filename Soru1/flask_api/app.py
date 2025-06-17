from flask import Flask, request, jsonify
import pickle
import numpy as np
import re

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open('model.pkl', 'rb'))

def preprocess(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = preprocess(data.get('text', ''))
    features = np.array([len(text), text.count('!')]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({'sentiment': 'positive' if prediction == 1 else 'negative'})

@app.route('/', methods=['GET'])
def index():
    return "Duygu Analizi API Çalışıyor!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

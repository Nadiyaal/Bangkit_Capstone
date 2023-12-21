from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)
CORS(app)

# Load machine learning model
model = joblib.load('models/recommendation_model.pkl')

# Load sales data (contoh data)
sales_data = pd.read_csv('data/sales_data.csv')

@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        # Terima data dari frontend
        data = request.json

        # Proses data untuk mendapatkan rekomendasi
        user_id = data['user_id']  # Misalnya, user_id dari frontend
        user_sales_data = sales_data[sales_data['user_id'] == user_id]

        # Prediksi menggunakan model machine learning
        recommended_items = model.predict(user_sales_data)

        # Konversi hasil prediksi menjadi format yang sesuai
        recommendations = [str(item) for item in recommended_items]

        return jsonify({'recommendations': recommendations})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

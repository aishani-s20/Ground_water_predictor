import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Load your trained model
model = joblib.load('water_level_model.joblib')

@app.route('/data', methods=['POST'])
def process_data():
    data = request.json
    
    # Convert the received data to a pandas DataFrame
    df = pd.DataFrame([data])
    
    # Rename columns to match your training data
    df = df.rename(columns={
        'temp': 'Temperature_C',
        'rainfall': 'Rainfall_mm',
        'ph': 'pH',
        'dissolvedOxygen': 'Dissolved_Oxygen_mg_L'
    })
    
    # Ensure the order of columns matches your training data
    df = df[['Temperature_C', 'Rainfall_mm', 'pH', 'Dissolved_Oxygen_mg_L']]
    
    # Make prediction
    prediction = model.predict(df)
    
    return jsonify({
        "message": "Data received and processed successfully",
        "predicted_water_level": float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)
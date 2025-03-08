import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)
CORS(app)  


model = joblib.load('water_level_model.joblib')

@app.route('/data', methods=['POST'])
def process_data():
    data = request.json
    
   
    df = pd.DataFrame([data])
    
 
    df = df.rename(columns={
        'temp': 'Temperature_C',
        'rainfall': 'Rainfall_mm',
        'ph': 'pH',
        'dissolvedOxygen': 'Dissolved_Oxygen_mg_L'
    })
    
    
    df = df[['Temperature_C', 'Rainfall_mm', 'pH', 'Dissolved_Oxygen_mg_L']]
    
 
    prediction = model.predict(df)
    
    return jsonify({
        "message": "Data received and processed successfully",
        "predicted_water_level": float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)
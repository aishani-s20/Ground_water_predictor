# Water Level Prediction Project

This project is a web-based application that predicts water levels based on environmental data (temperature, rainfall, pH, and dissolved oxygen) using a pre-trained Linear Regression model. It consists of a Flask backend server and an HTML/JavaScript frontend.

## Project Structure
```
water_level_project/
├── app.py                   # Flask backend server
├── index.html              # Frontend HTML form
├── script.js               # JavaScript for form submission
├── water_level_model.joblib # Pre-trained machine learning model
├── DWLR_Dataset_2023.csv   # Sample dataset for training (optional)
├── train_model.py          # Script to train and save the model
├── requirements.txt        # Python dependencies
├── Procfile                # Heroku deployment configuration (optional)
└── README.md               # This file
```

## Features
- Input environmental data via a web form
- Predict water levels using a Linear Regression model
- Display the prediction as text below the form
- Show error alerts if the server is unreachable

## Prerequisites
- **Python 3.6+**: Installed on your system ([download here](https://www.python.org/downloads/))
- **Git**: For version control and deployment (optional, [install here](https://git-scm.com/downloads))
- A web browser to access the frontend

## Installation

### 1. Clone or Set Up the Project
If you have the project files:
- Place all files in a directory (e.g., `water_level_project`)
- Navigate to the directory:
  ```bash
  cd path/to/water_level_project
  ```

### 2. Install Dependencies
- Install Python dependencies:
  ```bash
  pip install flask flask-cors pandas numpy scikit-learn joblib
  ```

- If pip doesn't work, try:
  ```bash 
  pip3 install flask flask-cors pandas numpy scikit-learn joblib
  ```

### 3. Verify Files
Ensure the following files are present:
- `data.py`: Flask server script
- `index.html`: Frontend form
- `script.js`: JavaScript logic
- `water_level_model.joblib`: Pre-trained model

If the model file is missing, generate it with:
```bash 
python model.py
```

## Running the Application

### 1. Start the Flask Server
- Open a terminal in the project directory:
  ```bash
  cd path/to/water_level_project
  ```
- Run the Flask app:
  ```bash
  python data.py
  ```

### 2. Serve the Frontend
- Open a second terminal window
- Run a simple HTTP server:
  ```bash
  python -m http.server 8000
  ```
- Open your browser and go to:
  ```
  http://localhost:8000/index.html
  ```

## Usage
1. Enter values for temperature, rainfall, pH, and dissolved oxygen in the form
2. Click "Predict Water Level"
3. View the predicted water level displayed below the form

## Troubleshooting
- If you encounter CORS issues, ensure Flask-CORS is properly installed and configured
- If the model file is missing, run `python model.py` to generate it
- Check console logs in your browser for JavaScript errors
- Verify that the Flask server is running on the expected port

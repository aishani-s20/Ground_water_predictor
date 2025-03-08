# Water Level Prediction Project

This project is a web-based application that predicts water levels based on environmental data (temperature, rainfall, pH, and dissolved oxygen) using a pre-trained Linear Regression model. It consists of a Flask backend server and an HTML/JavaScript frontend.

## Project Structure
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


## Features
- Input environmental data via a web form.
- Predict water levels using a Linear Regression model.
- Display the prediction as text below the form.
- Show error alerts if the server is unreachable.

## Prerequisites
- **Python 3.6+**: Installed on your system ([download here](https://www.python.org/downloads/)).
- **Git**: For version control and deployment (optional, [install here](https://git-scm.com/downloads)).
- A web browser to access the frontend.

## Installation

### 1. Clone or Set Up the Project
If you have the project files:
- Place all files in a directory (e.g., `water_level_project`).
- Navigate to the directory:
  ```bash
  cd path/to/water_level_project
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import tkinter as tk
from tkinter import scrolledtext

# Load dataset
# Replace 'your_dataset.csv' with the actual dataset file path
data = pd.read_csv("properties_public.csv", dtype=str)

# Data Preprocessing

# Drop rows with missing values to ensure the quality of our model input
data.dropna(inplace=True)

# Feature Engineering
# Convert features to numeric as operations require numerical types
data['feature1'] = pd.to_numeric(data['feature1'])
data['feature2'] = pd.to_numeric(data['feature2'])
data['target_variable'] = pd.to_numeric(data['target_variable'])

# Add a new feature representing the ratio of two existing features
data['feature_ratio'] = data['feature1'] / data['feature2']

# Model Development

# Prepare the features (X) and target variable (y)
X = data.drop('target_variable', axis=1)
y = data['target_variable']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models with their respective settings
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting Regressor': GradientBoostingRegressor(n_estimators=100, random_state=42)
}

# Function to train and evaluate models, then display results in the GUI
def evaluate_models():
    results = ""
    for name, model in models.items():
        model.fit(X_train, y_train)  # Train model
        y_pred = model.predict(X_test)  # Predict on test set
        mse = mean_squared_error(y_test, y_pred)  # Calculate MSE
        mae = mean_absolute_error(y_test, y_pred)  # Calculate MAE
        results += f'{name} - MSE: {mse:.4f}, MAE: {mae:.4f}\n'
    return results

# GUI for displaying results
def show_results():
    # Create a GUI window
    root = tk.Tk()
    root.title("Model Evaluation Results")
    
    # Create a scrolled text area widget
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    text_area.grid(column=0, pady=10, padx=10)
    
    # Evaluate models and get results
    evaluation_results = evaluate_models()
    
    # Insert the results in the text area and disable editing
    text_area.insert(tk.INSERT, evaluation_results)
    text_area.configure(state='disabled')
    
    root.mainloop()

# Run the function to show results in a GUI
show_results()

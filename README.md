# House Price Prediction in Nepal

This is a machine learning project that predicts house prices in Nepal.

## What This Project Does
- Cleans and processes house price data
- Converts different area units (Ropani, Aana, Sqft) to standard Aana
- Extracts neighborhoods from addresses
- Encodes categories (City, Amenities, etc.)
- Trains 3 machine learning models (Linear Regression, Random Forest, XGBoost)
- Compares model performance

## Files in This Project
- .gitignore = Prevents Git from tracking, staging, or uploading unnecessary files
- config.py = All settings and constants
- house_price_prediction.ipynb = Main notebook with all code
- requirements.txt = List of libraries needed
- README.md = This file

## How To Use
1. Install Python libraries: pip install -r requirements.txt
2. Open house_price_prediction.ipynb in Jupyter
3. Run all cells

## Results
- Linear Regression: 59.6% accuracy
- Random Forest: 79.1% accuracy
- XGBoost: 79.4% accuracy (BEST)

## Author
Dipesh Pandey

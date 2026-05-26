"""
Configuration file for House Price Prediction
All constants and thresholds in ONE place
"""

# ============================================================
# AREA CONVERSION CONSTANTS (AANA BASE SYSTEM)
# ============================================================

AANA_TO_SQFT = 342.25
AANA_TO_SQMT = 31.80

# Hill system
ROPANI_TO_AANA = 16
PAISA_TO_AANA = 0.25
DAM_TO_AANA = 0.0625

# Terai system
BIGHA_TO_AANA = 212.8
KATTHA_TO_AANA = 10.64
DHUR_TO_AANA = 0.532

# Standard system
SQFT_TO_AANA = 1 / AANA_TO_SQFT
SQMT_TO_AANA = 1 / AANA_TO_SQMT

# Local system
HAAT_TO_SQFT = 2.25
HAAT_TO_AANA = HAAT_TO_SQFT * SQFT_TO_AANA

# ============================================================
# DATA QUALITY THRESHOLDS
# ============================================================

MIN_AREA_AANA = 2.8
MAX_AREA_AANA = 192
MIN_PRICE_PER_AANA = 100000
MAX_PRICE_PER_AANA = 35000000


MIN_ROAD_WIDTH_FEET = 10
MAX_ROAD_WIDTH_FEET = 48
METER_TO_FEET = 3.281

# ============================================================
# FEATURE ENGINEERING
# ============================================================

TOP_NEIGHBORHOODS = 20
banned_tokens = {'na', 'n/a', 'none', 'unknown', 'null'}
continuous_features = ['Bedroom', 'Bathroom', 'Floors', 'Parking', 'RoadWidth_feet', 'area_aana_log']

NUMERIC_LIMITS = {
    'Bedroom': 17,
    'Bathroom': 10,
    'Floors': 5,
    'Parking': 10
}

# ============================================================
# GARBAGE AREA VALUES TO DROP
# ============================================================

drop_area_values = [
    '8.10.0.0 Aana', '5.2.2 Aana', '4.9.0.0 Aana',
    '4.1.1 Aana', '3.3.1 Aana', '3.1.2 Aana',
    '3.1.0 Aana', '3.0.2 Aana', '0.5.3.0 Aana',
    '0.4.0.0 Aana', '0.3.3.3 Aana', '0.3.0.0 Aana',
    '00 Aana', '1111111111111 Aana',
    '1+ Ropani', '4+ Aana',
    '12 Aman Aana', '8 Anand Aana', '55 Anand Aana',
    '10 ana Aana', '18 ana Aana', '29 ana Aana',
    '3.1 ana Aana', '4 ana Aana', '5 ana Aana',
    '5.5 ana Aana', '6 ana Aana', '5 aana Aana',
    '4 anna Aana', '5.5 aana Aana',
    '2 ropani Ropani', '2r Aana', '3 ropani Aana',
    '3 -4 Pieces Aana', '3 to 5 Anna Aana',
    '4,5,6,7,8 aana Aana', '0-8,9,10-0-0 Aana',
    '4/2/2 Aana', '5/10/20 Aana',
    '5/5/6 Aana', '4/4/5/5/6 Aana',
    'dont know Sq. Feet',
    '500sqft Sq. Feet', '968sqft Sq. Feet', '1600sq/ft Aana',
    '3.3aana Aana',
    '11:10 Kattha',
    '3-5 Sq. Feet',
    '04-02 Sq. Feet',
    '22 Haat',
    '20 Haat',
]

# ============================================================
# VALID UNITS
# ============================================================

allowed_units = {
    'aana', 'sqft', 'ropani', 'dhur',
    'kattha', 'haat', 'sqm', 'bigha', 'paisa'
}

# ============================================================
# COLUMNS TO DROP BEFORE TRAINING
# ============================================================

columns_to_drop = [
    'Area', 'Road Width', 'Build Area', 'Area_fixed', 'value_raw', 
    'unit_raw', 'unit_clean', 'unit_final', 'land_system', 'value_norm', 
    'title_clean', 'RoadType_missing', 'unit_invalid_flag', 'is_bad', 
    'valid_format_flag', 'Price', 'price_per_aana', 'Price_total', 
    'price_per_aana_log', 'area_aana'
]

# ============================================================
# MODEL TRAINING
# ============================================================

TEST_SIZE = 0.2
RANDOM_STATE = 42
LEARNING_RATE =0.1
N_ESTIMATORS =100
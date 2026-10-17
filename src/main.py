import os
import pandas as pd
from extract.reader import read_sales_data
from quality.validator import validate_and_reject
from transform.cleaner import clean_and_transform
from load.loader import load_data_to_db

def run_pipeline():
    print("--- BẮT ĐẦU CHẠY LUỒNG ETL (SPRINT 1) ---")
    
    sample_file = "data/sample/orders_2024_2026.csv"
    db_path = "smart_crm_dwh.db"
    
    # 1. EXTRACT
    df_raw = read_sales_data(sample_file)
    
    # 2. QUALITY CHECK
    df_valid = validate_and_reject(df_raw, db_path)
    
    # 3. TRANSFORM
    df_clean = clean_and_transform(df_valid)
    
    # 4. LOAD 
    load_data_to_db(df_clean, db_path)
    
    print("--- HOÀN THÀNH LUỒNG ETL ---")

if __name__ == "__main__":
    run_pipeline()
# -*- coding: utf-8 -*-
"""
VNL 2024 Men's Volleyball – Python to PostgreSQL Data Bridge
------------------------------------------------------------
This script connects to the PostgreSQL database, retrieves the `player_stats` table,
and loads it into a Pandas DataFrame for further analysis or integration with Power BI.
"""

import pandas as pd
import psycopg2

# Database connection details
# Replace these with your actual credentials before running
connection_details = {
    "host": "localhost",
    "database": "volleyball_db",
    "user": "postgres",
    "password": "your_password_here"
}

# SQL query to retrieve data
sql_query = "SELECT * FROM player_stats;"

print("🔗 Connecting to PostgreSQL database...")

try:
    # Establish connection
    conn = psycopg2.connect(**connection_details)
    
    # Execute query and load results into DataFrame
    df = pd.read_sql_query(sql_query, conn)
    
    # Close the connection
    conn.close()
    
    print("✅ Data successfully retrieved from database.")
    print("\nPreview of player_stats table:")
    print(df.head())  # Show first 5 rows
    
except Exception as e:
    print("❌ Connection or query failed.")
    print(f"Error details: {e}")

# VNL 2024 Men's Volleyball – Python to PostgreSQL Data Bridge
# Connects to PostgreSQL, retrieves the player_stats table,
# and loads it into a Pandas DataFrame for analysis or Power BI.

import pandas as pd
import psycopg2

connection_details = {
    "host": "localhost",
    "database": "volleyball_db",
    "user": "postgres",
    "password": "your_password_here"
}

sql_query = "SELECT * FROM player_stats;"

try:
    conn = psycopg2.connect(**connection_details)
    df = pd.read_sql_query(sql_query, conn)
    conn.close()

    print("Data successfully retrieved from database.")
    print("Preview of player_stats table:")
    print(df.head())

except Exception as e:
    print("Connection or query failed.")
    print(f"Error details: {e}")

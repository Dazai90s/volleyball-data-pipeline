# Volleyball Data Pipeline

This project demonstrates an end-to-end ETL pipeline built to analyze player performance in the Men's Volleyball Nations League. The workflow takes raw CSV data, cleans and engineers key metrics using Python, stores the data in a PostgreSQL database, and visualizes it in Power BI. The dashboard connects directly to the database for live, refreshable insights.

## Project Workflow

1. **Tool Setup** – Verified Python and SQL environments were functional.
2. **Data Cleaning** – Used Pandas to clean raw Kaggle data and created an Efficiency Rating metric for each skill.
3. **Database Design** – Built a PostgreSQL database (`volleyball_db`) with a `player_stats` table for cleaned data.
4. **Python–SQL Integration** – Connected Python to PostgreSQL using `psycopg2` to run queries and automate data flow.
5. **Visualization** – Created initial Power BI visuals from CSV, then connected Power BI directly to PostgreSQL for live updates.
6. **Final Pipeline** – Imported cleaned data into the database and refreshed the Power BI report to complete the live pipeline.

## Challenges and Solutions

**Encoding Errors**  
- Problem: CSV files contained special characters that caused read errors.  
- Solution: Used `encoding='latin-1'` to successfully load the files.

**Empty Dataset Issue**  
- Problem: Cleaning code ran without errors but produced empty outputs.  
- Solution: Debugged step-by-step to identify encoding as the root cause.

**Schema Mismatches**  
- Problem: CSV headers did not match database table schema.  
- Solution: Standardized column names to match exactly before import.

## Tools and Technologies

- Python: Pandas, NumPy, psycopg2  
- PostgreSQL with PGAdmin  
- Power BI Desktop  
- GitHub for version control

## Repository Contents

- `volleyball_dashboard.pbix` – Power BI report  
- `player_stats_cleaning.ipynb` – Jupyter Notebook with Python cleaning code  
- `create_tables.sql` – SQL schema creation script  
- `cleaning_queries.sql` – SQL data cleaning script  
- `screenshots/` – PNG images of dashboard visuals

## Next Steps

- Add additional cleaned datasets into the same PBIX as separate pages.  
- Publish an interactive version to Power BI Service.  
- Expand SQL scripts to include advanced queries.

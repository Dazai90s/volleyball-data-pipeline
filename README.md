# VNL 2024 Men's Volleyball Data Pipeline

End-to-end project: Python cleaning → PostgreSQL database → Power BI dashboard. Designed to show real ETL skills, SQL schema design, and interactive visualization in one cohesive workflow.

## Tech stack

- **Python:** Pandas, psycopg2
- **Database:** PostgreSQL
- **BI:** Power BI
- **Files:** CSV → cleaned CSV → SQL → PBIX

## Features

- **Automated cleaning:** Calculates efficiency metrics and fixes CSV encoding across 7 role-based files (Attackers, Receivers, Servers, Setters, Blockers, Diggers, Scorers).
- **Database-ready output:** Cleaned CSVs load into a simple, readable schema for demos/interviews.
- **Python↔Postgres bridge:** Small script that queries the table and returns a DataFrame.
- **Power BI dashboard:** Interactive view with slicers, aligned visuals, and labeled KPIs.

## How to use

1. **Set up PostgreSQL**
   - Create a database named `volleyball_db`.
2. **Create schema**
   - Run `create_tables.sql` in your SQL client.
3. **Load demo/sample data**
   - Run `cleaning_queries.sql` to insert sample rows (for quick demo without Kaggle files).
4. **(Optional) Run full cleaning with Python**
   - `vnl_data_cleaning.py` generates cleaned CSVs from the raw Kaggle files and fixes encoding.
5. **(Optional) Test Python ↔ PostgreSQL**
   - Update credentials in `data_bridge.py` and run to fetch `player_stats` into Pandas.
6. **Open the dashboard**
   - Open `volleyball_dashboard.pbix` in Power BI and explore filters and visuals.

## Repository structure

- `vnl_data_cleaning.py` — Full cleaning pipeline for all CSVs + debug example for Attackers
- `data_bridge.py` — Python-to-PostgreSQL connection and data retrieval (DataFrame preview)
- `create_tables.sql` — Database schema
- `cleaning_queries.sql` — Demo/sample inserts
- `volleyball_dashboard.pbix` — Power BI report
- `images/dashboard.png` — Screenshot (optional)

## Dataset notes

- Uses Kaggle VNL 2024 Men’s role-based CSVs. Some files required `latin-1` encoding; efficiency metrics computed per role.
- Cleaned outputs are designed to be loaded into PostgreSQL and visualized in Power BI.
 
 
## Results and what I learned

- **ETL skills:** Built a repeatable cleaning process with encoding handling and metric calculations.
- **Data modeling:** Created a simple table that demonstrates join-ready, analysis-friendly columns.
- **Visualization:** Produced a clean, interactive Power BI report with consistent colors and aligned visuals.

## Next steps

- Add drill-through pages and bookmarks in Power BI.
- Expand schema to support match-level trend analysis.
- Convert Python scripts into a notebook with inline previews for presentation.

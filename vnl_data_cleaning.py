# -*- coding: utf-8 -*-
"""
VNL 2024 Men's Volleyball Data Cleaning & Debugging
---------------------------------------------------
This script performs two main tasks:

1. Automatic Cleaning Machine:
   - Reads all 7 raw CSV files from the Kaggle VNL 2024 Men's dataset.
   - Fixes encoding issues.
   - Calculates efficiency metrics for each role.
   - Outputs cleaned CSV files for use in PostgreSQL and Power BI.

2. Debug Example for Attackers:
   - Demonstrates the cleaning process on a single file.
   - Shows encoding handling and previews cleaned data.
"""

import pandas as pd

# ============================================================
# PART 1 – AUTOMATIC CLEANING MACHINE
# ============================================================

print("🔧 STARTING THE AUTOMATIC DATA CLEANING MACHINE...")
print("Using Latin-1 encoding to fix the problem...\n")

# Function to read CSV with correct encoding
def read_csv_fixed(filename):
    return pd.read_csv(filename, encoding='latin-1')

# 1. CLEAN RECEIVERS
df = read_csv_fixed('VNL2024Men_Receivers.csv')
df['Efficiency_Receive'] = (df['Sf_Receive'] - df['Err_Receive']) / df['Att_Receive']
df.to_csv('clean_VNL2024Men_Receivers.csv', index=False)
print("✅ 1/7: Receivers - DONE")

# 2. CLEAN ATTACKERS
df = read_csv_fixed('VNL2024Men_Attackers.csv')
df['Efficiency_Attack'] = (df['Pt_Attack'] - df['Err_Attack']) / df['Att_Attack']
df.to_csv('clean_VNL2024Men_Attackers.csv', index=False)
print("✅ 2/7: Attackers - DONE")

# 3. CLEAN SERVERS
df = read_csv_fixed('VNL2024Men_Servers.csv')
df['Efficiency_Serve'] = (df['Pt_Serve'] - df['Err_Serve']) / df['Att_Serve']
df.to_csv('clean_VNL2024Men_Servers.csv', index=False)
print("✅ 3/7: Servers - DONE")

# 4. CLEAN SETTERS
df = read_csv_fixed('VNL2024Men_Setters.csv')
df['Efficiency_Set'] = (df['Sf_Set'] - df['Err_Set']) / df['Att_Set']
df.to_csv('clean_VNL2024Men_Setters.csv', index=False)
print("✅ 4/7: Setters - DONE")

# 5. CLEAN BLOCKERS
df = read_csv_fixed('VNL2024Men_Blockers.csv')
df['Efficiency_Block'] = (df['Pt_Block'] - df['Err_Block']) / df['Tot_Block']
df.to_csv('clean_VNL2024Men_Blockers.csv', index=False)
print("✅ 5/7: Blockers - DONE")

# 6. CLEAN DIGGERS
df = read_csv_fixed('VNL2024Men_Diggers.csv')
df['Efficiency_Dig'] = (df['Sf_Dig'] - df['Err_Dig']) / df['Receptions']
df.to_csv('clean_VNL2024Men_Diggers.csv', index=False)
print("✅ 6/7: Diggers - DONE")

# 7. CLEAN SCORERS (No calculation needed)
df = read_csv_fixed('VNL2024Men_Scorers.csv')
df.to_csv('clean_VNL2024Men_Scorers.csv', index=False)
print("✅ 7/7: Scorers - COPIED")

print("\n🎉 BOOM! CLEANING COMPLETE!")
print("All 7 clean CSV files are ready for PostgreSQL and Power BI.\n")

# ============================================================
# PART 2 – DEBUG EXAMPLE FOR ATTACKERS
# ============================================================

print("🔍 DEBUG MODE ACTIVATED")
print("Checking the VNL2024Men_Attackers.csv file with encoding fix...\n")

# Try reading with multiple encodings
print("--- READING ORIGINAL FILE ---")
try:
    df_original = pd.read_csv('VNL2024Men_Attackers.csv', encoding='utf-8')
    print("Read with UTF-8 encoding")
except UnicodeDecodeError:
    try:
        df_original = pd.read_csv('VNL2024Men_Attackers.csv', encoding='latin-1')
        print("Read with Latin-1 encoding")
    except UnicodeDecodeError:
        df_original = pd.read_csv('VNL2024Men_Attackers.csv', encoding='iso-8859-1')
        print("Read with ISO-8859-1 encoding")

print(f"Number of rows in original file: {len(df_original)}")
print(f"Columns in original file: {df_original.columns.tolist()}\n")

# Cleaning step for Attackers
print("--- CLEANING THE DATA ---")
df_clean = df_original.copy()
df_clean['Efficiency_Attack'] = (df_clean['Pt_Attack'] - df_clean['Err_Attack']) / df_clean['Att_Attack']
print(f"Number of rows in clean data: {len(df_clean)}\n")

# Preview first 5 rows
print("--- FIRST 5 ROWS OF CLEAN DATA ---")
print(df_clean[['Name', 'Team', 'Pt_Attack', 'Err_Attack', 'Att_Attack', 'Efficiency_Attack']].head())
print("")

# Save debug output
df_clean.to_csv('DEBUG_clean_VNL2024Men_Attackers.csv', index=False)
print("💾 Saved debug file: 'DEBUG_clean_VNL2024Men_Attackers.csv'")

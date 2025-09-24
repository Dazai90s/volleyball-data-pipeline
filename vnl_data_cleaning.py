# VNL 2024 Men's Volleyball Data Cleaning
# Reads raw CSVs, fixes encoding, standardizes columns, removes duplicates,
# fills missing values, and calculates efficiency metrics.

import pandas as pd

def read_csv_fixed(filename):
    df = pd.read_csv(filename, encoding='latin-1')
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace(r"[^\w\s]", "", regex=True)
    )
    return df

def clean_dataframe(df):
    df = df.drop_duplicates()
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(0)
    obj_cols = df.select_dtypes(include="object").columns
    df[obj_cols] = df[obj_cols].fillna("Unknown")
    return df

# Receivers
df = read_csv_fixed('VNL2024Men_Receivers.csv')
df = clean_dataframe(df)
df['efficiency_receive'] = (df['sf_receive'] - df['err_receive']) / df['att_receive'].replace(0, 1)
df.to_csv('clean_VNL2024Men_Receivers.csv', index=False)

# Attackers
df = read_csv_fixed('VNL2024Men_Attackers.csv')
df = clean_dataframe(df)
df['efficiency_attack'] = (df['pt_attack'] - df['err_attack']) / df['att_attack'].replace(0, 1)
df.to_csv('clean_VNL2024Men_Attackers.csv', index=False)

# Servers
df = read_csv_fixed('VNL2024Men_Servers.csv')
df = clean_dataframe(df)
df['efficiency_serve'] = (df['pt_serve'] - df['err_serve']) / df['att_serve'].replace(0, 1)
df.to_csv('clean_VNL2024Men_Servers.csv', index=False)

# Setters
df = read_csv_fixed('VNL2024Men_Setters.csv')
df = clean_dataframe(df)
df['efficiency_set'] = (df['sf_set'] - df['err_set']) / df['att_set'].replace(0, 1)
df.to_csv('clean_VNL2024Men_Setters.csv', index=False)

# Blockers
df = read_csv_fixed('VNL2024Men_Blockers.csv')
df = clean_dataframe(df)
df['efficiency_block'] = (df['pt_block'] - df['err_block']) / df['tot_block'].replace(0, 1)
df.to_csv('clean_VNL2024Men_Blockers.csv', index=False)

# Diggers
df = read_csv_fixed('VNL2024Men_Diggers.csv')
df = clean_dataframe(df)
df['efficiency_dig'] = (df['sf_dig'] - df['err_dig']) / df['receptions'].replace(0, 1)
df.to_csv('clean_VNL2024Men_Diggers.csv', index=False)

# Scorers
df = read_csv_fixed('VNL2024Men_Scorers.csv')
df = clean_dataframe(df)
df.to_csv('clean_VNL2024Men_Scorers.csv', index=False)

# Debug example for Attackers
df_original = read_csv_fixed('VNL2024Men_Attackers.csv')
df_clean = clean_dataframe(df_original)
df_clean['efficiency_attack'] = (df_clean['pt_attack'] - df_clean['err_attack']) / df_clean['att_attack'].replace(0, 1)
print(df_clean[['name', 'team', 'pt_attack', 'err_attack', 'att_attack', 'efficiency_attack']].head())
df_clean.to_csv('DEBUG_clean_VNL2024Men_Attackers.csv', index=False)

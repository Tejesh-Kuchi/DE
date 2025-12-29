import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def load_rules(path):
    return pd.read_excel(path)

def save_excel(df, path):
    df.to_excel(path, index=False)

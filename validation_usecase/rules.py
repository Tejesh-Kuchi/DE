import pandas as pd

def validate_row(row):
    errors = []

    if pd.isna(row["order_id"]):
        errors.append("order_id is NULL")

    if pd.isna(row["customer_id"]):
        errors.append("customer_id is NULL")

    if pd.isna(row["net_sales"]) or row["net_sales"] < 0:
        errors.append("net_sales < 0")

    if pd.isna(row["country"]) or str(row["country"]).strip() == "":
        errors.append("country missing")

    return errors

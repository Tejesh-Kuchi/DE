import pandas as pd
from rules import validate_row

def build_clean_dataframe(schema):
    return pd.DataFrame({col: pd.Series(dtype=dtype) for col, dtype in schema.items()})

def validate_data(data, schema):
    clean_df = build_clean_dataframe(schema)
    errors = []

    for index, row in data.iterrows():
        row_errors = validate_row(row)

        if row_errors:
            errors.append({
                "row_number": index + 1,
                "order_id": row.get("order_id"),
                "issues": ", ".join(row_errors)
            })
        else:
            clean_row = {
                "order_id": int(row["order_id"]),
                "customer_id": str(row["customer_id"]),
                "net_sales": float(row["net_sales"]),
                "country": str(row["country"])
            }
            clean_df = pd.concat([clean_df, pd.DataFrame([clean_row])], ignore_index=True)

    return clean_df, pd.DataFrame(errors)

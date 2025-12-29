import pandas as pd

sales_data = pd.read_csv('T:\\validation_usecase.csv')

rules = pd.read_excel(r"T:/validation_rules.xlsx")
print(rules.head())

schema = {
    "order_id": "int64",
    "customer_id": "string",
    "net_sales": "float64",
    "country": "string"
}

clean_df = pd.DataFrame({col: pd.Series(dtype=dtype) for col, dtype in schema.items()})
errors = []
for index, row in sales_data.iterrows():
    row_errors = []

    # Rule 1 & 2 – not null
    if pd.isna(row["order_id"]):
        row_errors.append("order_id is NULL")

    if pd.isna(row["customer_id"]):
        row_errors.append("customer_id is NULL")

    # Rule 3 – net_sales >= 0
    if pd.isna(row["net_sales"]) or row["net_sales"] < 0:
        row_errors.append("net_sales < 0")

    # Rule 4 – country present
    if pd.isna(row["country"]) or str(row["country"]).strip() == "":
        row_errors.append("country missing")

    # If errors exist → log them
    if row_errors:
        errors.append({
            "row_number": index + 1,
            "order_id": row.get("order_id"),
            "issues": ", ".join(row_errors)
        })
    else:
        # Row is clean → cast to schema & insert
        clean_row = {
            "order_id": int(row["order_id"]),
            "customer_id": str(row["customer_id"]),
            "net_sales": float(row["net_sales"]),
            "country": str(row["country"])
        }
        clean_df = pd.concat([clean_df, pd.DataFrame([clean_row])], ignore_index=True)

        clean_df.to_excel("clean_data.xlsx", index=False)

error_df = pd.DataFrame(errors)
error_df.to_excel("data_errors.xlsx", index=False)



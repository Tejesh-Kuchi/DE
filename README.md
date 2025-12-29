Data Validation Project

This project validates raw CSV data using business rules defined in an Excel file and produces two outputs:

1.A clean dataset
2.An error report for invalid records

What this project does

1.Reads a CSV file containing business data
2.Reads an Excel file containing validation rules
3.Applies required checks such as:
4.Not null checks
5.Value checks (e.g., net_sales >= 0)
6.Copies only valid rows into a clean dataset
7.Captures invalid rows with error reasons into a separate file

Input Files
CSV (Raw Data)

Contains columns like:
1.order_id
2.customer_id
3.net_sales
4.country

Excel (Rules)
1.Contains validation rules such as:
2.order_id should not be null
3.customer_id should not be null
4.net_sales should be >= 0
5.country should be present

Output Files
After running the script, two Excel files are generated:
1.clean_data.xlsx
2.Contains only valid rows
3.data_errors.xlsx

Contains row number, order_id and the reason why the record failed

How to Run
1.Install dependencies
2.pip install pandas openpyxl
3.Update file paths in config.py
4.Run
5.python main.py


Check the outputs folder for results

Purpose

This project shows how to:
1.Validate data before loading into databases
2.Enforce business rules
3.Capture bad data instead of silently ignoring it

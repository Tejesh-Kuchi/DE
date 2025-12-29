from io_utils import load_data, load_rules, save_excel
from validator import validate_data
from config import DATA_PATH, RULES_PATH, OUTPUT_CLEAN, OUTPUT_ERRORS, SCHEMA

data = load_data(DATA_PATH)
rules = load_rules(RULES_PATH)

clean_df, error_df = validate_data(data, SCHEMA)

save_excel(clean_df, OUTPUT_CLEAN)
save_excel(error_df, OUTPUT_ERRORS)

print("Pipeline completed.")

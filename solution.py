import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    operations = ["+", "-", "*"]
    pattern = "^[a-zA-Z_]*$"
    # validations
    for col_label in pd.DataFrame.columns:
        if bool(re.match(pattern,col_label)) == False:
            return pd.DataFrame([])
    if 
    return pd.DataFrame([]) 

df = pd.DataFrame([[1, 1]] * 5, columns = ["label_one", "label_two"])

print(df)
import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    operations = ["+", "-", "*"]
    pattern = re.compile(r'^[a-zA-Z_]+$')
    
    # validations
    ### Column labels must consist only of letters and underscores (_).
    ### if the role or any column label is incorrect, the function should return an empty DataFrame.
    role_columns_split = re.split(r'[+*-]', role)

    if not pattern.match(new_column):
        return pd.DataFrame([])
    
    if not all(pattern.match(col) for col in df.columns):
        return pd.DataFrame([])
    
    for col_label in role_columns_split:
        col_label = col_label.strip()
        if col_label and (col_label not in df.columns or not pattern.match(col_label)):
            return pd.DataFrame([])

    ### The function must support basic operations: addition (+), subtraction (-), and multiplication (*).
    if not any(op in role for op in operations):
        return pd.DataFrame([]) 
    
    return df.assign(**{new_column: eval(role, {}, df)})


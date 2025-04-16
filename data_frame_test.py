import pandas as pd

pd.set_option('display.max_colwidth', None)  # Don't cut off long strings
pd.set_option('display.max_columns', None)   # Show all columns
pd.set_option('display.width', 0)            # Let pandas auto-wrap lines
# Load JSONL into DataFrame
df = pd.read_json("courses_202509.jsonl", lines=True)

# Preview the data
print(df['details'])

print(df['description'].head(5))  # Now shows full content



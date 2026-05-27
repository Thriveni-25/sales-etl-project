import pandas as pd

# Load CSV
df = pd.read_csv("datasets/sales_data_sample.csv", encoding='latin1')

# Remove duplicates
df = df.drop_duplicates()

# Remove null values
df = df.dropna()

# Save cleaned file
df.to_csv("datasets/cleaned_sales_data.csv", index=False)

print("Data cleaned successfully")
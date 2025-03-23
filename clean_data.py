
import pandas as pd

# Read CSV with all columns as strings.
df = pd.read_csv('ebay-scraper/ebay_tech_deals.csv', dtype=str)

# Clean 'price' and 'original_price' by removing currency symbols ("US $", "$", ",").
for col in ['price', 'original_price']:
    if col in df.columns:
        df[col] = df[col].str.replace("US $", "", regex=False)
        df[col] = df[col].str.replace("$", "", regex=False)
        df[col] = df[col].str.replace(",", "", regex=False)
        df[col] = df[col].str.strip()

# Replace "N/A" and empty strings in original_price with missing values, then fill missing original_price with price.
df['original_price'] = df['original_price'].replace({"N/A": None, "": None})
df['original_price'] = df['original_price'].fillna(df['price'])

# Clean the shipping column, replacing missing or empty values.
if 'shipping' in df.columns:
    df['shipping'] = df['shipping'].str.strip().replace({"N/A": None, "": None})
    df['shipping'] = df['shipping'].fillna("Shipping info unavailable")

# Convert price columns to numeric.
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['original_price'] = pd.to_numeric(df['original_price'], errors='coerce')

# Calculate discount_percentage and round to 2 decimals.
df['discount_percentage'] = (1 - (df['price'] / df['original_price'])) * 100
df['discount_percentage'] = df['discount_percentage'].round(2).fillna(0)

# Remove invalid or missing titles.
if 'title' in df.columns:
    df['title'] = df['title'].astype(str).str.strip()
    invalid_titles = {"", "N/A", "NAN"}
    df = df[~df['title'].str.upper().isin(invalid_titles)]

# Save cleaned data to CSV.
df.to_csv('cleaned_ebay_deals.csv', index=False)
print("Cleaned data saved to cleaned_ebay_deals.csv")

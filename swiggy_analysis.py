import pandas as pd
import os

# Load dataset
df = pd.read_csv(
    r"C:\Users\ABC\OneDrive\Desktop\swiggy data analyst project\data\raw\swiggy.csv",
    encoding='latin1'
)

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# -----------------------------
# CLEAN RATING
# -----------------------------
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# -----------------------------
# CLEAN NUMBER OF RATINGS
# Example: "10+ ratings" → 10
# -----------------------------
df['number_of_ratings'] = (
    df['number_of_ratings']
    .astype(str)
    .str.extract(r'(\d+)')[0]
)

df['number_of_ratings'] = pd.to_numeric(
    df['number_of_ratings'],
    errors='coerce'
)

# -----------------------------
# CLEAN AVERAGE PRICE
# Example: "₹250 for two" → 250
# -----------------------------
df['average_price'] = (
    df['average_price']
    .astype(str)
    .str.extract(r'(\d+)')[0]
)

df['average_price'] = pd.to_numeric(
    df['average_price'],
    errors='coerce'
)

# -----------------------------
# FILL MISSING VALUES
# -----------------------------
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['number_of_ratings'] = df['number_of_ratings'].fillna(0)
df['average_price'] = df['average_price'].fillna(0)

# -----------------------------
# CREATE PRICE CATEGORY
# -----------------------------
df['price_category'] = pd.cut(
    df['average_price'],
    bins=[0, 200, 500, 2000],
    labels=['Low', 'Medium', 'High']
)

# -----------------------------
# CREATE PROCESSED FOLDER
# -----------------------------
os.makedirs(
    r"C:\Users\ABC\OneDrive\Desktop\swiggy data analyst project\data\processed",
    exist_ok=True
)

# -----------------------------
# SAVE CLEANED FILE
# -----------------------------
df.to_csv(
    r"C:\Users\ABC\OneDrive\Desktop\swiggy data analyst project\data\processed\swiggy_cleaned.csv",
    index=False
)

print("Data cleaned successfully!")
import pandas as pd

# ==========================================
# LEVEL 1 (MVP): Load & Inspect
# ==========================================
print("--- Level 1: Loading and Inspecting Data ---")

# Replace 'data.csv' with your actual file path if needed
# We use a try-except block to handle errors gracefully if the file is missing
try:
    df = pd.read_csv("data.csv")
    print("✔ File loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'data.csv' not found. Creating a dummy file for demonstration.")
    # Creating a sample dataset so the script can run seamlessly
    sample_data = {
        "item": ["Product A", "Product B", "Product C", "Product D", "Product E"],
        "category": ["Electronics", "Clothing", "Electronics", "Home", "Clothing"],
        "val": [1200, 450, 800, 150, 300]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv("data.csv", index=False)
    print("✔ 'data.csv' created with sample data.")

# Inspecting the first few rows (Defaults to 5 rows)
print("\nFirst few rows of the dataset:")
print(df.head())


# ==========================================
# LEVEL 2: Filter & Calculate Statistics
# ==========================================
print("\n--- Level 2: Calculating Core Statistics ---")

# 1. Calculate average and total of the target column ('val')
average_val = df["val"].mean()
total_val = df["val"].sum()

# 2. Find highest and lowest values
max_val = df["val"].max()
min_val = df["val"].min()

print(f"Average Value: {average_val}")
print(f"Total Value:   {total_val}")
print(f"Highest Value: {max_val}")
print(f"Lowest Value:  {min_val}")

# 3. Filter specific rows (Example: filtering for 'Electronics' if category exists)
if "category" in df.columns:
    print("\nFiltering rows where category is 'Electronics':")
    filtered_df = df[df["category"] == "Electronics"]
    print(filtered_df)


# ==========================================
# LEVEL 3 (Challenge): Structured Summary Report
# ==========================================
print("\n--- Level 3: Summary Report ---")

# Gathering structural metadata
total_rows = len(df)
total_columns = len(df.columns)
column_names = list(df.columns)

# Formatting a clean terminal report
report = f"""
==================================================
               CSV ANALYZER REPORT                
==================================================
[Dataset Dimensions]
• Total Records: {total_rows}
• Total Columns: {total_columns}
• Column Names : {', '.join(column_names)}

[Key Metrics for 'val']
• Grand Total  : {total_val}
• Average (Mean): {average_val:.2f}
• Maximum Value: {max_val}
• Minimum Value: {min_val}
==================================================
"""
print(report)
import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 00. TEST DATA GENERATION (For End-to-End Run)
# ==========================================
def generate_sample_data():
    data = {
        'Date': ['2026-01-10', '2026-01-15', '2026-01-20', '2026-02-05', '2026-02-12', '2026-02-25', '2026-03-02'],
        'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Laptop'],
        'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
        'Sales': [1200, 25, 1200, 75, 30, 300, 1200]
    }
    df = pd.DataFrame(data)
    df.to_csv('sales.csv', index=False)
    print("✔ Created sample file 'sales.csv' successfully.\n")

# ==========================================
# MAIN REPORT GENERATION
# ==========================================
def generate_sales_report(file_path):
    print(f"--- Loading Data from {file_path} ---")
    # Load Data
    df = pd.read_csv(file_path)
    
    # Ensure proper data types
    df['Sales'] = pd.to_numeric(df['Sales'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%B') # Extract Month name

    # ------------------------------------------
    # 01. MVP Level: Overall Metrics & Top Product
    # ------------------------------------------
    total_sales = df['Sales'].sum()
    
    # Aggregate sales by product to find the top one
    product_totals = df.groupby('Product')['Sales'].sum()
    top_product = product_totals.idxmax()
    top_product_sales = product_totals.max()

    print("\n[01. MVP RESULTS]")
    print(f"• Total Revenue Generated: ${total_sales:,.2f}")
    print(f"• Best-Selling Product: {top_product} (${top_product_sales:,.2f})")

    # ------------------------------------------
    # 02. Improve Level: Dynamic Grouping (Category & Month)
    # ------------------------------------------
    category_totals = df.groupby('Category')['Sales'].sum().reset_index()
    month_totals = df.groupby('Month')['Sales'].sum().reindex(['January', 'February', 'March']).fillna(0).reset_index()

    print("\n[02. IMPROVE RESULTS]")
    print("\n--- Sales by Category ---")
    print(category_totals.to_string(index=False))
    print("\n--- Sales by Month ---")
    print(month_totals.to_string(index=False))

    # ------------------------------------------
    # 03. Challenge Level: Multi-Chart Visualization
    # ------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Chart 1: Sales by Product (Bar Chart)
    product_totals.sort_values(ascending=False).plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
    axes[0].set_title('Total Sales by Product', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Sales ($)')
    axes[0].set_xlabel('Product')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Chart 2: Sales Distribution by Category (Pie Chart)
    axes[1].pie(category_totals['Sales'], labels=category_totals['Category'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
    axes[1].set_title('Sales Distribution by Category', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig('sales_report_charts.png')
    print("\n[03. CHALLENGE RESULTS]")
    print("✔ Generated 'sales_report_charts.png' containing dual-visual charts.")
    plt.show()

# Execute Script
if __name__ == "__main__":
    generate_sample_data()
    generate_sales_report('sales.csv')
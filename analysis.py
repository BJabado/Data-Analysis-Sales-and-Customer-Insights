import duckdb
import os
import matplotlib.pyplot as plt

# 1. Path Setup: Ensure the script finds files in its own directory
base_path = os.path.dirname(os.path.abspath(__file__))
cust_path = os.path.join(base_path, 'customers (1).csv')
ord_path = os.path.join(base_path, 'orders (1).csv')
prod_path = os.path.join(base_path, 'products (1).csv')

# 2. SQL Queries
# We use the absolute paths defined above to avoid 'File Not Found' errors
query_customers = f"""
    SELECT 
        c.customer_id, 
        SUM(o.quantity * p.price) AS total_spend
    FROM '{cust_path}' AS c
    JOIN '{ord_path}' AS o ON c.customer_id = o.customer_id
    JOIN '{prod_path}' AS p ON o.product_id = p.product_id
    GROUP BY c.customer_id
    ORDER BY total_spend DESC
    LIMIT 5
"""

query_category = f"""
    SELECT 
        p.category, 
        SUM(o.quantity * p.price) AS total_revenue
    FROM '{ord_path}' AS o
    JOIN '{prod_path}' AS p ON o.product_id = p.product_id
    GROUP BY p.category
"""

# 3. Execution
try:
    top_customers = duckdb.sql(query_customers).df()
    category_revenue = duckdb.sql(query_category).df()

    print("--- Top 5 Customers by Spending ---")
    print(top_customers.to_string(index=False))

    print("\n--- Revenue by Category ---")
    print(category_revenue.to_string(index=False))

    # 4. Visualization
    category_revenue.plot(kind='bar', x='category', y='total_revenue', color='skyblue', figsize=(10, 6))
    plt.title('Total Revenue by Product Category')
    plt.xlabel('Category')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
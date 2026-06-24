import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the datasets
customers = pd.read_csv('customers (1).csv')
orders = pd.read_csv('orders (1).csv')
products = pd.read_csv('products (1).csv')

# 2. Merge the data
df = orders.merge(products, on='product_id').merge(customers, on='customer_id')

# 3. Calculate total spend per order
df['total_price'] = df['quantity'] * df['price']

# 4. Basic Analysis: Top 5 customers by total spend
top_customers = df.groupby('customer_id')['total_price'].sum().sort_values(ascending=False).head(5)

print("--- Top 5 Customers by Spending ---")
print(top_customers)

# 5. Basic Analysis: Revenue by Category
category_revenue = df.groupby('category')['total_price'].sum()

print("\n--- Revenue by Category ---")
print(category_revenue)

# 6. Visualization: Bar chart for Revenue by Category
plt.figure(figsize=(10, 6))
category_revenue.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
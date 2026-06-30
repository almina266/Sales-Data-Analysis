import pandas as pd

# Read the CSV file
df = pd.read_csv("data/sales_data.csv")

# Create Total column
df["Total"] = df["Quantity"] * df["Price"]

# Calculate total revenue
total_revenue = df["Total"].sum()

print("Sales Data")
print(df)

print("\nTotal Revenue:", total_revenue)
# Product-wise quantity sold
product_sales = df.groupby("Product")["Quantity"].sum()

print("\nProduct-wise Sales:")
print(product_sales)
# Find the best-selling product
best_product = product_sales.idxmax()
best_quantity = product_sales.max()

print("\nBest Selling Product:", best_product)
print("Units Sold:", best_quantity)
import matplotlib.pyplot as plt

# Create a larger figure
plt.figure(figsize=(8, 5))

# Create bar chart
product_sales.plot(kind="bar")

# Add title and labels
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

# Rotate x-axis labels
plt.xticks(rotation=45)

# Adjust spacing
plt.tight_layout()

# Save the chart
plt.savefig("output/product_sales_chart.png")

# Display the chart
plt.show()
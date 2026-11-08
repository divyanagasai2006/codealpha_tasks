import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Extract month
df["Month"] = df["Date"].dt.strftime("%b")

sns.set_theme(style="whitegrid")

# 1. Product-wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title("Product-wise Sales Analysis")
plt.xlabel("Total Sales (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("product_sales_chart.png")
plt.close()

# 2. Region-wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Region-wise Sales Distribution")
plt.tight_layout()
plt.savefig("region_sales_chart.png")
plt.close()

# 3. Monthly Sales Trend
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total_Sales"].sum()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# 4. Category-wise Sales
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Category-wise Sales Comparison")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_sales_chart.png")
plt.close()

# Display insights
print("\n========== SALES VISUALIZATION INSIGHTS ==========")
print("\nProduct-wise Sales:\n", product_sales)
print("\nRegion-wise Sales:\n", region_sales)
print("\nMonthly Sales:\n", monthly_sales)
print("\nCategory-wise Sales:\n", category_sales)

print("\nAll charts generated successfully!")
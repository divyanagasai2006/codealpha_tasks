
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Research Questions for EDA
print("\n========== RESEARCH QUESTIONS ==========")
print("1. Which product generates the highest total sales?")
print("2. Which region generates the highest total sales?")
print("3. Which month records the highest total sales?")
print("4. Are there any missing values or duplicate records?")
print("5. Are there any unusual values or patterns in the sales data?")
print("6. Does the monthly sales pattern support the assumption that sales remain stable?")

# 1. Load the dataset
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 2. Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# 3. Display basic information
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe())

# 4. Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 5. Check duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())
# 5.1 Check invalid values
print("\n========== INVALID VALUES ==========")

print("Invalid Quantity values:", (df["Quantity"] <= 0).sum())
print("Invalid Unit Price values:", (df["Unit_Price"] <= 0).sum())
print("Invalid Dates:", pd.to_datetime(df["Date"], errors="coerce").isna().sum())
print("Invalid Product values:", df["Product"].isna().sum())
print("Invalid Region values:", df["Region"].isna().sum())

# 5.2 Detect unusually high or low sales values using IQR
print("\n========== SALES ANOMALY CHECK ==========")

Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

unusual_sales = df[
    (df["Total_Sales"] < lower_bound) |
    (df["Total_Sales"] > upper_bound)
]

print(f"Lower threshold: Rs. {lower_bound:,.2f}")
print(f"Upper threshold: Rs. {upper_bound:,.2f}")

if unusual_sales.empty:
    print("No unusual sales values detected using the IQR method.")
else:
    print("Unusual sales records detected:")
    print(unusual_sales[["Order_ID", "Product", "Total_Sales"]])

# 6. Sales by product
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(
    ascending=False
)
print("\n========== SALES BY PRODUCT ==========")
print(product_sales)

# 7. Sales by region
region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(
    ascending=False
)
print("\n========== SALES BY REGION ==========")
print(region_sales)

# 8. Monthly sales analysis

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Total_Sales"].sum()
# 8.2 Validate the monthly sales hypothesis
print("\n========== HYPOTHESIS VALIDATION ==========")

average_monthly_sales = monthly_sales.mean()
sales_difference = monthly_sales.max() - monthly_sales.min()

print(f"Average monthly sales: Rs. {average_monthly_sales:,.2f}")
print(f"Difference between highest and lowest month: Rs. {sales_difference:,.2f}")

if monthly_sales.nunique() == 1:
    print("Result: Monthly sales are equal in all months.")
else:
    print("Result: Monthly sales vary across the observed months.")

print("Conclusion: The assumption that monthly sales remain exactly stable is not supported by this dataset.")

# 8.1 Identify sales trends and patterns
print("\n========== SALES TRENDS AND PATTERNS ==========")

highest_product = product_sales.idxmax()
print(f"Highest sales product: {highest_product} (Rs. {product_sales.max():,.2f})")

highest_region = region_sales.idxmax()
print(f"Highest sales region: {highest_region} (Rs. {region_sales.max():,.2f})")

highest_month = monthly_sales.idxmax()
print(f"Highest sales month: {highest_month} (Rs. {monthly_sales.max():,.2f})")

lowest_month = monthly_sales.idxmin()
print(f"Lowest sales month: {lowest_month} (Rs. {monthly_sales.min():,.2f})")

print(f"Total revenue: Rs. {df['Total_Sales'].sum():,.2f}")


print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# 9. Save analysis results
product_sales.to_csv("product_sales.csv", header=["Total_Sales"])
region_sales.to_csv("region_sales.csv", header=["Total_Sales"])
monthly_sales.to_csv("monthly_sales.csv", header=["Total_Sales"])

# 10. Visualize sales by product
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (INR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()

# 11. Visualize sales by region
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales (INR)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# 12. Visualize monthly sales trend
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (INR)")
plt.xticks(rotation=30)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

print("\nEDA completed successfully!")
print("Results and charts have been saved in the project folder.")

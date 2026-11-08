# Exploratory Data Analysis (EDA) - Sales Data

## Project Overview
This project performs Exploratory Data Analysis (EDA) on a sample retail sales dataset using Python. It analyzes sales performance across products, regions, and months to identify trends, patterns, and unusual sales records.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

## Dataset
The dataset contains 20 sample retail sales records with the following columns:
- Order_ID
- Date
- Product
- Category
- Quantity
- Unit_Price
- Region

## Research Questions
1. Which product generates the highest total sales?
2. Which region generates the highest total sales?
3. Which month records the highest total sales?
4. Are there any missing values or duplicate records?
5. Are there any unusual values or patterns in the sales data?
6. Do monthly sales remain stable across the observed months?

## Analysis Performed
- Dataset structure and summary statistics
- Missing value and duplicate record checks
- Invalid quantity, unit price, date, product, and region checks
- Product-wise sales analysis
- Region-wise sales analysis
- Monthly sales analysis
- IQR-based detection of unusual sales values
- Monthly sales hypothesis validation using descriptive statistics
- Sales visualizations and CSV summary exports

## Key Findings
- Total sales revenue: INR 574,500
- Highest revenue product: Laptop (INR 330,000)
- Highest revenue region: South (INR 234,000)
- Highest sales month: May 2026 (INR 145,900)
- Lowest sales month: April 2026 (INR 92,000)
- Average monthly sales: INR 114,900
- Missing values: 0
- Duplicate rows: 0
- Invalid quantities, prices, dates, products, and regions: 0
- Two Laptop sales records were flagged by the IQR method as unusual values requiring review.

## Hypothesis Validation
The assumption that monthly sales remain exactly stable was not supported by the observed data. Monthly sales ranged from INR 92,000 in April 2026 to INR 145,900 in May 2026.

This is a descriptive comparison of the five observed months, not a formal statistical significance test.

## Generated Outputs
- `product_sales.csv` - Product-wise sales summary
- `region_sales.csv` - Region-wise sales summary
- `monthly_sales.csv` - Monthly sales summary
- `sales_by_product.png` - Product sales chart
- `sales_by_region.png` - Region sales chart
- `monthly_sales_trend.png` - Monthly sales trend chart

## How to Run
1. Install Python.
2. Install the required libraries:

   `python -m pip install pandas matplotlib seaborn`

3. Run the analysis:

   `python eda_analysis.py`

## Note
The dataset is created for educational and demonstration purposes.

## Author
Divya
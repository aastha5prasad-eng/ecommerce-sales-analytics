import pandas as pd

# Load the dataset
df = pd.read_csv("data/global_ecommerce_sales-selected-columns.csv")
# Display basic information
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

print("\nTotal Sales:")
print(df["Total_Sales"].sum())

print("\nAverage Order Value:")
print(df["Total_Sales"].mean())
# Sales by Product Category
category_sales = df.groupby("Product_Category")["Total_Sales"].sum().sort_values(ascending=False)

print("\nSales by Product Category:")
print(category_sales)
# Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)

print("\nSales by Region:")
print(region_sales)
# Top 10 Products by Sales
product_sales = (
    df.groupby("Product_Name")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(product_sales)
# Sales by Customer Segment
segment_sales = (
    df.groupby("Customer_Segment")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Customer Segment:")
print(segment_sales)
# Monthly Sales Trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)
# Sales by Country
country_sales = (
    df.groupby("Country")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Country:")
print(country_sales)
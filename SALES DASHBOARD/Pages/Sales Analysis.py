# SALES DATA VISUALIZATION

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("sales.xls")

# -----------------------------------
# 1. CATEGORY-WISE SALES BAR CHART
# -----------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()


# -----------------------------------
# 2. CATEGORY-WISE PROFIT BAR CHART
# -----------------------------------

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind='bar')

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.show()


# -----------------------------------
# 3. SALES TREND LINE CHART
# -----------------------------------

# Convert Order Date into datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly Sales
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,5))
monthly_sales.plot(kind='line')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# -----------------------------------
# 4. PROFIT TREND LINE CHART
# -----------------------------------

monthly_profit = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Profit"].sum()

monthly_profit.index = monthly_profit.index.astype(str)

plt.figure(figsize=(12,5))
monthly_profit.plot(kind='line')

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.show()


# -----------------------------------
# 5. CATEGORY SALES PIE CHART
# -----------------------------------

plt.figure(figsize=(7,7))

category_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Sales Distribution by Category")
plt.ylabel("")

plt.show()


# -----------------------------------
# 6. TOP 10 PRODUCTS BY SALES
# -----------------------------------

top_products = df.groupby("Product Name")["Sales"] \
                 .sum() \
                 .sort_values(ascending=False) \
                 .head(10)

plt.figure(figsize=(12,6))
top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()


# -----------------------------------
# 7. REGION-WISE SALES
# -----------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()


# -----------------------------------
# 8. DISCOUNT VS PROFIT SCATTER PLOT
# -----------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    df["Discount"],
    df["Profit"]
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.show()
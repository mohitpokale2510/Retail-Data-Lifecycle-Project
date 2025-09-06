import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Retail.csv")

print("Most sold products:\n", df['Product'].value_counts())
print("\nTotal sales per product:\n", df.groupby('Product')['Total'].sum())
print("\nAverage price per product:\n", df.groupby('Product')['Price'].mean())

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Product', order=df['Product'].value_counts().index)
plt.title("Most Sold Products")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Product', y='Total', estimator=sum, order=df.groupby('Product')['Total'].sum().sort_values(ascending=False).index)
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.show()

df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Total'].sum().reset_index()
plt.figure(figsize=(8,5))
sns.lineplot(data=daily_sales, x='Date', y='Total')
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Quantity', y='Total', hue='Product')
plt.title("Quantity vs Total Sales")
plt.show()

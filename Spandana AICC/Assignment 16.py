# Install these packages if you haven't already
# pip install matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt

# 1. Prepare the dataset
data = {
    "Product": ["A", "B", "C", "D"],
    "January": [50, 30, 20, 40],
    "February": [60, 40, 25, 35],
    "March": [55, 35, 30, 45],
    "April": [70, 45, 20, 50]
}

df = pd.DataFrame(data)
df.set_index("Product", inplace=True)

# 2. Bar Chart - total sales per product
total_sales = df.sum(axis=1)
plt.figure(figsize=(6,4))
total_sales.plot(kind='bar', color=['skyblue', 'orange', 'green', 'red'])
plt.title("Total Sales by Product (Jan–Apr)")
plt.ylabel("Units Sold")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# 3. Pie Chart - proportion of total sales
plt.figure(figsize=(6,6))
total_sales.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'orange', 'green', 'red'])
plt.title("Sales Proportion by Product")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# 4. Histogram - distribution of all sales numbers
all_sales = df.values.flatten()
plt.figure(figsize=(6,4))
plt.hist(all_sales, bins=[20, 30, 40, 50, 60, 70, 80], color='purple', edgecolor='black')
plt.title("Distribution of Monthly Sales")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# 5. Print Data Story
story = """
Over the first four months, Product A was the clear leader in sales, consistently outperforming others.
Product D steadily increased, showing potential growth. Product B had moderate sales, while Product C remained low and inconsistent.
Most sales fell between 30–50 units per month, highlighting a common performance range, but Product A’s peak of 70 units shows potential for higher demand.
"""
print(story)
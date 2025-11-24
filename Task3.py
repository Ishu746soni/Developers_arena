import pandas as pd
data={"product":["Laptop", "Headphones", "Keyboard", "Mouse", "Laptop", "Keyboard"],
      "price":[50000, 1500, 800, 400, 50000, 800],
      "quantity":[5, 20, 10, 15, 3, 5]}

df=pd.DataFrame(data)

#1.Total Sales for each row
df["total_Sales"] = df["price"] * df["quantity"]

#2.Total Sales
total_sales=df["total_Sales"].sum()

#3.Best-Selling product
best_selling=df.groupby("product")["total_Sales"].sum().idxmax()
best_selling_sales=df.groupby("product")["total_Sales"].sum().max()

#4.Generate report
print("-------Sales Data Analysis------")
print("DataFrame:")
print(df)
print("Total Sales Amount:",total_sales)

print("Sales by product:")
print(df.groupby("product")["total_Sales"].sum())

print(f"Best selling product:{best_selling}(Rs.{best_selling_sales})")
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Sales_data.csv")

#DAILY REVENUE TREND
'''daily_revenue=df.groupby("date")["money"].sum().reset_index()
plt.plot(daily_revenue["date"], daily_revenue["money"], marker="o")
plt.xlabel("Date")
plt.ylabel("Daily Revenue")
plt.title("Daily Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''

#Top 10 Most Popular Coffees (By Count)
'''popular_coffee=df["coffee_name"].value_counts().reset_index()
popular_coffee.columns=['coffee_name','counts']
top_10=popular_coffee
plt.bar(top_10['coffee_name'], top_10['counts'])
plt.xlabel("Coffee Name")
plt.ylabel("Number of Orders")
plt.title("Top 10 Most Popular Coffees (By Count)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''

#Revenue by Coffee Name
'''revenue=df.groupby("coffee_name")["money"].sum().reset_index()
plt.plot(revenue["coffee_name"], revenue["money"], marker="o")
plt.xlabel("coffee_name")
plt.ylabel("Revenue")
plt.title("Revenue by Coffee Name")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''

#Payment Method Percentage Comparison
'''payment_counts=df["cash_type"].value_counts()
payment_percentage=(payment_counts / payment_counts.sum()) * 100
plt.pie(payment_percentage,labels=payment_percentage.index,autopct='%1.1f%%')
plt.title("Payment Method Percentage Comparison")
plt.show()'''

#Sales by Month
'''df["datetime"]=pd.to_datetime(df["datetime"])
df["month"]=df["datetime"].dt.month_name()
df["month_num"]=df["datetime"].dt.month
monthly_sales=df.groupby(["month","month_num"])["money"].sum().reset_index()
monthly_sales=monthly_sales.sort_values("month_num")

plt.plot(monthly_sales["month"], monthly_sales["money"], marker="o")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Sales by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''

#Peak Sales Heatmap (Hour vs Day)
df["datetime"]=pd.to_datetime(df["datetime"])
df["hour"]=df["datetime"].dt.hour
df["day"]=df["datetime"].dt.day_name()

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df["day"] = pd.Categorical(df["day"], categories=day_order, ordered=True)

heatmap_data = df.groupby(["day", "hour"])["money"].sum().unstack()

plt.imshow(heatmap_data)
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")
plt.title("Peak Sales Heatmap")
plt.xticks(range(len(heatmap_data.columns)),heatmap_data.columns, rotation=45)
plt.yticks(range(len(heatmap_data.index)),heatmap_data.index)
plt.tight_layout()
plt.colorbar(label="Total Sales")
plt.show()


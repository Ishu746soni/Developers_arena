import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Task5 import heatmap_data

df=pd.read_csv("Sales_data.csv")

#Monthly revenue trend
'''df["datetime"]=pd.to_datetime(df["datetime"])
df["month"]=df["datetime"].dt.month
df["month_name"]=df["datetime"].dt.month_name()
Monthly_sales=df.groupby(["month","month_name"])["money"].sum().reset_index()
Monthly_sales=Monthly_sales.sort_values("month")

sns.lineplot(data=Monthly_sales,x="month_name",y="money",marker="o")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.title("Monthly revenue trend")
plt.tight_layout()
plt.show()'''

#Peak sales Heatmap
'''df["datetime"]=pd.to_datetime(df["datetime"])
df["hour"]=df["datetime"].dt.hour
df["day"]=df["datetime"].dt.day_name()

heatmap_data=pd.pivot_table(
    values="money",
    index="day",
    columns="hour",
    aggfunc="sum"
)

Day_order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
heatmap_data=heatmap_data.reindex(Day_order)

sns.heatmap(heatmap_data,cmap="YlOrRd",annot=True,fmt=".0f")
plt.title("Peak Sales Heatmap (Hour vs Day)")
plt.xlabel("Hour of the Day")
plt.ylabel("Day of the Week")
plt.tight_layout()
plt.show()'''

#Distribution by Coffee Type
'''sns.boxplot(x="coffee_name",y="money", data=df)
plt.xlabel("Coffee_name")
plt.ylabel("Amount")
plt.title("Spending Distribution by Coffee Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''


#Cash vs Card Spending Pattern
'''df["payment_method"] = df["cash_type"].fillna(df["card"])

plt.figure(figsize=(8,5))
sns.violinplot(x="payment_method", y="money", data=df)
plt.xlabel("Payment Method")
plt.ylabel("Amount Spent")
plt.title("Cash vs Card Spending Pattern")
plt.tight_layout()
plt.show()'''

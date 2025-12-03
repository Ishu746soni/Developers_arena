import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("globalAirQuality.csv")
df=df.drop_duplicates()
df=df.dropna()
df.to_csv("cleaned_globalAirQuality.csv",index=False)
print("Cleaning complete")

# Bar chart
plt.bar(df["country"],df["temperature"])
plt.title("Country vs Temperature")
plt.xlabel("Country")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.show()

#Line chart
df=df.sort_values(by="latitude")
plt.plot(df["country"],df["latitude"],label="Latitude")
plt.plot(df["country"],df["longitude"],label="Longitude")
plt.xlabel("Country")
plt.ylabel("Coordinates")
plt.title("Country vs Latitude/Longitude")
plt.xticks(rotation=45)
plt.legend()
plt.show()

#Scatter chart
city_means = df.groupby("city")[["aqi", "latitude", "longitude"]].mean().reset_index()
plt.scatter(
    city_means["longitude"],
    city_means["latitude"],
    s=city_means["aqi"],
    alpha=0.6
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("City-wise Mean AQI Scatter Plot (Bubble Size = AQI)")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./csv_files/Iris.csv")
features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
print(df.shape )
print(df.columns )
print(df.head() )
print(df.tail() )
df.info()
print(df.isnull().sum().sum())

df = df.drop(columns = 'Id') # The Id does nothing, and I want to be able to ascertain true duplicates
print(df.duplicated().sum())
df.drop_duplicates()
print(df)
# From the information I've received above, there are no null values, no duplicate values and no inappropriate datatypes so it is only nothing I had to clean

corr = df[features].corr()
print(corr.round(2))

""" From the observation above
1) SepalLengthCm and SepalWidthCm are weakly negatively correlated
2) PetalLengthCm and PetalWidthCm are strongly positively correlated
3) SepalLengthCm and PetalLengthCm are strongly positively correlated
4) SepalLengthCm and PetalWidthCm are strongly positively correlated
5) SepalWidthCm and PetalLengthCm are moderately negatively correlated
6) SepalWidthCm and PetalWidthCm are weakly negatively correlated"""

# Histogram
df[features].hist(bins=18)
plt.suptitle("Feature distributions")
plt.show()

# Scatter Plot
df.plot(kind='scatter', x='SepalLengthCm', y='PetalWidthCm')
plt.title("Sepal length vs. Petal width")
plt.show()

df.plot(kind='scatter', x='PetalLengthCm', y='SepalWidthCm')
plt.title("Petal length vs. Sepal width")
plt.show()

df.groupby('Species')[features].mean()\
 .plot(kind='bar')
plt.show()

# Summary stats per species
print(df.groupby("Species")[features].agg(["mean", "std"]).round(2))

# Overall summary statistics
print(df.describe())
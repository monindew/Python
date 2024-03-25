import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./recent-grads.csv")
# print(df.head)

# df.plot(x="Rank", y=["P25th", "Median", "P75th"])
# df['Median'].plot(kind="hist", bins = 20) # or df['Median'].hist()
# df.loc[0:4].plot(x="Major", y="Median", kind = "bar", rot=5, fontsize=5)
# df.plot(x="Median", y="ShareWomen", kind="scatter")
# print(df.loc[:,['Median', 'ShareWomen']].corr(method='pearson'))
grouped_df = df.groupby("Major_category")["Total"].sum().sort_values()
grouped_df.plot(kind="barh", fontsize=4)
plt.show()


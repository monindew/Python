import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#1
df = pd.read_csv("./recent-grads.csv")

#2
sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='Malgun Gothic', font_scale=1, rc={"axes.unicode_minus":False})
f, ax = plt.subplots(figsize=(8,4))
gs = f.add_gridspec(1,3)

#3
# ax = f.add_subplot(gs[0,0])
# sns.boxplot(df["Median"])
# ax = f.add_subplot(gs[0,1])
# sns.boxenplot(df["Median"])
# ax = f.add_subplot(gs[0,2])
# sns.violinplot(df["Median"])
# f.tight_layout()

sns.countplot(x="Major_category", data=df).set(ylim=(0,40)).set(xlabel="", ylabel="")
# sns.jointplot(x=df["ShareWomen"], y=df["Median"], kind='kde', xlim=(-0.2, 1.2), ylim=(0,80000))


# sns.pairplot(df)
# df_tips = sns.load_dataset('tips')
# sns.violinplot(x="day", y="total_bill", data=df_tips, hue="smoker", split=True)

# sns.heatmap(df_tips.pivot(index='time',columns=['day'],values=['tip']))
#5
plt.show()
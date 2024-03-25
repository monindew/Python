import pandas as pd

df = pd.read_csv('patient.csv')

print(df.head())

missing_values_cnt = df.isnull().sum()
print(missing_values_cnt)

cleaned_df = df.dropna()
print(cleaned_df)

filled_df = df.fillna(0)
print(filled_df)

bfilled_df = df.fillna(method='bfill', axis=0)
print(bfilled_df)

# df["Blood_Pressure"].fillna(df["Blood_Pressure"].mean(), inplace=True)
# print(df)
print(df)
print(df.interpolate())

filled_df['Blood_Pressure'].replace(0,70, inplace=True)
print(filled_df)

for x in df.index : 
    if df.loc[x, "Max_Blood_Pressure"] > 150:
        df.drop(x, inplace=True)
print(df)

print(df.duplicated())
print(df["Patient_ID"].duplicated())
print(df["Patient_ID"].duplicated().sum())

df.drop_duplicates(subset='Patient_ID', inplace=True)
print(df)
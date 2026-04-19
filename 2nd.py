import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Telco-Customer-Churn.csv")
pd.set_option('display.max_columns', None)
print(df.head())
print(df.info())
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True) * 100)
print(df.groupby("Contract")["Churn"].value_counts(normalize=True)*100)
print(df.groupby("Churn")["tenure"].mean())
print(df.groupby("Churn")["MonthlyCharges"].mean())



df.groupby("Contract")["Churn"].value_counts().unstack().plot(kind="bar")
plt.title("Churn by Contract Type")
plt.show()
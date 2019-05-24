import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_main = pd.read_csv('data.csv')
# print(df['Name'])

df = df_main.copy()

young_good = df[(df['Age']<25) & (df['Overall']>=85)]
young_bad = df[(df['Age']<25) & (df['Overall']<85)]
old_good = df[(df['Age']>=25) & (df['Overall']>=85)]
old_bad = df[(df['Age']>=25) & (df['Overall']<85)]

plt.scatter(young_good['Age'], young_good['Overall'], c='red')
plt.scatter(young_bad['Age'], young_bad['Overall'], c='blue')
plt.scatter(old_good['Age'], old_good['Overall'], c='yellow')
plt.scatter(old_bad['Age'], old_bad['Overall'], c='green')
plt.grid(True)
plt.legend(['Young_Good', 'Young_Bad', 'Old_Good','Old_Bad'])

plt.show()
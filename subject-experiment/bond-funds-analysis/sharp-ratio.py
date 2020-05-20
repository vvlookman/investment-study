import pandas as pd
import numpy as np

df = pd.read_csv('ac-worth-from-2017/002138.csv')
df['daily_return'] = df['worth'].pct_change()

days = df['date'].count()
sharp_ratio = np.sqrt( days / 3.347 ) * df['daily_return'].mean() / df['daily_return'].std()
print(days, sharp_ratio)
import pandas as pd
import numpy as np

df = pd.read_csv('ac-worth-from-2017/002138.csv')
df['daily_return'] = df['worth'].pct_change()

days = df['date'].count()
return_days = days / 3.347
sharp_ratio = ( return_days * df['daily_return'].mean() - 0.03) / ( df['daily_return'].std() * np.sqrt(return_days) )
print(days, sharp_ratio)
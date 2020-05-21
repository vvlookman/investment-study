import pandas as pd
import empyrical as emp

df = pd.read_csv('ac-worth-from-2017/002138.csv')
df['daily_return'] = df['worth'].pct_change()

days = df['date'].count()
return_days = days / 3.347
risk_free = 0.03/return_days

annual_return = emp.annual_return(df['daily_return'], annualization=return_days)
max_drawdown = emp.max_drawdown(df['daily_return'])
sharpe_ratio = emp.sharpe_ratio(df['daily_return'], risk_free, annualization=return_days)
sortino_ratio = emp.sortino_ratio(df['daily_return'], risk_free, annualization=return_days)
omega_ratio = emp.omega_ratio(df['daily_return'], risk_free, annualization=return_days)
print(annual_return, max_drawdown, sharpe_ratio, sortino_ratio, omega_ratio)
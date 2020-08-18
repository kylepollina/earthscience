"""
Get date with the maximum temperature
"""

import pandas as pd
c = pd.read_csv('data/climate.csv')
c.info()
max_temp = c['Temperature_C'].max()
print(max_temp)
print(c[c['Temperature_C'] == max_temp])
print(c[c['Temperature_C'] == max_temp]['Date'])

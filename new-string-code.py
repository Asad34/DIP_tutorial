import pandas as pd
import numpy as np

df = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv', low_memory=False)
df['LATITUDE'] = df['LATITUDE'].astype(str)
df['LONGITUDE'] = df['LONGITUDE'].astype(str)
df = df[['CRASH DATE', 'LATITUDE', 'LONGITUDE']]

# Dropping the last 1700099 rows because file was not loading, making a lot of mess
num_rows = df.shape[0]
df = df.drop(index=range(num_rows-1700099, num_rows))
df.replace('nan', np.nan, inplace=True)
df.dropna(axis=0, how='any', inplace=True)
df.to_csv("a-current_situation_3.csv", index=False)

days = df['CRASH DATE'].str.extract(r'(\d{1,2})/\d{1,2}/\d{4}')
lat = df['LATITUDE'].astype(str).str.extract(r'\d{2}(\.\d{4})')
long = df['LONGITUDE'].astype(str).str.extract(r'-\d{2}(\.\d{4})')

# Concatenating day, lat, and long
answer = pd.concat([days, lat, long], axis=1)
answer = answer.apply(lambda x: ''.join(x.dropna().astype(str)), axis=1)
df['new-string'] = answer
df.to_csv('aa-new-aa.csv', index=False)

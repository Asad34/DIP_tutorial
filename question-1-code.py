import pandas as pd

df = pd.read_csv('diabetes.csv')
df['DiabetesPedigreeFunction'] = df['DiabetesPedigreeFunction'].apply(lambda x: x * 10)
df.to_csv('diabetes_new.csv', index=False)
total = df['DiabetesPedigreeFunction'].reduce(lambda x, y: x + y)
print(total)

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('diabetes.csv')
# histogram of the Age column
plt.hist(df['Age'])
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.title('Histogram of Age')
plt.show()
# line graph of the BloodPressure column
plt.plot(df['BloodPressure'])
plt.xlabel('Index')
plt.ylabel('Blood Pressure')
plt.title('Line Graph of Blood Pressure')
plt.show()

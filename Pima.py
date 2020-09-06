import pandas
import matplotlib.pylab as plt
plt.style.use('seaborn')

dataframe = pandas.read_csv('https://modcom.co.ke/bigdata/datasets/pima.csv')
print(dataframe)

print(dataframe.describe())

print(dataframe.corr())

print(dataframe.groupby('Outcome').size())

print(dataframe.groupby('Outcome').mean())

print(dataframe.groupby('Outcome').describe())

# Graph plots
# Pie Chart
x, y = plt.subplots()
dataframe.groupby('Outcome').size().plot(kind='pie', autopct='%2.2f%%', explode=(0.01, 0.01))
plt.title('Pie chart showing oucome distribution')
plt.savefig('fig10.png')

# Bar Chart
x, y = plt.subplots()
dataframe.groupby('Outcome')['Glucose'].mean().plot(kind='bar')
plt.title('Graph showing average glucose per outcome')
plt.xlabel('Outcome')
plt.ylabel('Glucose')
plt.savefig('fig11.png')

# Line plots
x, y = plt.subplots()
y.plot(dataframe['Glucose'], lw=1, color='blue', label='Glucose')
y.plot(dataframe['DiabetesPedigreeFunction'], color='Red', lw=1, label='DiabetesPedigreeFunction')
plt.xlabel('Frequency')
plt.legend(loc='best')
plt.savefig('fig12.png')



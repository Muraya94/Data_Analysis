import pandas
import matplotlib.pylab as plt

dataframe = pandas.read_csv('https://modcom.co.ke/bigdata/datasets/Advertising.csv')
print(dataframe)

subset = dataframe[(['TV', 'Radio', 'Newspaper', 'Sales'])]
print(subset)

print(subset.describe())

print(subset.corr())

# Graph plots
plt.style.use('seaborn')
# Line plots
x, y = plt.subplots()
y.plot(subset['TV'], lw=1, color='red', label='TV')
y.plot(subset['Radio'], lw=1, color='blue', label='Radio')
y.plot(subset['Newspaper'], lw=1, color='green', label='Newspaper')
plt.xlabel('No.')
plt.ylabel('Advertising costs')
plt.legend(loc='best')
plt.savefig('fig13.png')

# Scatter plot
x, y = plt.subplots()
y.scatter(subset['TV'], subset['Sales'], color='blue')
plt.title('Relationship Between TV Advertising Costs and Sales')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.savefig('fig14.png')

x, y = plt.subplots()
y.scatter(subset['Radio'], subset['Sales'], color='blue')
plt.title('Relationship Between Radio Advertising Costs and Sales')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.savefig('fig15.png')

x, y = plt.subplots()
y.scatter(subset['Newspaper'], subset['Sales'], color='blue')
plt.title('Relationship Between Newspaper Advertising Costs and Sales')
plt.xlabel('Newspaper')
plt.ylabel('Sales')
plt.savefig('fig16.png')


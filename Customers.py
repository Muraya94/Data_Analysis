import pandas
import matplotlib.pylab as plt

pandas.set_option('display.max_columns', 7)
dataframe = pandas.read_csv('https://modcom.co.ke/bigdata/datasets/Customers.csv')
print(dataframe)

subset = dataframe[(['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent'])]
print(subset)

print(subset.describe())

print(subset.corr())

# Graph plots
plt.style.use('seaborn')
# Line plots
x, y = plt.subplots()
y.plot(subset['Avg. Session Length'], lw=1, color='Red', label='Avg. Session Length')
y.plot(subset['Time on App'], lw=1, color='blue', label='Time on App')
y.plot(subset['Time on Website'], lw=1, color='green', label='Time on Website')
y.plot(subset['Length of Membership'], lw=1, color='black', label='Length of Membership')
plt.legend(loc='best')
plt.ylabel('')
plt.xlabel('No.')
plt.savefig('fig17.png')

# Scatter plot
x, y = plt.subplots()
y.scatter(subset['Avg. Session Length'], subset['Yearly Amount Spent'], color='blue')
plt.title('Relationship between Avg. Session Length and Yearly Amount Spent')
plt.xlabel('Avg. Session Length')
plt.ylabel('Yearly Amount Spent')
plt.savefig('fig18.png')

x, y = plt.subplots()
y.scatter(subset['Time on App'], subset['Yearly Amount Spent'], color='blue')
plt.title('Relationship between Time on App and Yearly Amount Spent')
plt.xlabel('Time on App')
plt.ylabel('Yearly Amount Spent')
plt.savefig('fig19.png')

x, y = plt.subplots()
y.scatter(subset['Time on Website'], subset['Yearly Amount Spent'], color='blue')
plt.title('Relationship between Time on Website and Yearly Amount Spent')
plt.xlabel('Time on Website')
plt.ylabel('Yearly Amount Spent')
plt.savefig('fig20.png')

x, y = plt.subplots()
y.scatter(subset['Length of Membership'], subset['Yearly Amount Spent'], color='blue')
plt.title('Relationship between Length of Membership and Yearly Amount Spent')
plt.xlabel('Length of Membership')
plt.ylabel('Yearly Amount Spent')
plt.savefig('fig21.png')

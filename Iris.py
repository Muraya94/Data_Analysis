import pandas
import matplotlib.pylab as plt

# Display all rows
pandas.set_option('display.max_rows', 151)
dataframe = pandas.read_csv('https://modcom.co.ke/bigdata/datasets/iris.csv')
print(dataframe)
# Get more information about the dataset
print(dataframe.describe())
# See how the different columns relate to each other
print(dataframe.corr())
# Show the number of flowers in each of the three classes
print(dataframe.groupby('class').size())
# Compute the averages of each of the columns according to their class
print(dataframe.groupby('class').mean())

print(dataframe.groupby('class').describe())

print(plt.style.available)
plt.style.use('seaborn')

# Graph Plots
# Histogram
x, y = plt.subplots()
y.hist(dataframe['petallength'], color='blue')
plt.title('Distribution of Petal Length')
plt.xlabel('Petallength')
plt.ylabel('Frequency')
# Saving the graph
plt.savefig('fig1.png')

x, y = plt.subplots()
y.hist(dataframe['sepallength'], color='blue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepallength')
plt.ylabel('Frequency')
# Saving the graph
plt.savefig('fig2.png')

x, y = plt.subplots()
y.hist(dataframe['sepalwidth'], color='blue')
plt.title('Distribution of Sepal width')
plt.xlabel('Sepalwidth')
plt.ylabel('Frequency')
# Saving the graph
plt.savefig('fig3.png')

x, y = plt.subplots()
y.hist(dataframe['petalwidth'], color='blue')
plt.title('Distribution of Petal width')
plt.xlabel('Petalwidth')
plt.ylabel('Frequency')
# Saving the graph
plt.savefig('fig4.png')

# Scatter Plot
x, y = plt.subplots()
y.scatter(dataframe['sepallength'], dataframe['petalwidth'], color='blue')
plt.title('Relationship between sepallength and petalwidth')
plt.xlabel('sepallength')
plt.ylabel('petalwidth')
# Saving the graph
plt.savefig('fig5.png')

# Pie Chart
x, y = plt.subplots()
dataframe.groupby('class').size().plot(kind='pie', autopct='%1.1f%%', explode=(0.01, 0.01, 0.01))
plt.title('Pie chart for the flower classes')
# Saving the graph
plt.savefig('fig6.png')

# Bar Chart
x, y = plt.subplots()
dataframe.groupby('class')['petallength'].mean().plot(kind='bar', color='blue')
plt.title('Mean petallength for the flower classes')
plt.xlabel('Class')
plt.ylabel('petallength')
# Saving the graph
plt.savefig('fig7.png')

x, y = plt.subplots()
dataframe.groupby('class')['sepallength'].mean().plot(kind='bar', color='blue')
plt.title('Mean Sepallength for the flower classes')
plt.xlabel('Class')
plt.ylabel('sepallength')
# Saving the graph
plt.savefig('fig8.png')

# Line plots, scatter, density
x, y = plt.subplots()
y.plot(dataframe['petalwidth'], color='orange', lw=2, label='P-widths')
y.plot(dataframe['petallength'], color='red', lw=2, label='P-lengths')
plt.title('')
plt.xlabel('Frequency')
plt.ylabel('cm')
plt.legend(loc='best')
plt.savefig("fig9.png")


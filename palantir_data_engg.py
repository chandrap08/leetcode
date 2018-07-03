# @Author: Chandra Pandey
# @Email: pandey.chandra@gmail.com
#Q2. Which geography contained the smallest total population in each year from
#2013 to 2016?
# Q3. Plot a visualisation of the age distribution, split out by year and by sex.
# Q4. What anomalies do you see in the data? Describe the external factors
# that could account for each anomaly.
# Investigate
# Q5.which geographies of the UK have a particularly high or low proportion
# of over-65s, and which show the largest change in proportion of over65s
# between 2013 and 2016.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


filename = 'C:\\Users\\cbpandey\\Downloads\\a3bffb7a-ca51-473b-8920-1477c0c34651.csv'
# Read the CSV file convered from Excel.
population = pd.read_csv(filename)

# Create dataframe with the population values.
df = pd.DataFrame(population.loc[:,['Geography','Geography code','Age','Sex','2013','2014','2015','2016']])
df.replace(to_replace='90+', value='90', inplace=True)

df.Age = pd.to_numeric(df.Age, errors='coerce')

df_1 = df[(df['Sex'] == 'All')]
# Group the rows by the Geography
df_1 = df_1.groupby('Geography')

# Get the sum and the minimum of the sum of populations for a given year.
sum_2013 = df_1['2013'].sum(skipna=True).idxmin()
sum_2014 = df_1['2014'].sum(skipna=True).idxmin()
sum_2015 = df_1['2015'].sum(skipna=True).idxmin()
sum_2016 = df_1['2016'].sum(skipna=True).idxmin()

print('Geography with minimum population in 2013 was %s \n' % sum_2013)
print('Geography with minimum population in 2014 was %s \n' % sum_2014)
print('Geography with minimum population in 2015 was %s \n' % sum_2015)
print('Geography with minimum population in 2016 was %s \n' % sum_2016)


# Get population over 65 and over all sex
df_65 = df[(df['Age'] >= 65) & (df['Sex'] == 'All')]

# Group the rows by the Geography
df_65 = df_65.groupby('Geography')

sum_65_2013 = df_65['2013'].sum(skipna=True)
sum_65_2016 = df_65['2016'].sum(skipna=True)
sum_2013 = df_1['2013'].sum()
sum_2016 = df_1['2016'].sum()

prop_65_2013 = (sum_65_2013/sum_2013)*100
prop_65_2016 = (sum_65_2016/sum_2016)*100

print('Geography with maximum change in proportion of over 65 in 2013 and 2016 was %s '
      'with change of %0.2f percentage. \n' %
      ((prop_65_2016 - prop_65_2013).abs().idxmax(),
       (prop_65_2016 - prop_65_2013).abs().max()))

print('Geography with higher change in proportion of over 65 in 2013 and 2016 was %s \n' %
      (prop_65_2016 - prop_65_2013).abs().nlargest(10))

print('Geography with smallest change in proportion of over 65 in 2013 and 2016 was %s \n' %
      (prop_65_2016 - prop_65_2013).abs().nsmallest(10))

print('Geographies with higher proportion of over 65s %s in 2016 \n' % prop_65_2016.nlargest(10))
print('Geographies with lower proportion of over 65s %s in 2016 \n' % prop_65_2016.nsmallest(10))



df = df[(df['Sex'] != 'All') & (df['Geography'] == 'Great Britain')]
print(df['Age'])
fig, ax = plt.subplots()
plt.interactive(True)
pivot_df = df.pivot(index='Age', columns='Sex',values=['2013','2014','2015','2016'])
pivot_df.plot(style=['b', 'g', 'r', 'c', 'm', 'y', 'k'])
plt.show(block=True)









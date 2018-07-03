# @Author: Chandra Pandey
# @Email: pandey.chandra@gmail.com
# In 2013, which geography had the highest female-to-male ratio, and
# what was the ratio?
# Which geography's female-to-male ratio changed the most between
# the census in 2013 and the census in 2016?

import pandas as pd

filename = 'C:\\Users\\cbpandey\\Downloads\\a3bffb7a-ca51-473b-8920-1477c0c34651.csv'
# Read the CSV file convered from Excel.
population = pd.read_csv(filename)

# Create dataframe with the population values.
df = pd.DataFrame(population.loc[:,['Geography','Geography code','Age','Sex','2013','2014','2015','2016']])
df.replace('90+', 90)
df.Age = pd.to_numeric(df.Age, errors='coerce')

df_1 = df[(df['Age'] >= 65)]

# Group the rows by the Geography
df_1 = df_1.groupby('Geography')

sum_65_2013 = df_1['2013'].sum()
sum_65_2016 = df_1['2016'].sum()

#print(sum_65_2013)
print(df_1.head())








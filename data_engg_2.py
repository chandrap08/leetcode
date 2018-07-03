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
df.replace(to_replace='90+', value='90', inplace=True)
df.Age = pd.to_numeric(df.Age, errors='coerce')
df_1 = df[(df['Sex'] == 'Male')]
df_2 = df[(df['Sex'] == 'Female')]

# Group the rows by the Geography
df_1 = df_1.groupby('Geography')
df_2 = df_2.groupby('Geography')

sum_m_2013 = df_1['2013'].sum()
sum_f_2013 = df_2['2013'].sum()

sum_m_2016 = df_1['2016'].sum()
sum_f_2016 = df_2['2016'].sum()

print('Geography with maximum female to male ratio in 2013 was %s with ratio %8.5f \n' %
      ((sum_f_2013/sum_m_2013).idxmax(),(sum_f_2013/sum_m_2013).max()))

print('Geography with maximum change in female to male ratio in 2013 and 2016 was %s with ratio %8.5f \n' %
      (((sum_f_2016/sum_m_2016) - (sum_f_2013/sum_m_2013)).abs().idxmax(),
       ((sum_f_2016/sum_m_2016) - (sum_f_2013/sum_m_2013)).abs().max()))

print('Geography with minimum change in female to male ratio in 2013 and 2016 was %s with ratio %8.5f \n' %
      (((sum_f_2016/sum_m_2016) - (sum_f_2013/sum_m_2013)).abs().idxmin(),
       ((sum_f_2016/sum_m_2016) - (sum_f_2013/sum_m_2013)).abs().min()))






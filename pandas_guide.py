
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# To read a Tab delimited file or files with a different delimiter: 
df_tab = pd.read_csv('pokemon_data.txt', delimiter='\t')

# #### READ THE DATA #### #

# Return the headers of the dataset
my_columns = df.columns

# Return a specific column from the dataset
# format: df['column name'] and df.column_name
attack = df['Attack']
attack_1 = df.Attack

# Read multiple columns
# format: df[['col 1', 'col 2', col 3,...]] to
multiple_columns = df[['Name', 'Attack', 'Speed']]

# Return a row
# format: df.iloc[row number]
my_row = df.iloc[24]

# Return a range of rows
# format: df.iloc[row number:row number]
my_rows = df.iloc[24:45]

# Grab  single cell
# format: df.iloc[r,c]
my_cell = df.iloc[24, 2]

# return index and row content
for index, row in df.iterrows():
    my_index = index
    my_row = row['Name']

# Statistical information about the dataset
# format df.describe()
description = df.describe()

# Return a table sorted by values in a column
# format: df.sort_values(col, ascending=True/False)
df_1 = df.sort_values('Name', ascending=True)


# Return a table sorted by values in multiple columns
# format: df.sort_values([col1, col2, col3,...])
df_2 = df.sort_values(['Name', 'Speed'])

# df.sort_values([col1, col2], ascending=[1,0]) will sort the first 
# column ascending and the second descending
df_3 = df.sort_values(['Type 1', 'Speed'], ascending=[1, 0])


# #### MAKING CHANGES TO THE DATA #####
# Create a new column df[new_col] that will represent the result of a function applied
# to other columns in the dataset. 
df['AttackSpeed'] = df['Attack'] + df['Speed']

# the function .sum(axis=1) sums the selected columns
# the function .sum(axis=0) sums the selected rows
# format: df.iloc[row:col] or df.iloc[from row:to row, from col:to col]
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# Change the value of a column
df['Speed'] = df['Speed'] * 2

# create a column with the value of an existing column changed
df['New_Speed'] = df['Speed'] * 2

# Change cell content in a column
df_new = df.copy()
df_new.loc[df_new['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# Create a new column with df.loc
df_new_2 = df.copy()
df_new_2.loc[df_new_2['Type 1'] == 'Fire', 'Legendary'] = True


# #### FILTER DATA IN A DATASET #####
# Filter data with a conditional statement using boolean operators
# format: df.loc[conditional statement]
type1_fire = df.loc[df['Type 1'] == 'Fire']

# Filter data with multiple conditional statement using boolean operators
# format: df.loc[(conditional statement) & (conditional statement)]

multiple_conditions = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

# Remember to reset the index after filtering
type1_fire = type1_fire.reset_index(drop=True)

# Filter a dataset with certain string in the content of a column
new_df = df.loc[df['Name'].str.contains('Mega')]

# Filter a dataset missing contains certain string in the content of a column
# ~ represents NOT
dff = df.loc[~df['Name'].str.contains('Mega')]

# To filter a dataset with a regular expression
import re
filter_fire_or_grass = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
starts_with_pi = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

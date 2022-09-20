import pandas as pd
import tableone as t1
import researchpy as rp

from tableone import TableOne, load_dataset

my_data = pd.read_csv('/Users/marialozano/Documents/GitHub/descriptives-scipy/data/data.csv')
my_data
my_data.columns 

##DATA SET 1##
example_dataset = load_dataset('pn2012') ##Load sample data into a pandas dataframe
example_dataset


##TRANSFORMATION: recode death where 0 = alive and 1 = dead 
## example_dataset['death'] = example_dataset['death'].replace(0, 'alive')
## example_dataset['death']

example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death'] ##a list of columns to be included in Table 1
example_data_categorical = ['ICU', 'death'] #list of columns that have categorical variables 
example_data_groupby = ['death']
example_data_labels={'death': 'mortality'} #relabels 'death' to 'mortality' instead

exampleTab1 = TableOne(example_dataset,columns=example_data_columns,categorical=example_data_categorical, groupby=example_data_groupby,rename=example_data_labels, pval=False)
exampleTab1 

print(exampleTab1.tabulate(tablefmt = "fancy_grid"))
exampleTab1.to_csv('/Users/marialozano/Documents/GitHub/descriptives-scipy/data/testtable.csv')

##PRACTICE WITH MY DATA

df2 = my_data.copy()
df2.dtypes
list(df2)

df2_columns = ['Age', 'Group','HR', 'sBP', 'Smoke']
df2_categories = [ 'Group', 'Smoke']
df2_groupby = ['Smoke']

##df2['Vocation'].value_counts()

df2_table1 = TableOne(df2,columns= df2_columns,categorical=df2_categories, groupby=df2_groupby, pval=False)
df2_table1
print(df2_table1.tabulate(tablefmt = "fancy_grid"))

df2_table1.to_csv('/Users/marialozano/Documents/GitHub/descriptives-scipy/data/test2.csv')
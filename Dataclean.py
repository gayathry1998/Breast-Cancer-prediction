import numpy as np         
import pandas as pd        # data processing, CSV file I/O (e.g. pd.read_csv)


data = pd.read_csv('data/data.csv', index_col=False,)

data.drop('id', axis =1, inplace=True)
#data.drop('Unnamed: 0', axis=1, inplace=True)
data.head(2)
data.shape
#data.info()
data.get_dtype_counts()
data.diagnosis.unique()
#save the cleaner version of dataframe for future analyis
data.to_csv('data/clean-data.csv')
from matplotlib.pyplot import close
import pandas as pd
from sqlalchemy import false
# importing pandas 

data = pd.read_csv('artwork_data.csv')
# opening artwork and saving it to a variable
# if there are missing values, it will most likely cause 
# the columns to be listed as objects

#print(data.head())
# prints the first 5 rows 

#print(data.dtypes)
# prints the estimated data type of each column

data.acquisitionYear.astype(float)
# assigns 'AcquisitionYear' to a new data type of float But this does
# not change my dataset 

data.acquisitionYear = data.acquisitionYear.astype(float)
# this assigns it to a variable which I can now use to change my dataset

fulldf = pd.read_csv("artwork_data.csv", low_memory=false)
#reads the full data set

#print(fulldf.dtypes)
#prints data types for the new set 

#print(fulldf.height.astype(float))
# This gives me a ValueError astype couldn't figure out 
# how to convert 'mm' from string to float 

pd.to_numeric(fulldf.height, errors="coerce")
#coerce the errors into a float type and it should return 'nan'
# for the errors that were 'coerced'

fulldf.height = pd.to_numeric(fulldf.height, errors="coerce")
# I have now changed my actual dataframe with the information 
#in line 33 
data.close()


sample = pd.read_csv("artwork_sample")
print(sample.head)

from matplotlib.pyplot import close
import pandas as pd
from sqlalchemy import false
from numpy import nan
# importing pandas 

data = pd.read_csv('artwork_data.csv', low_memory=False)
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

data.loc[data.title.str.contains('\s$', regex=True)]
# now I have several rows where the title ends in at least one white space
data.title = data.title.str.strip()
# strips white space on the entire series; this is not an inplace function and 
#must be set to a variable in order to change my dataset
#lstrip strips to the left while Rstrip goes to the right 
#I could also use 'transform' instead of strip

pd.isna(data.loc[:, 'dateText'])
#we are checking to see if the dateText column are numbers 
# after importing 'not a number' from numpy, I can use this below with 'replace'
data.replace({ 'dateText': {'date not known' : nan}})
# not done inplace, but If I added it, it would change my original data set 
#data.loc[data.year.notnull() & data.year.astype(str)str.contains('[^0-9']), ["year"]] = nan
# make sure to include the column name or it will set everything to nan
data.fillna(value={'depth': 0}, inplace=True)
# pass a value to fillna that is a dictionary. And in that dictionary we can put the colunns 
# to fill as the 'keys' and the values in the dictionary are the values put in the 'nan' spots 
# inplace will change my dataframe 

data.dropna()
# this will return a new dataframe. It dropped all the rows if any of the values were nan 
data.dropna(how='all').shape
# I would rather filter to see if there are any rows that have only NAN values. The shape will tell 
# me how many rows were dropped 
data.dropna(thresh=15).shape
# I could also check my rows and drop any that have over 15 blank (or 'nan') values

data.drop_duplicates(subset=['artist'], keep='first')
# I want to drop any row that has a duplicate artist and keeping the first item 
# must do 'inplace' in order to edit the original dataframe 

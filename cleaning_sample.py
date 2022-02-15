from curses import COLS
import pandas as pd

data = pd.read_csv("artwork_sample.csv")
#print(data.head)
#prints the first 5 rows 

#print(data.dtypes)
#prints the datatype of each column 

#print(data.year.min())
#print(data.year.max())
# prints the column 'year' min and max
#print(data.year.sum())
# sum of all the values 
#print(data.year.mean())
# mean of all the values 
#print(data.year.std())
# prints the standard deviation of all the years 
#nan's are automatically removed from these aggregate functions 

#print(data.agg(["min", "max", "mean", "std"]))
# I can pass in multiple arguments in the aggregate function to return an array 

#print(data.agg("mean, axis="columns"))
# it will print the means across all my columns 

#print(data.height.agg(["min", "max", "mean", "std"]))
# grabbing the helful stats first 

height = data.height 

norm = (height - height.mean())/height.std()
print(norm)
# I am normalizing my data. The formula above is specifically call 'standardization' 
# in statistics 
# I could also normalize my data into a specific range by placing it between 0 and one. I would do this 
# with this line of code. minmax = (height - height.min())/ (height.max()- height.min())

data["standardized_height"] = norm
# I didn't want to change this column, but I still want my values visible. So I appended 'norm' to 
# the columns in this data frame (I couldn't do this with dot notation because pandas doesn't allow it)

data.groupby('artist')
# this will output a dataframeGroupBy object 
data.groupby('artist').transform('nunique')
# this will count the number of unique rows per column grouped by artist
data.groupby('artist')['height']
#looks at the height column that is grouped by artist that cretates a SeriesGroupBy that I can also use transform on
data.groupby('artist')['height'].transform('mean')
#now this shows me, per artist, the mean of the height column. None of this has transformed my original dataset yet. 
# I could assign it to a column in my original dataframe by setting it equal to variable such as data['mean_height_by_artist]


data.filter(items=['id','artist'])
#this allows me to create a new dataframe with only two columns
data.filter(like='artist')
#I could also filter data using the 'like' param which is case sensitive 
data.filter(regex="(?i)year")
# we can filter all year columns now regardless of their case 
# data can also be filtered by rows


data.drop('0')
# drops the first row in the index
data.drop(columns=['id'])
# here I am only dropping the id column, but I could drop multiple columns at once if needed 
# I could read in the data = pd.read_csv('artwork_sample.csv', usecols=['artist, 'year', 'height'])
# which will take in an array of just those columns

data.columns.str.lower()
# this will make all the columns read in a lower case 
[x.lower() for x in data.columns]
# this does the same thing which gives us more control because we can add 
# an element of specificity to this logic 
#  remember that this does not change the original data set unless I set it equal to a variable 

data.rename(columns={'thumbnailUrl': 'thumbnail'})
#this renames the column to something more useful which accepts many different arguments. 
# in the example above, I just took in the original name and output the new name. I would use inplace if I wanted to change original df

data[1:2]
#I cannot access rows in a dataframe with square brackets but I can access a range of rows (inclusive for the first number and exculisve 
# for our second number) This would return only a single row. This also refers to the integer position of the row and not the actual index

data[data['year'] > 1800]
# return every row where the year is greater than 1800

#data.loc[ROWS, COLS]
#loc takes whichever rows we watn followed by whichever columns we want. 
data.loc[0, :]
#this would return the zeroth row and all the columns
data.loc[0:2, :]
#loc returns a range of rows that is inclusive on both ends. I will get three rows and all the columns
data.loc[0:2, ['artist', 'title']]
# this returns rows 0, 1, and 2 and the columns artist and title 
data.loc[[1,5], "id":"artistId"]
# this returns rows 1 and 5 and all columns from id to artistId
data.loc[data.artist == 'Blake, Robert', :]
# this returns every row where the artists name is 'Robert Blake' and every column
#loc is label based so I have to specify rows and columns based on their labels, 
#iloc is integer based so you have to specify rows and columns by their integer position values

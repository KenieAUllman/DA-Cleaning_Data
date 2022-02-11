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



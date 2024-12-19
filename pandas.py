import pandas as pd

# series pandas is :
    #like a data in a coulmn  
    #NB 1 dim array 
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
#labels 
a = [1, 7, 2]
myvar = pd.Series(a , index=["x", "y ","z"])
print(myvar)
# to print the value of specific element 
print(myvar[2]) # 2 is the index
# to create a dictionary series with keys and values 
a = {"a":1 , "b" :2 ,  "c":3}
myvar = pd.Series(a)
print(myvar)
# NB the keys in dictionary become a label 


#---------------------------------------------------------------------------------------------------------


# dataFrame pandas is :
    # data like rows and coulmns ( full table ) 
    #NB 2 dim array


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)
#Pandas use the loc attribute to return one or more specified row(s) using index
print(df.loc[0])
# NB the index of the row in the []
# to print the dataframe
print(df.to_string())
# to display the first 5 rows in the dataframe
print(df.head())
#NB : we can display specific rows from the start 
print(df.head(10))
# to display the last 5 rows in the dataframe
print(df.tail())
#NB : we can display specific rows from the last 
print(df.tail(10))

# to display information about dataframe
print(df.info()) 



# to load files to dataframe as :
    # csv file 
    #CSV files contains plain text and is a well know format that can be read by everyone including Pandas.


df = pd.read_csv('data.csv')

print(df)    

# to incerase the number of rows 
pd.options.display.max_rows = 9999
     # json file
     #JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
     # json file is as dictionary dataframe

df = pd.read_json('data.json')

print(df.to_string())

#---------------------------------------------------------------------------------------------------------


#Data cleaning means fixing bad data in your data set.

#Bad data could be:

#Empty cells
#Data in wrong format
#Wrong data
#Duplicates

#Empty Cells :
    #One way to deal with empty cells is to remove rows that contain empty cells.
import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna() #remove the empty rows 
print(new_df.to_string())
# to Remove all rows with NULL values:
import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True) #remove all rows containing NULL values from the original DataFrame

print(df.to_string())
#Replace Empty Values 
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
#NB : To only replace empty values for one column, specify the column name for the DataFrame:
df["Calories"].fillna(130, inplace = True)
# to Replace Using Mean, Median, or Mode
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mean() #Mean = the average value (the sum of all values divided by number of values)
x = df["Calories"].median() #Median = the value in the middle, after you have sorted all values ascending.
x = df["Calories"].mode()[0] #Mode = the value that appears most frequently.
df["Calories"].fillna(x, inplace = True)



#---------------------------------------------------------------------------------------------------------
#Data of Wrong Format :
    #Cells with data of wrong format can make it difficult, or even impossible, to analyze data
    # to Convert Into a Correct Format


import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())  
  

#---------------------------------------------------------------------------------------------------------

#Wrong Data :
    #Replacing Values
    #df.loc[index of row, coulmn key] = new value
df.loc[7, 'Duration'] = 45    
    

    #Removing Rows 
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True) #Delete rows where "Duration" is higher than 120


#---------------------------------------------------------------------------------------------------------
#Discovering Duplicates
#Duplicate rows are rows that have been registered more than one time.

print(df.duplicated()) #Returns True for every row that is a duplicate, otherwise False

#Removing Duplicates
df.drop_duplicates(inplace = True)
#---------------------------------------------------------------------------------------------------------
#Data Correlations ;
#Finding Relationships
df.corr() #Show the relationship between the columns

#Perfect Correlation:
     #We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.

#Good Correlation:
     #"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

#Bad Correlation:
      #"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.







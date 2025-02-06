import pandas as pd

data = {
    'Name': ['Emil', 'Anan', 'Emma', 'Georgi', 'Atanas', 'Maria', 'Jhon', 'Kimber', 'Johannes'],
    'Age': [32, 18, 22, 30, 23, 34, 17, 26, 43],
    'Town': ['Sofia', 'London', 'Paris', 'London', 'Rome', 'Prague', 'Sofia', 'Madrid', 'Berlin'], 
}

df = pd.DataFrame(data)

print(df)

# 0      Emil   32   Sofia
# 1      Anan   18  London
# 2      Emma   22   Paris
# 3    Georgi   30  London
# 4    Atanas   23    Rome
# 5     Maria   34  Prague
# 6      Jhon   17   Sofia
# 7    Kimber   26  Madrid
# 8  Johannes   43  Berlin


######################################


print(df.head())  # -> first five rows

print(df.head(3))  # -> first three rows

print(df.tail())  # -> last five rows

print(df.tail(1))  # -> last row

print(df.info())  # -> general information about the DataFrame (columns, data types, non-null values)

print(df.describe())  # -> summary statistics for numerical columns

print(df['Name'])  # -> selecting a single column (returns a Series)

print(df[['Name', 'Age']])  # -> selecting multiple columns (returns a DataFrame)

print(df.iloc[3])  # -> selecting a row by index (fourth row, index starts at 0)

print(df[df['Age'] > 25])  # -> filtering rows where Age > 25



#######################################


df['Salary'] = [2000, 1500, 1800, 2500, 2200, 3000, 1200, 2700, 3500]  # -> added a new column 'Salary'
print(df)

df.loc[3, 'Town'] = 'New York'  # -> updated value in the 'Town' column for row with index 3
print(df)

df = df.drop(columns=['Salary'])  # -> removed the 'Salary' column
print(df)

df = df.drop(index=2)  # -> removed the row with index 2
print(df)

filtered_df = df[(df['Age'] > 15) & (df['Town'] == 'Sofia')]  # -> filtered rows where 'Age' > 15 and 'Town' is 'Sofia'
print(filtered_df)
















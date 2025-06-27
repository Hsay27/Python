import pandas as pd
import numpy as np

# data = {"col1":[3,np.nan,np.nan,2], "col2":[1.0,pd.NA,pd.NA,2.0]}
# df = pd.DataFrame(data)
# print(df)

# f = df.fillna('-')
# print(f)

# data = [[9,-3,-2],[-5,1,8],[6,4,-8]]
# df = pd.DataFrame(data,index=['a','c','d'],columns=['one','two','three'])
# df = df.reindex(['a','b','c','d','e'])
# print(df)

# result = df.ffill()
# print(result)

# result = df.bfill()
# print(result)

# data = [[9,-3,-2],[-5,1,8],[6,4,-8]]
# df = pd.DataFrame(data,index=['a','b','c'],columns=['one','two','three'])
# df = df.reindex(['a','b','c','d','e'])
# print(df)

# result = df.ffill(limit=1)
# print(result)

# data = {'one':[9,-3,-2,5],'two':[-5,1,8,10]}
# df = pd.DataFrame(data)
# print(df)

# result = df.replace({-5:9,10:5})
# print(result)

# data = ['40000','40000 attached']
# df = pd.DataFrame(data,columns=['p'])
# print(df)

# df['p'] = df['p'].str.replace(r'\D+','', regex=True).astype('int')
# print(df)

# data= {'category':['a','b','a','c','b','c','a'],
#        'values':[10,45,55,32,65,23,75]}

# df = pd.DataFrame(data)

# group_data = df.groupby('category')['values'].sum()
# print(group_data)

# group_data = df.groupby('category')['values'].mean()
# print(group_data)

# group_data = df.groupby('category')['values'].count()
# print(group_data)

# group_data = df.groupby('category')['values'].min()
# print(group_data)

# group_data = df.groupby('category')['values'].max()
# print(group_data)

# group_data = df.groupby('category')['values'].agg(sum)
# print(group_data)

# data= {'category':['a','b','a','c','b','c','a'],
#        'subcategory':['x','y','x','z','y','z','y'],
#        'values':[10,45,55,32,65,23,75]}

# df = pd.DataFrame(data)

# group_data = df.groupby(['category','subcategory'])['values'].sum()
# print(group_data)

# group_data = df.groupby(['category','subcategory'])['values'].mean()
# print(group_data)

# group_data = df.groupby(['category','subcategory'])['values'].count()
# print(group_data)

# group_data = df.groupby(['category','subcategory'])['values'].min()
# print(group_data)

# group_data = df.groupby(['category','subcategory'])['values'].max()
# print(group_data)

# group_data = df.groupby(['category','subcategory'])['values'].agg(sum)
# print(group_data)

# data = {'name':['abc','xyz','pqr'],'age':[28,22,34]}
# df = pd.DataFrame(data)
# print(df)

# result = df.sort_values(by="name")
# print(result)

# result = df.sort_values(by="name", ascending=True)
# print(result)

# result = df.sort_values(by="name", ascending=False)
# print(result)

# result = df.sort_values(by=["name","age"], ascending=[True,False])
# print(result)

# result = df.sort_values(by="age",inplace=True)
# print(result)

# result = df.sort_index(ascending=False)
# print(result)

# result = pd.date_range("6/1/25",periods=5)
# print(result)

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
# print(df)
# result = df.head(10)
# print(result)
# result = df.tail(10)
# print(result)
# result = df.info()
# print(result)
# result = df.describe()
# print(result)
# result = df.shape
# print(result)
# result = df.columns
# print(result)
# result = df['Name']
# print(result)

# ....

# result = df.groupby('Country')['Index'].mean()
# print(result)
# result = df['Name'].value_counts
# print(result)

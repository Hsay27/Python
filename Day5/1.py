import pandas as pd      
#pd = pandas directory

# a = [10,20,30,40]

# s = pd.Series(a)   #write pd if as pd is given otherwise write pandas.series()   ye column me deta h
# print(s[1])
# print(type(s))

# marks = {"day1":583, "day2":483, "day3":884}
# var = pd.Series(marks,dtype=float)
# print(var)


# marks = {"day1":583, "day2":483, "day3":884}
# var = pd.Series(marks,index=['day1','day2','day3'])
# print(var['day2'])


# print(df)
# print(type(df))
#
# print(pd._version_)   # state the version of pandas


# s = pd.Series(a,index=['a','b','c','d'])
# print(s['b'])
# print(type(s))


# data = {"num":[10,20,30,40],
#       "alpha":['A','B','C','D']
# }
# df = pd.DataFrame(data)
# print(df)
# print("--------------------------------------")
# print(df.loc[1])
# print(df.loc[[0,1]]) # do eaksath karane h to 2 square bracket lagane padenge
# print(df.columns)   # printing columns name
# df.columns=["cup","cake"]    #modify column name
# print(df)

# df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'],
# index = ['r1','r2','r3','r4'])

# print(df)
# result = df.loc['r1':'r3','col1']
# print(result)

# data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
# df = pd.DataFrame(data)

# col_A = df.loc[:,'A']
# print(col_A)

# cols_AB=df.loc[:,'A':'B']
# print(cols_AB)

# df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'])
# print(df)

# df.iloc[1:3,0] = ['x','y']
# print(df)

df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8],'C': [9, 10, 11, 12, 0]}, 
                  index=['r1', 'r2', 'r3', 'r4', 'r5'])

# print(df)
# result = df[df["C"] != 0]
# print(result)
print(df)
result = df.drop(df.index[2:4])
print(result)
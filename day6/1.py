import pandas as pd

# data={'A':[1,2,3,4],'B':[5,6,7,8]}
# df = pd.DataFrame(data)
# print(df)
# print("\n addition is \n ", df+5)
# print("\n substraction is \n ", df-5)
# print("\n multiplication is \n ", df*5)
# print("\n divison is \n ", df/2)

# df['C']=df['A']+df['B']
# print(df)

# data1={'A':[11,12,13],'B':[15,16,17]}
# df1=pd.DataFrame(data1,index = [1,2,3])
# print(df1)
# print("\n addition of two dataframes is: \n", df + df1)
# print("\n subtraction of two dataframes is: \n", df - df1)
# print("\n multiplication of two dataframes is: \n", df * df1)
# print("\n divison of two dataframes is: \n", df / df1)

# one = pd.DataFrame({
#     'Name':['a1','a2','a3','a4','a5'],
#     'subject':['sub1','sub2','sub3','sub4','sub5'],
#     'marks':[32,75,75,56,86]},
#     index=[1,2,3,4,5]
# )

# two = pd.DataFrame({
#     'Name':['b1','b2','b3','b4','b5'],
#     'subject':['sub1','sub2','sub3','sub4','sub5'],
#     'marks':[99,86,35,76,54]},
#     index=[1,2,3,4,5]
# )
# res = pd.concat([one, two])
# print(res)

# res = pd.concat([one, two], keys=['a','b'])
# print(res)

# res = pd.concat([one, two], keys=['a','b'], ignore_index=True)
# print(res)

# res = pd.concat([one, two], axis=1)
# print(res)

# left = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['a1','a2','a3','a4','a5'],
#     'subject':['sub1','sub2','sub6','sub4','sub5'],
#     'marks':[99,86,35,76,54]
# })

# right = pd.DataFrame({
#         'id':[1,2,3,4,5],
#     'Name':['b1','b2','b3','b4','b5'],
#     'subject':['sub1','sub2','sub3','sub4','sub5'],
#     'marks':[32,75,35,56,86]
# })

# result = left.merge(right,on='id')
# print(result)

# result = left.merge(right,on='marks')
# print(result)

# result = left.merge(right,on=['marks','id'])
# print(result)

# result = left.merge(right,on='subject',how='left')
# print(result)

# result = left.merge(right,on='subject',how='right')
# print(result)

# result = left.merge(right,on='subject',how='outer')
# print(result)

# result = left.merge(right,on='subject',how='inner')
# print(result)

# result = left.merge(right,how='cross')
# print(result)

# result = left.join(right,rsuffix='_right',lsuffix='_left')
# print(result)
# result = left.join(right,rprefix='_right',lsuffix='_left')
# print(result)                         there is no argument for prefix we have to add it individually

# df=pd.DataFrame({"col1":range(12),"col2":['A','A','A','B','B','B','C','C','C','D','D','D']
#                  , "date":pd.to_datetime(["2025-06-20","2025-06-21","2025-06-22"]*4)
# })

# print(df)

# result= df.pivot(index="date",columns="col2",values="col1")
# print(result)
# result= df.pivot(index="date",columns="col1",values="col2")
# print(result)

data = {
    "course":['cs','civil','cs','civil','cs'],
    "year":[1,2,1,1,2],
    "students":[100,150,120,90,180]
}
df=pd.DataFrame(data)
print(df)

result = df.pivot_table(
    index="course",
    columns="year",
    values="students",
    aggfunc="sum"
)
print(result)
import numpy as np

# a=np.array([[[1,2,3],[2,3,4],[4,5,6]],[[3,2,1],[4,3,2],[6,5,4]]])
# print(a)
# print(a.shape)

# a=np.zeros((4,2,3))
# print(a)

# a=np.array([1,2,3,5,2,4,2,8 ,9 ,10 , 11 , 12 ])
# base =1
# x = a.copy()
# y= a.view()
# print(a)
# print(x)
# print(x.base)
# print(y.base)
# print(a.reshape(3,4),base)

# a=np.array([1,2,3,5,2,4,2,8 ,9 ,10 , 11 , 12 ], ndmin=5)
# print(a)

# a=np.array([[1,2,3,5] ,[9 ,10 , 11 , 12 ]])
# print(a)
# a1=a.reshape(-1)
# print(a1)

# a = np.array([[1,2,3,4,5],[5,4,3,2,1]])
# for x in a:
#     print(x)
#     for y in x:
#         print(y)
        
# for x in np.nditer(a):
#     print(x)

# a = np.array([[1,2,3,4,5],[6,4,3,2,1]])
# x=a.ravel()
# print(x)
# x=np.unique(a)
# print(x)
# x=a.sum()
# print(x)
# x=a.sum((1))
# print(x)

# a= np.array([1,2,3,4])
# b=np.array([2,3,4,5])
# x=np.add(a,b)
# print(x)

# x=np.dot(a,b)
# print(x)

# x=np.pad(a,pad_width=2,mode="constant")
# print(x)

# a= np.array([[1,2,3,4],[2,3,4,5]])
# x=np.transpose(a)
# print(a)
# print(x)

# a=np.arange(9)
# print(a)
# x=np.split(a,3)
# print(x)
# b=np.resize(a,(3,2))
# print(b)
# b=np.resize(a,(3,3))
# print(b)

# a=np.array([[1,2,3],[4,5,6]])
# x=np.append(a,[[7,8,9]],axis=0)
# print(x)


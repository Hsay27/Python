import numpy as np

# a = np.array([[1,2,3],[2,3,4]])
# print(a)
# print(a.dtype)

# a = np.array([1,2,3], dtype='i8')
# print(a)
# print(a.dtype)

# a=np.array([]).dtype
# print(a)

# list = [1,2,3,4]
# a = np.array()

# a=np.ones(4)
# print(a)
# a=np.ones((4,3))
# print(a)
# a=np.ones((4,3),order='F')
# print(a)
# a=np.arange(1,10,2)
# print(a)
# a1=np.linspace(0,5,num=10)
# print("a1:",a1)
# a2=np.linspace(1,2,num=5,endpoint=False)
# print("a2:",a2)
# a3,step=np.linspace(0,10,num=5,retstep=True)
# print("a3",a3)
# print("step size ", step)

# a=np.random.rand(2,3,4)
# print("a",a)

# a=np.empty((2,3))
# print("a",a)

# a=np.full((2,3),3)
# print("a",a)

# a=np.array([[[2,3,4,5],[6,7,8,9]], [[1,2,3,6],[3,4,5,9]]])
# print("a",a[0,1,2])

a=np.array([[2,3,4,5],[6,7,8,9], [1,2,3,6],[3,4,5,9]])
print("a",a[0:6,2])
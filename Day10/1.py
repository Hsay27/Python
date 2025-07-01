import numpy as np

# arr = np.array([[10,20,30],[2,3,4],[6,7,8],[4,5,6]])
# print(arr)

# arr[[0,2],:]=arr[[2,0],:]
# arr[:,[0,2]]=arr[:,[2,0]]
# print(arr)
# print(arr[0])

# arr[[1],[0,2]]=arr[[1],[2,0]]
# print(arr)

# arr = np.array([[[10,20,30],[2,3,4]],[[6,7,8],[4,5,6]]])

# arr[[0,1],[0,1],:]=arr[[1,0],[1,0],:]
# print(arr)

# arr = np.array([10,10,np.nan,4, np.nan,5])
# res = np.nan_to_num(arr,copy=True, nan=2, posinf=None, neginf=None)
# print(arr)
# print(res)

# arr = np.array([[10,20,30],[4,5,6]])
# np.save('data.npy', arr)

# res = np.load('data.npy')
# print(res)

# arr1 = np.array([[10,20,30],[2,3,4],[6,7,8],[4,5,6]])
# arr2 = np.array([[10,20,30],[2,3,4]])

# np.savez('data.npz', arr1=arr1, arr2=arr2)

# res = np.load('data.npz')
# print(res['arr1'])
# print(res['arr2'])

# with open('data.txt', 'w') as f:
#     f.write('10 20 30\n2 3 4\n6 7 8\n4 5 6\n')

# res = np.loadtxt('data.txt')
# print(res)

# data = np.array([[3,6,8],[8,3,5]])
# np.savetxt('data.txt', data, delimiter=' ',fmt='%1.1f')

# res = np.loadtxt('data.txt')
# print(res)

# with open('data.csv', 'w') as f:
#     f.write('10,20,30\n2,3,4\n6,7,8\n4,5,6\n')
    
# res = np.genfromtxt('data.csv', delimiter=',')
# print(res)

arr1 = np.array([[10,20],[2,3]])
arr2 = np.array([10,20])

res = np.linalg.solve(arr1, arr2)
print(res)
inv = np.linalg.inv(arr1)
print(inv)
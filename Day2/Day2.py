# a=8
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)


# a=50
# a+=20
# print(a)

# x=25
# y=23
# print(x==y)
# print(x!=y)
# print(x>=y)
# print(x<=y)
#
# if x is not y:
#     print(x==y)
#     print(x!=y)
#     print(x>=y)
#     print(x<=y)
#
# str = "Yash"
# if 'Y' in str:
#     print(str)

# a = 10
# b = 8
# print(bin(a))
# print(bin(b))
# print(a&b)

# a= int(input('enter any number: '))
# if a%2 == 0:
#     print('number is even')
# else:
#     print('number is odd')


# a= int(input('enter any number: '))
# if a<8:
#     print('number is less than 8')
#     if a<6:
#         print('number is less than 6')
# else:
#     print('number is greater than 8')


# a= int(input('enter any number: '))
# if a<8:
#     print('number is less than 8')
# elif a>8:
#     print('number is greater than 8')
# else:
#     print('number is equal to 8')

# per = int(input("percentage?: "))
# if per > 60:
#     print('Good')
# elif per > 30:
#     print('average')
# else:
#     print('fail')

# a= int(input('Enter 1st no.: '))
# b= int(input('Enter 2nd no.: '))
#
# operator = str(input('enter the operator to perform: '))
# if operator == '+':
#     print(a+b)
# elif operator == '-':
#     print(a-b)
# elif operator == '*':
#     print(a*b)
# else:
#     print(a/b)

# for x in range(1,10,2):
#     print(x)
#
# for x in range(9, 0, -2):
#     print(x)

# for x in range(1,10,2):
#     pass

# a = int(input('enter number: '))
# for x in range(1,11,1):
#     print(a,'*',x,'=',a*x)

# a = int(input('enter number: '))
# for x in range(1,11,1):
#     if x > 5:
#         break
#     print(a,'*',x,'=',a*x)

# a = int(input('enter number: '))
# for x in range(1,11,1):
#     if x == 5:
#         continue
#     print(a,'*',x,'=',a*x)

# a = int(input('enter number: '))
# for x in range(1,11,1):
#     if x%2==0:
#         continue
#     print(a,'*',x,'=',a*x)

# for x in range(3):
#     for y in range(4):
#         print(x,y)

# for x in range(3,5):
#     for y in range(1,11):
#         print(x,'*',y,'=',x*y)

# for x in range(9):
#     for y in range(10):
#         if x <= y:
#             print(y,end=" ")
#             print( )
#             break
#         print(y, end=" ")

# while True:
#     n = int(input("enter any number and 0 to exit: "))
#     if n==0:
#         break
#     print(n)

# str = "Sanidhya"
# l = len(str)
# print(l)
# print(str)
# print(str[0::2])
# print(str[4])
# print(str[-2])
# print(str[0:7])
# print(str[-1::-1])
# print(str[-1:-8:-1])
# print(str[-8:-1])
# print(str[-8:])

# l = [10, 20, 30, 40, "python", [1,2,3]]
# print(type(l))
# print(l)
# print(l[5])
# print(l[5][1])
# l.reverse()
# print(l)

# l = [10, 20, 30, 40,50]
# s=0
# for x in l:
#     s+=x
# print(s)

# x= input("enter elemnets with space: ")
# l= x.split()
# print(l)

# l1 = []
# l1.append(10)
# l1.append(20)
# print(l1)
# l2 =["yash","sanidhya"]
# l1.append(l2)
# print(l1)
# l1.insert(0,50)
# l1.extend(["x","y"])
# print(l1)

# l= [1,2,3,4,5,6,7,8]
# l.remove(2)
# l.pop()
# l.pop(3)
# print(l)

# while True:
# print('''
# 1. Create Bill
# 2. Display Item Price and total bill amount
# 3. Display Total
# 4. Exit
# ''')
# ch = int(input("your choice: "))
# if ch == 1:
#     pass
# elif ch == 2:
#     pass
# elif ch == 3:
#     pass
# elif ch == 4:
#     pass
# else:
#     print("invalid value")
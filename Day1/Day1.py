# print("hello python")
# print('hello Python',"welcome",6,sep=",")
# print('hello Python',"welcome",6,sep=" ",end="---")
# print("hello")
# print('hello')
# print(8-5)
# print(10<2)
# print(10>2)
#
# a=8
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print('The sum of',a,'and',b,'is', a+b)
# print(f'The sum of {a} and {b} is {a+b}')
# print(f'The sum of {a} and {b} is',a+b,sep=" ")
# print(f"The sum of {a} and {b} is {a+b}")
#
#
# print(f"The value of a {a} and the value of b {b} and the sum is {a+b}")
# print(f"the value of pi is {22/7:.3f}")
# print(f"the value of pi is {22/7:.10f}")
# print(f"the value of pi is {22/7:.1f}")
#

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# print(a,'and',b)
# print("sum is", a+b)
# print(f"The value of a {a} and the value of b {b} and the sum is {a+b}")

# help("keywords")

a=25
print(a)
print(type(a))
a="python"
print(a)
print(type(a))

print('''
1. Yash
2. Sanidhya
3. Lakshay
4. Shivam
''')

a=10
b=10
print(id(a))
print(id(b))

a=10
b=5
print(id(a))
print(id(b))

a="yAsH Bansal"
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.capitalize())
print(a.center(50))
print(a.count("B"))

str="Names:\nA\nB\nC\nD"
print("string before splitting: " +str)
print("string after splitting: ")
print(str.splitlines())


a="tipon"
b="12345"

str= "this is python"
encoding = str.maketrans(a,b)
print(str.translate(encoding))
# d = {1:"Python", 2:"java", "name":"Programs", 4:{1:'one',2:'two'}}
# print(d)
# print(d[1])
# print(d['name'])
# print(d[4])
# print(d[4][2])

# dict = {}
# print(dict)
# dict[0]='yash'
# dict[1]='Sanidhya'
# dict[3]='Shivam'
# print(dict)
#
# dict2 = dict.copy()
# print(dict2)
# # dict.clear()
# print(dict)
# print(dict.get(2))
# dict.pop(1)
# print(dict.items())
# print(dict.popitem())
# print(dict)

# dict = {'a':10,'b':5}
# dict2 = {'c' :7,'d':9}
#
# dict2.update(dict)
# print(dict2)

# t=(10,20,30,40,50)
# print(t)
# print(type(t))
# l = len(t)
# for x in range(l):
#     print(x, t[x])
# print(2, t[2])

# l = [10,20,30,40]
# t = tuple(l)
# print(t)
# print(max(t))
# print(min(t))
# print(t.count(10))
# print(t.index(10))
# print(sum(t))

# s = {"a","b","c","d","e"}
# print(s)

# s = {"apple","banana","cherry"}
# s.add("mango")
# print(s)

# s1={"a","b","c","d","e"}
# s2={10,20}
# s3=s1.union(s2)
# print(s3)

# s1=set()
# s2=set()
#
# for i in range(5):
#     s1.add(i)
# for i in range(3,9):
#     s2.add(i)
# s3=s1.intersection(s2)
# print(s3)
# s4=s1&s2
# print(s4)
#
# s5=s1.difference(s2)
# print(s5)

# def sanidhya(a=0,b=0):
#     print("Sum", a+b)
#
# sanidhya(12)

# def sanidhya(a=0,b=0):
#     res = a+b
#     return res
#
# sum = sanidhya(12,15)
# print(sum)

# def place(*city):
#     print(city[1])
# place("jaipur","delhi","mumbai")

# def place(city3,city2,city1):
#     print(city1)
# place(city1="jaipur",city2="delhi",city3="mumbai")

# def place(**city):
#     print(city['lname'])
#
# place(fname="new",lname="delhi")

f = open("new1.txt","w")
f.write("sanidhya dewaana ")
f.write("kisi ke peehce pagal hai beechara")
f.close()

f = open("new1.txt","r")
# for i in f:
#     print(i)
# print(f.read())
# data = f.read()
# print(data)
data = f.readlines()
for line in data:
    word = line.split()
    print(word)
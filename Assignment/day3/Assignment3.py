print("*********Q.1***********")

s = ("apple", "banana", "cherry")
print("Original Tuple:", s)
print("First element:", s[0])
for item in s:
    print("Tuple item:", item)


print("\n=== Dictionary Example ===")

dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Original Dictionary:", dict)

print("Name:", dict["name"])


dict["job"] = "Engineer"
print("Updated Dictionary:", dict)


for key, value in dict.items():
    print(f"{key} -> {value}")


print("\n=== Set Example ===")

set = {1, 2, 3, 4, 4, 2}
print("Original Set (duplicates removed):", set)


set.add(5)
print("Set after adding 5:", set)

set.remove(2)
print("Set after removing 2:", set)


another_set = {3, 4, 5, 6}
print("Intersection:", set & another_set)
print("Union:", set | another_set)
print("Difference:", set - another_set)

print("*********Q.2***********")

def maths(a=0, b=0):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Division Cannot divide by zero")


a = int(input("enter the a value"))
b = int(input("enter the b value "))

maths(a, b)

print("**********Q.3***********")

s = input("Enter the string: ")
length = len(s)
mid = length // 2

rev = -1
for a in range(mid):
    if s[a] == s[rev]:
        rev -= 1
    else:
        print(s, "is not a palindrome")
        break
else:
    print(s, "is a palindrome")
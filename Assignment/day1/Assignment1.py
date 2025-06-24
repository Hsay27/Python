print("*****Q.1*******")

name = input("Enter student name: ")
student_class = input("Enter class: ")
print("Enter marks for 5 subjects:")
mark1 = int(input("Subject 1: "))
mark2 = int(input("Subject 2: "))
mark3 = int(input("Subject 3: "))
mark4 = int(input("Subject 4: "))
mark5 = int(input("Subject 5: "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100
print("\n----- Student Result -----")
print("Name:", name)
print("Class:", student_class)
print("Total Marks:", total_marks)
print("Percentage: {:.2f}%".format(percentage))

if percentage>90:
    print('excellent')
elif percentage>70:
    print('good')
elif percentage>50:
    print('average')
elif percentage>33:
    print('below average')
else:
    print('Fail')

print("********Q.2**********")

a = str(input("Enter first string: "))
b = str(input("Enter second string: "))
c = a + b

print("\n----- String Operations -----")
print("Concatenated String:", c)
print("Uppercase:", c.upper())
print("Lowercase:", c.lower())
print("Title Case:", c.title())
print("Capitalized:", c.capitalize())
print("Length of String:", len(c))
print("Is Alphanumeric:", c.isalnum())
print("Is Alphabetic:", c.isalpha())
print("Reversed String:", c[::-1])
print("Count of 'a':", c.count('a'))
print("----------------Q.2---------------")

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

if percentage>=60:
    print('Grade A')
elif percentage>=50:
    print('Grade B')
elif percentage>=40:
    print('Grade C')
elif percentage>33:
    print('Grade D')
else:
    print('Fail')

print("-------------Q.3------------")

a = int(input("enter number to find its factorial: "))
fac = 1
for x in range(a,0,-1):
    fac*=x
print(fac)

print("-------------Q.4-----------")

a = []
n = int(input("Enter how many times you want to use the billing system: "))
for _ in range(n):
    print("1. Create Bill")
    print("2. Display Items and Total")
    print("3. Display Total Only")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        item = input("Enter item name: ")
        price = input("Enter item price: ")
        a.append([item, price])
        print("Item added.\n")
    elif choice == '2':
        if not a:
            print("No items in the bill.\n")
        else:
            total = 0
            print("\nItems in the Bill:")
            for i in a:
                print(i[0], ": $", i[1])
                total = total + float(i[1])
            print("Total Bill Amount: $", total, "\n")
    elif choice == '3':
        total = 0
        for i in a:
            total = total + float(i[1])
        print("Total Amount: $", total, "\n")
    elif choice == '4':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice.\n")

print("------------Q.5-----------")

a= [5, 2, 9, 1, 7]

smallest = a[0]
greatest = a[0]
smallest2= a[0]
greatest2= a[0]
for x in a:
    if  x < smallest:
        smallest = x

print("Smallest number is:",smallest)

for y in a:
    if y < smallest2:
        if y > smallest:
            smallest2 = y

print("2nd smallest is : ", smallest2)

for w in a:
    if  w > greatest:
        greatest = w

for z in a:
    if z > greatest2:
        if z <greatest:
            greatest2 = z

print("2nd smallest is : ", greatest2)
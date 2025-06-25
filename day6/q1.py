a= [5, 2, 9, 1, 7]

x = min(a)
w = max(a)
smallest2= a[0]
greatest2= a[0]

print("Smallest number is:",x)

for y in a:
    if y < smallest2:
        if y > x:
            smallest2 = y

print("2nd smallest is : ", smallest2)

for z in a:
    if z > greatest2:
        if z < w:
            greatest2 = z

print("2nd smallest is : ", greatest2)
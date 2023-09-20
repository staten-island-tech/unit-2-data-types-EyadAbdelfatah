x = 3
y = float(3)
print(x,y)

x = "test"
print(f"hello {x}")

temp = float(68)
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')

values = [1,2,23,5,7,2,30,15]
print(values[2])

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

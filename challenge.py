x=int(input("Enter a number:"))
e=("even")  
o= ("odd")
def oddoreven(x):
    print({x})
    if x % 2 == 0:
        print(e)
    else: 
        print(o)
oddoreven(x)


g=("good")
b=("bad")
o=("okay")
gr=("great")
y=int(input("What was your bill?:"))
x=(input("How was your service?:"))
def tips():
    print({x})
    if {g}:
        print(1.2* y)
    elif {b}:
        print(y)
    elif {o}:
        print(1.15*y)
    else :
        print(1.25*y)
tips()


def factors(x,y):
        if x>=y:
            if x % y ==0:
                print(y)
                y = y+1
                factors(x,y)
            else:
                y=y+1
                factors(x,y)
factors(328,1)
    
def greatest(a,b,c,d):
    if a>=b:
        if a % b ==0 :
            b =b+1
    if c>=d:
        if c%d ==0:
            d=d+1
    if c:=d:
        print(c,d)
greatest(200,1,300,1)
        

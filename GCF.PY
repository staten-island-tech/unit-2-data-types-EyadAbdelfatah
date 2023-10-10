y = 1
y = y+1

def factors(x,y):
        if x>=y:
            if x % y ==0:
                print(y)
                y = y+1
                factors(x,y)
            else:
                y=y+1
                factors(x,y)
        return (y)

everything=[]
something=[]

def eggs():
     factors(24,1)
     everything.append(y)

def toast():
     factors(36,1)
     something.append(y)
  
anything=[]
def gcf():
     for y in everything:
          for x in something:
               if x==y:
                    anything.append(x)
                    print(anything(-1))
gcf()
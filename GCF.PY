everything=[]
something=[]
def factors(x,y):
     if x>=y:
          if x % y ==0:
               print(y)
               everything.append(y)
               y = y+1
               factors(x,y)
          else:
               y=y+1
               factors(x,y)
          return (y)
          
def factors2(x,y):
     if x>=y:
          if x % y ==0:
               print(y)
               something.append(y)
               y = y+1
               factors2(x,y)
          else:
               y=y+1
               factors2(x,y)
          return (y)     



def eggs():
     factors(24,1)
     print(everything)
eggs()
def toast():
     factors2(36,1)
     print(something)
toast()
anything=[]
def gcf():
     for y in everything:
          for x in something:
               if x==y:
                    anything.append(x)
     print(anything[-1])
     print(anything)
gcf()
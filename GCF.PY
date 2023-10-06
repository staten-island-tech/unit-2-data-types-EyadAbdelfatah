def factors(x,y):
        if x>=y:
            if x % y ==0:
                print(y)
                y = y+1
                factors(x,y)
            else:
                y=y+1
                factors(x,y)


def gcf(x,y):
     while x>=y:
          if x%y>0:
            y=y+1
            return (x)
          print(x,y)
gcf(24,1)
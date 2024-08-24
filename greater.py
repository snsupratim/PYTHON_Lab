# greatest among three number

a=int(input("enter a number = "))
b=int(input("enter a number = "))
c=int(input("enter a number = "))

if (a>b)and(a>c) :
    print("{} is greatest".format(a))
elif (b>c)and(b>a) :
    print("{} is the greatest".format(b))
else :
    print("{} is the greatest".format(c))    


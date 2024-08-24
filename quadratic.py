#qudratic equations

a=int(input("enter 'a' : "))
b=int(input("enter 'b, : "))
c=int(input("enter 'c' : "))

if a!=0:
    d=b**2-4*a*c
    if d<0 :
        print("no real root")
    elif d==0 :
        r1=-b/(2*a)
        print("{} roots are eqaul and real".format(r1))
    else:
         r1=((-b+(d**0.5))/(2*a))
         r2=((-b-(d**0.5))/(2*a))
         print("{} & {} are two roots".format(r1,r2))       
else :
    print("not a quadratic equation")   
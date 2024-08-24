# to display fibanocci series:

nterms=int(input("enter a range: "))

n1,n2 = 0,1
count=0

if nterms<=0:
    print("enter a valid range:")
elif nterms==1:
    print("the fibanocci series is:")
    print(n1)
else:
    print("the fibanocci seires is :")
    while count<nterms:
        print(n1,end=' ')
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1        
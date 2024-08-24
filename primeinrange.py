# 2.generate prime number within a range:

nterms=int(input("enter a range = "))

for i in range(1,nterms):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)  

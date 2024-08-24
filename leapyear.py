 #leap year

year=int(input("enter the year="))

if (year%4==0)and(year%100!=0) :
    print("{} is leap year".format(year))
elif year%400==0 :
    print("{} is leap year".format(year))
else :
    print("{} is not a leap year".format(year))    
   
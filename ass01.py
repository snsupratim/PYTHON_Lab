#question no-01
# print("MCKVIE\nComputer Science &Engineering")

#question no-02
# num1= int(input("Enter the first number: "))
# num2= int (input("Enter the second number:"))

# sum_result=num1+num2
# print("the sum of {} and {} is {}." .format(num1,num2,sum_result))

#question no-03

# p=float(input("Enter the principal amount (p): "))
# r=float(input("enter rate of interest (R):"))
# t=float(input("enter the given time(T):"))

# s=(p*r*t)/100
# print("simple interest: {} ".format(s))

#question no-04


radius =float(input("enter the radius of the circle: "))
area= 3.14*radius**2
perimeter=2*3.14*radius

print("Area of the circle is:{:.2f}".format(area))
print("perimeter if the circle :{:.2f}".format(perimeter))

#question no-05
#using third variable

# a=int(input("enter first number'a':"))
# b=int(input("enter second number'b':"))

# temp=a
# a=b
# b=temp

# print("after swapping using a third variable\n a={} and b={}:".format(a,b))

# #without 3rd variable

# x=int(input("enter first number'x':"))
# y=int(input("enter second number'y':"))

# x=x+y
# y=x-y
# x=x-y

# print("after swapping using a third variable\n x={} and y={}:".format(x,y))

#question no-06
import math

a=int(input("enter sides as 'a':"))
b=int(input("enter sides as 'b':"))
c=int(input("enter sides as 'c':"))

#s is semi-perimeter
s=(a+b+c)/2
print("Semi-perimeter is {}".format(s))

#finding the area

area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle:{:.2f}".format(area))







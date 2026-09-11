import math 
a = float(input ("enter  first  side of  the  triangle "))
b =float(input("entre   second  side of  the triangle "))
c =float(input("enter   third  side of  the triangle "))
s=0
if(a+b>=c or a+c>=b or  b+c>=a):
    print("triangle is possible ")
    s=(a+b+c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("area of the trangle is " , area)
else :
     print("triangle  is  not  possible ")

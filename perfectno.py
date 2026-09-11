
import math  
num = int(input("Enter a perfect  number "))
i=1
while(i<=num):
    sum = 0
    if(num % i == 0):
        sum = sum+i
    i+=1
    
if(sum == num):
    print("perfect number is ",sum,num)



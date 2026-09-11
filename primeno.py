num = int(input("enter a prime  number"))
i=1
count=0
while(i<=num):
    num %i==0
    count+=1
    i+=1
if(count==2):
    print(num,"is  not a prime number ")
else:
    print(num,"is a prime number ")
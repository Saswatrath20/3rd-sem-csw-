x = int(input("Enter  how many number  you want  to enter "))
a = int (input("Enter a number "))
big=a
small=a
i=1
while(i<=x-1):
     n = int(input( ))
if(n>big):
    big=n
if(n<small):
    small=n
    i+=1
print("Biggest number is ", big)
print("Smallest number is ", small)
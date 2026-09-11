n = int(input ("Enter a number"))
r=0
s =" "
while (n !=0):
    r= n%2
    n=n//2
    s=str(r)+s
print(s)
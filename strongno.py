def is_strong_number(num):
    sum=0
    temp=num
    while(num>0):
        digit =num%10
        fact=1
        while(digit>=1):
            fact= fact*digit
            digit -= 1
        sum +=fact
        num //=10
        if(sum == temp):
            return True
    return False

print("Enter a number to check if it is a strong number  or not")
num =int(input())
if is_strong_number(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")
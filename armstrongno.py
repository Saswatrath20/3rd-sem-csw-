from unicodedata import digit
def is_armstrong_no(num):
    sum =0
    temp =num
    count=0
    while(num>0):
        digit =num%10
        count +=1
        num /=10
        sum+=digit **count
        if(sum == temp):
            return True
    return False

print("Entera number to check if it is an  armstrong number or not ")
num =int(input())
if is_armstrong_no(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
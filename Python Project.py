#Project-11: In this project you have to enter a range[A,B] and systemwill randomly pick any number from your give range and check the status of the number. {odd or even, prime or composite and positive or negative}


import random

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

#System will generate a random integer from the range.
num=random.randint(a,b)
print("Range= [%d,%d]"%(a,b))
print("Random Number =",num)
#Program to check a number is positive or negative.
if num>0:
    print(num,"is a positive number")
elif num==0:
    print("0 is neither positive nor negative")
else:
    print(num,"is a negative number")

    
#Program to check a number is even or odd.
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

    
#Program to check Prime Number or Composite Number.
#Prime Numbers are greater than 1.
if num>1:
    count=0
    i=1
    while (i<=num):
        if (num%i==0):
            count+=1
        i+=1
    if (count==2):
        print(num,"is a Prime Number")
    else:
        print(num,"is a Composite Number")
else:
    print(num,"is neither prime nor composite")

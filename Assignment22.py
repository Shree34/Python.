# write a python script to calculate sum of first n natural numbers.
s=0
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    s+=e
print("Sum of first",n,"natural numbers is:",s)

# write a python scrip to calculate sum of squares of first N natural numbers.
s=0
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    s+=e**2
print("Sum of squares of first",n,"natural numbers is:",s)

# write a python script to calculate sum of squares of first N natural numbers.
s=0
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    s+=e**3
# write a python script to calculate sum of first N odd natural numbers.
s=0
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    s+=2*e-1
print("Sum of first",n,"odd natural numbers is:",s)


# write a python script to calculate sum of first n even natural numbers.
s=0
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    s+=2*e
print("Sum of first",n,"even natural numbers is:",s)

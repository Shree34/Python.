# print the first n natural numbers using range from user.
a=int(input('Enter a number'))
r1=range(1,a+1)
for e in r1:
    print(e, end=' ')

# print the squares of first n natural numbers using range from user.

for e in range(1,int(input('Enter a number:'))+1):
    print(e**2, end=' ')

# write a program to print first even natural numbers in reverse order.
n=int(input('Enter a number:'))
for e in range(n*2,(1),-2):
    print(e, end=' ')

# write a program to calculate sum of first n multiples of x.
n=int(input('Enter a number:'))
x=int(input('Enter a second number:'))
s=0
for e in range(1,(n+1)):
    s=s+x*e
    print('Sum is ',s)




 
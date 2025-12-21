
# write a python script to print the first 10 mutiples of 5.
for s in range(1,11):
    print(s*5, sep=' ')

# write a python script to print first 10 multiples of N.
a=int(input('Enter a number:'))
for s in range(1,11):
    print(s*a, sep=" ")

# Write a python script to frint first M multiples of N.
s=int(input('enter a number'))
for a in range(1,int(input('Enter a number'))+1):
    print(a*s,end=' ')


# Write a python scrip to print the first 19 multiples of N in reverse order.
s=int(input('enter a number'))
for a in range(10,0,-1):
    print(a*s,end=' ')


# Write a python script to print tabled of user's choice.
for x in range(1,11):
    print('{}*{}={}'.format(s,x,s*x))
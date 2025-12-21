# Write a python script to print first N even natural numbers. 
n=int(input('Enter a mnumber :'))
i=1
while i<=n:
    print(2*i, end=" ")
    i+=1

# Write a python script to print first N even natural numbers in reverse order. 
n=int(input('Enter a mnumber :'))
while n:
    print(2*n, end=" ")
    n-=1

# write a python script to print first n naturam numbers squares.
s=int(input('Enter a numbet: '))
i=1
while i<=s:
    print(i**2, end=" ")
    i+=1

# write a python script to print first n naturam numbers cube.
s=int(input('Enter a numbet: '))
i=1
while i<=s:
    print(i**3, end=" ")
    i+=1

# write a python script to print first 10 multiples of N.
s=int(input('Enter a numbet: '))
i=1
while i<=s:
    print(i*s, end=" ")
    i+=1
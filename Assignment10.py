# write a python to remove the last digit from a given number.(for ex, if user enter 2453 the o/p should be 253)
s=int(input('Enter a number : '))
k= s//10
print(k)

# write a python script to get the last digit from a given number.( for example, if use enters 2039 then your outuput should be 9 )
x=int(input('Enter a number : '))
r=x%10
print('Last result is ',r) 

# Write a python script to swap data of two variables.
print('Enter two numbers :')
a,b=int(input()),int(input())
print(f'a={a} b={b}')

a,b=b,a
print(f'swap numbers  a={a} b={b}')  

# write a python script which takes a three digit number from the user and displas only its first digit.
print('Enter a three digit number')
u=int(input())
a= u//100
print('first digit is',a)



# write a python script which takes a three digit number from the user and print the middle digit.
print('Enter a three digit number')
u=int(input())
a= u//10%10
print('middle digit is',a)

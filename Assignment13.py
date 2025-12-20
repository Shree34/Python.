# write a python script to check whether a given number is three digit or not. 
a=int(input('Enter a number: '))
if 999>=a>=100:
    print("Three digit number")
else :
    print('Not a thre digit Number')    

# Check whether a given number is positive, negative or zero.
a=int(input('Enter a number'))
if 0<a :
    print('positive Number ')
elif a==0:
    print('This is a zero ')
else :
    print('This is a negative number')

# Write a python script to chek whether a given quadratic equation has two real and distinct roots, rea and equal roots or imaginary roots.
# quadratic eqn (ax**2+bx+c=0) (b**2-4ac>0 real and distinct) (b**2-4ac=0 real and equal) (b**2-4ac<0 imaginary roots)
print('Enter values of a,b and c')
a,b,c=int(input()),int(input()),int(input())
d= (b**2-4*a*c)
if d>0 :
    print('This is real and distinct roots')
elif d==0:
    print('This is real and equal roots ')
else:
    print('this is imaginary roots.')

# Write a python script to chechk whether a given year ia a leap year or not.
# centuary year and non centuary years.

y=int(input('Enter a year :'))
if y%100==0:
    if y%4==0:
        print('This is a leap year')
    else:
        print('This is not a leap year')

else: 
    if y%4==0:
        print('This is a leap year.')
    else:
        print('This is not a leap year')

# write a python script to print greater among three numbers. print number only once even if the numbers are the same.

print('Enter three numbers')
a,b,c= int(input()),int(input()),int(input())
if a>b:
    print(a if a>c else c)
else:
    print(b if b> c else c)
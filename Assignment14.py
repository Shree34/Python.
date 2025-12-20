# write a python script to check whether a given number is a three digit number or not.
n=int(input('Enter a number: '))
match n : 
    case n if 1000>n>99:
        print('Three digit number')
    case n :
        print('Not a three digit number ')

# write a python script to check whether a given number is positive, negative or zero.
a=int(input('Enter a number : '))
match a:
    case a if a>0:
        print('The number is positive')
    case a if a<0:
        print('The number is negative')
    case a if a==0:
        print('The number is zero')

# write a python script to make a menu driven program in which user has to choose one of the option from given options 1) Odd-Even 2)positive 3)Simple intrest and 4) find roots of quadratic equation. match and execte appropriate code on use selection.
print('1. Odd Even ')
print('2) positive and nonpositive')
print('3) Simple intrest ')
print('4) Roots of quadratic equation')

s=int(input('Enter your choise :'))
match s:
    case 1:
        r=int(input('Enter a number :'))
        print('Even number'if r%2==0 else 'Odd number')
    case 2:
        s=int(input('Ente a number :'))
        print('positive number'if s>0 else 'Non positive number')
    case 3:
        print('Enter p,r and t for simple intrest')
        p,r,t=int(input('p=')),float(input('r=')),int(input('t='))
        si=p*r*t/100
        print('simple intrest is',si)
    case 4:
        print('Quadratic qurations values a,b,c')
        a,b,c= int(input()),int(input()),int(input())
        r1=(-b+(b*b-4*a*c)**0.5)/2*a
        r2=(-b-(b*b-4*a*c)**0.5)/2*a
        print('The two roots are',r1,'and',r2)
    case _:
        print('Invalid choice ')

# Write a pytho script to take one data from user and evaluate the type of data.if the date is of inttype then print Monday, if the data is of float type then print Tuesday, if the data is of complex type then print wednesday, if the data is of type bool then print Thursday.
x=eval(input('Enter a data :'))
print(type(x))
match x:
    case x if type(x) == int:
        print('Monday')
    case x if type(x) == float:
        print('Tuesday')
    case x if  type(x) == bool:
        print('Wednesdayy')
    case X if type(x)== complex:
        print('Thursday')
    case _:
        print('invalid data')

# Find a python script to take a string from user. if the string is a part of 'Shrinat' then print'One',if string is part of 'prashant' the print"Two'. if the string is part of "Agre" then print'Three'.
z=input('Enter a string: ')
match z:
    case z if z in 'Shrinath':
        print('One')
    case z if z in 'Prashant':
        print('Two')
    case z if z in 'Agre':
        print('Three')
    case _:
        print('Have a good day!')


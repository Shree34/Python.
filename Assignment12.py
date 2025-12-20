# wrilte a python script to check whether a given number is positive or non positive.
a=int(input('Enter a number: '))
if a > 0:
    print('positeve number')
else:
    print('Non positeve')

# write a python scrip to check whether a given number is divisible by 5 or not
b=int(input('Enter a number : '))
if b%5==0 :
    print('This number is divisible by 5')
else:
    print('This number is not divisibles by 5')

# wite a python script to check whether a given number is even or odd.
c=int(input('Enter a number : '))
if c%2==0 :
    print('This number is Even number')
else:
    print('This number is Odd number')

# write a python script to print greater between tow numbers. print number only once even if the numbers are the same.
print('Enter two numbers')
d=int(input())
e=int(input())
if d>e:
    print("The greater number is",d)
else:
    print('The greater number is',e)

# write a python script to print two given words in dictonary order.
w1= input('Enter first word : ')
w2= input(' Enter second word :')
if w1<w2 :
    print(w1,w2, sep="\n")
else:
    print(w2,w1, sep="\n")
# write a script to calculate simple intrest.
print('Enter principle,rate and time ')
principle=int(input())
rate=float(input())
time=int(input())
simple_intrest= principle*rate*time/100
print('The siple intrest is',simple_intrest)

# calculate the area of the rectangle enter area from user.
print('Enter the length and breadth')
l=int(input('Length: '))
b=int(input('Bredth: '))
area=l*b
print("The area of rectangle is",area)

# Calculate the average of three numbers entred by the user.
print('Enter three numbers :')
x=int(input())
y=int(input())
z=int(input())
average=(x+y+z)/3
print('The average of 3 numbers is',average)

# write a python script for calculating the volume of cubid.
print('Enter the lenth,breadth and height of cube')
length,breadth,height=int(input('length :')),int(input('breadth :')),int(input('height :'))
volume=length*breadth*height
print('The volume of cube is',volume)

# write a python script take two numbers from user( x and y),now calculate x power y and display the result.
print('Enter two numbers')
x=int(input('X :'))
y=int(input('y :'))
print(f'The power of {x} is {x**y}')
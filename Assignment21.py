# write a python script to print first N even natural numbers.
N = int(input("Enter a number N: "))
for e in range(1, N + 1):
    print(2 * e, end=' ')

# write a python script to print first N odd natural numbers.
N = int(input("Enter a number N: "))
for e in range(1,N+1):
    print(2*e-1, end=' ')

# write a python script to print squares of first N natural numbers.
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    print(e**2, end=' ')

# write a python script to print cube s of first N natural numbers.
n=int(input("Enter a number N: "))
for e in range(1,n+1):
    print(e**3, end=' ')

# write a python script to print to display all primr numbers within a range # range start = 15 end= 45.
start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))
for x in range(start, end + 1):
    if x > 1:
        for i in range(2, int(x**0.5) + 1):
            if (x % i) == 0:
                break
        else:
            print(x, end=' ')

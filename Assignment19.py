# write a python code to print each character of a string with its corresponding Unicode.
s= input('enter a string')
for e in s:
    print(e,ord(e))

# write a pytthon script to print only vowels of the given string.
s=input('Enter a string: ')
v='aeiouAEIOU'
for e in s:
    if e in v:
        print(e)

# write a python script to count occurrence of speaces in a given string.
s= input( 'Enter a string :')
count=0
for e in s:
    if e==' ':
        count+=1
print('Count=',count)
    

# write a python script to print unique digits of a given integer.
s=('Enter a number :')
i=0
for e in s:
    if s.index(e)== i:
        print(e,end=' ')
        i+=1

# Write a Python script to count number of digita in a given number.
S=input('Enter a number:')
count=0
for e in s:
    count += 1
print('Total digits=',count)

#eligible for vote or not

age=int(input("enter your age"))
if(age>=18):
	print("eligible for voting ")
else:
	print("not eligible for voting")
	
	
	
#number is even or odd

num=int(input("enter the number"))
if(num%2==0):
	print("number is even")
else:
	print("number is odd")
	
	
	
	
#prime number or not 

n=int(input('enter the number'))
j=0
for i in range(2,n+1):
	
	if n%i==0:
		j+=1
	else:
		pass
if j==1:
	print(f'{n} is prime number')
else:
	print('not a prime number')
	



#number is positive or not 

a=int(input("enter the number"))
if(a>0):
	print("number is positive")
else:
	print("number is negative")
	
	
	
	
#quardatic equation

a=int(input('enter x**2 coefficent'))
b=int(input('enter x coefficent'))
c=int(input('enter the constant'))
d=b**2-(4*a*c)
if d==0:
	print(f'roots are equal they are : {(-b)/(2*a)}')
elif( d>0):
	print(f'roots are real and distent are : {(-b+(d**0.5))/(2*a)},{(-b-(d**0.5))/(2*a)}')
else:
    
    y=x=(-b)/(2*a)
    print(f'roots are imaginary they are {x}+{-(d/(2*a))}i and {y}-{-(d/(2*a))}i')
    
    
    
#number is positive or negative or zero

n=int(input("enter the number"))
if(n>0):
	print("number is positive")
elif(n==0):
	print("zero")
else:
	print("number is negative")
	
	
	
#print the number in words

a={1:"one",2:"two",3:"three",4:"four",5:"five"}
x=[1,2,3,4,5]
n=int(input("enter the number between (1 to 5)"))
if(n in x):
	print("number in words")
else:
	print("number not in words")
	

#vowel or consonant

n=str(input("enter the char from(a-z)"))
if n in ["a","e","i","o","u"]:
	print(" vowel")
else:
	print("consonant")
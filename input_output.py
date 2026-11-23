
#string 
name=input("enter your name")
print("name",name)
#int
num=input("enter a number")
num1=int(num)
print(num)
print(type(num1))
#intput_int
age=int(input("enter a number"))
print(age)
#float
num=input(" enter the number")
num1=float(num)
print(num1)
#input_float
num=float(input(" enter a number"))
print(num)
#program
name=input("enter the name")
age=int(input(" enter the age"))
print(" the name is "+ name + "! the age is",age,)


# used sep,end
a= int(input("enter  a"))
b=int(input("enter b "))
print(a, b,sep="," ,end="ended here")

# example program1

name= input("")
print("Hello", name,sep=",",end= "!")

# example program 2

num=int(input("enter a number"))
print("You entered:",num,sep="")

# example 3

num= float(input(" enter a num"))
print("Value of Pi:",num,sep="")

# example 4

num= input("")
a,b,c=num.split()
sum=int(a)+int(b)+int(c)
print(sum)

# example 5

vin=int(input("enter a number"))
print("Coutdown: 5,4,3,2,1",end="Blast Off!")


# example 6
num=int(input("enter a number"))
num1=int(input("enter a number"))
print("Addition:",num+num1)
print("Subtraction:",num-num1)
print("multiplication:",num*num1)
print("division:",num/num1)

# example 7

x=int(input())
y=int(input())
print(x>y,x<y,x==y,x!=y)


# example 8

vin=input("enter name and age")
name,age=vin.split(",")
print(name,age)

# example 9

x,y=input().split(",")
a=int(x)
b=int(y)
print(a+b,a-b,a*b,a/b)

#example 10

x,y= input().split(",")
a=int(x)
b=int(y)
print(x>y,x<y,x>=y,x<=y,x!=y)

# example 11

name=input()
print(" you entered:",name)

# example 12

x,y=input().split(",")
print(x and y)
print(x or y)
print(not x)

# example 13 f string
x,y=input().split(",")
print(f"Name:{x},Age:{y} years")

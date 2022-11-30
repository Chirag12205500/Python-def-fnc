def add(x,y):  #function defination
    print("Sum: ",x+y)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
add(a,b)#function call

def sub():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print("Subtraction: ",num1-num2)
sub()

def multiplication():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    c = num1*num2
    return(c)


result = multiplication()
print("Multiplication answer: ",result)


def calc():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    mul = num1*num2
    add = num1+num2
    sub = num1-num2
    return(mul,add,sub)
a,b,c = calc()
print("Multiplication answer: " ,a,"Addition :",b, "subtraction :",c)

def abc():
    """This is a comment inside the function"""
    a = 10
    return
print(abc.__doc__)
b = abc()
print("b : ", b)

a = 10 #global
def abc():
    global a  #local
    print("a = ",a)
print("Value of A outside function: ",a)
abc()

def display(name,age):
    print("name is=",name , "age is=",age)
display('j',25)
display(40,'s')
display("john",6)
display(age=34,name="abc")

def display(a,b=10,c=20):
    print("a=", a, "b=", b, "c=", c)
display(15,67)

def add(a,b,c=10):
    print("a=", a, "b=", b, "c=", c)
add(10,10)

a=100
def demo():
    a=10
    print(a)
demo()
print(a)

a=20
def d():
    global a
    a=30
    print("value of a in fn", a)
d()
print("value of a in fn", a)

def add(x,y): #addition
    return (round (x+y,2))

def sub(x,y): #subtraction
    return (round (x-y,2))

def mul(x,y): #multiplication
    return (round (x*y,2))

def division(x,y): #division
    return (round (x/y,2))

def modulus(x,y): #modulus
    return (round (x%y,2))
print("please select the operator:\n"
      "1.addition\n"
      "2.subtraction\n"
      "3.multiplication\n" 
      "4.division\n"
      "5.modulus\n")#print the operations
operator=int(input("Select the operation to be performed(1,2,3,4,5):"))
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

if operator == 1:
    print(num1,"+", num2, "=",add(num1, num2))
elif operator == 2:
    print(num1,"-", num2, "=",sub(num1, num2))
elif operator == 3:
    print(num1,"*", num2, "=",mul(num1,num2))
elif operator == 4:
    print(num1,"/",num2, "=",division(num1,num2))
elif operator == 5:
    print(num1,"%",num2,"=",modulus(num1,num2))
else:
    print("enter valid operation")

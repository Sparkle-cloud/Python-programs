#Function to compute GCD of two numbers.
def GCD(Number1, Number2):
    rem = Number1 % Number2
    while(rem != 0):
        Number1 = Number2
        Number2 = rem
        rem = Number1%Number2
    return Number2
    
Number1 = int(input("Enter the First Number:"))
Number2 = int(input("Enter the second Number:"))

output = GCD(Number1,Number2)
print("The GCD of the numbers = ", output)

#Euclid's method of finding GCD
print("This is Euclid's method")
def get_gc(a,b):
    while b:
        a,b=b,a%b
    return a

a = int(input("Enter the First Number:"))
b = int(input("Enter the second Number:"))
result = get_gc(a,b)
print("The GCD of the numbers = ",result)


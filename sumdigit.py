#Function to add the digits of the input number.
def add_digits(x):
    sumval=0
    strx=str(x)
    for i in strx:
        sumval += int(i)
    return sumval

digit=int(input("Enter a number: "))
print("Sum of the digits = ",add_digits(digit))



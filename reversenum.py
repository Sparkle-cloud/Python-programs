#Function to reverse the input number
def reverse_number(x):
    strx=str(x)
    txtval=strx[::-1]
    return txtval

num=int(input("Enter a number:"))
print (reverse_number(num))

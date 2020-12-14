#Function to reverse input number and check whether palindrome or not.
def check_palindrome(x):
    strx=str(x)
    txtval=strx[::-1]
    if strx== txtval:
        return True
    else:
        return False


num=int(input("Enter a number: "))

#calling the function and checking if the condition is true.
resultval = check_palindrome(num)
if resultval == True:
    print ("Yes it is a palindrome")
else:
    print ("No it is not a palindrome")
    

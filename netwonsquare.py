#type-1
#function that finds the square root with precision
def get_sqrt(number,precision):
    sqroot= float(number)
    while abs(number - sqroot + sqroot)> precision:
        print ("squareroot of the number by newton's method =",sqroot)
        
        sqroot=(sqroot+number/sqroot)/2
        
    return sqroot

num=int(input("Enter a number to find square root: "))
precision=int(input("Enter the precision: "))
precision=precision*-10
sroot=get_sqrt(num,precision)

#type-2
print("\nAnother type of finding square root using newton's method\n")
#function to compute square root using newton's method
def newton_method(num):
    fnum=float(num)
    for i in range(500):
#formula to find squareroot = 0.5 * (X + (N / X)) 
        num=0.5*(num+fnum/num)
    return num

x=int(input("Enter a number to find square root: "))
squareroot=newton_method(x)
print ("squareroot of the number by newton's method =",squareroot)


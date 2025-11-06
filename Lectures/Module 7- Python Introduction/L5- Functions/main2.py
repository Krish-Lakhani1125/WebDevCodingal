#Factorial of a number using recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = int(input("Enter a Number"))

#check if the number is negative
if num < 0:
    print("Sorry, negative numbers do not have a factorial")
elif num == 0:
    print("The factorial of 0 is 1")
elif num == 1:
    print("The factorial of 1 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
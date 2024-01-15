num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))
add_total = num1 + num2

if (add_total % 2 == 0):
    print ("Sum: ", add_total)
    print ("The sum is an even number.")
else:
    print ("Sum: ", add_total)
    print ("The sum is an odd number.")
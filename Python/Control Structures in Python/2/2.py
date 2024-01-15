num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))
mult_total = num1 * num2

if (mult_total % 2 == 0):
    print ("Product: ", mult_total)
    print ("The product is an even number.")
else:
    print ("Product: ", mult_total)
    print ("The product is an odd number.")
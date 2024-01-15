#5
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
average = sum / num
print("Result: The sum of the numbers from 1 to", num, "is", sum, "and the average of all the numbers in the range is", average)

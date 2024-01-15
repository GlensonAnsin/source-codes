sum = 0
print ("All even numbers less than 100: ")
for i in range (2, 100, 2):
    sum += i
    if (i % 2 == 0):
        print (i)
print ()
print ("-The sum of all even numbers less than 100 is", sum)
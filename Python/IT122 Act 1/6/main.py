#6
terms = int(input("Enter number of terms: "))
a, b = 0, 1
print(a, end=' ')
print(b, end=' ')
for i in range(2, terms):
    c = a + b
    print(c, end=' ')
    a, b = b, c
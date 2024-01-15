n = int(input("How many numbers you want to input?: "))
list_nums = []
length = len(list_nums)

for i in range(n):
    nums = int(input("Enter the numbers: "))
    list_nums.append(nums)
print("List of numbers:", list_nums)
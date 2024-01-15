stack = []  # initialize an empty list to represent the stack

# ask the user for the items to push onto the stack
num_items = int(input("Enter the number of items to push onto the stack: "))
for i in range(num_items):
    item = input("Enter an item to push onto the stack: ")
    stack.append(item)

# print the current state of the stack
print("Current stack:", stack)

# ask the user for the number of items to pop off the stack
num_pops = int(input("Enter the number of items to pop off the stack: "))
for i in range(num_pops):
    if len(stack) == 0:  # if the stack is empty
        print("Stack is empty. Cannot pop an item.")
        break
    else:  # if the stack is not empty
        item = stack.pop()  # remove the last item from the list
        print("Item", item, "has been popped from the stack.")

# print the final state of the stack
print("Final stack:", stack)
print("Submitted by: Bacolanta, Celeste Beatrix L. of IT1R14\n")

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def print_list(self):
        if self.head is None:
            print("The stack is empty.")
        else:
            current = self.head
            print("Current List:")
            while current is not None:
                items = current.data
                current = current.next
                yield items
            print()

myInstance = Stack()

while True:
    print("Choose an operation to use")
    print(" [1] Push\n", "[2] Pop\n", "[3] Stop\n")
    chosen_operation = int(input("Enter the operation of your choice: "))
    print()

    if chosen_operation == 1:
          myInstance.push(int(input("Enter a number to push: ")))
    elif chosen_operation == 2:
        popped = myInstance.pop()
        print("Popped Value: ", int(popped))
    elif chosen_operation == 3:
        print("Program Terminated.")
        break

    for items in myInstance.print_list():
        print(items)
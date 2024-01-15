#Name: Glenson M. Ansin
#Section: IT1R13
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self):
        if self.head is None:
            print("Linked List is empty.")
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def remove_item(self):
        if self.head is None:
            print("Linked List is already empty.")
        self.head = self.head.next
        self.count -= 1


items = Singly_linked_list()
items.append_item("PHP")
items.append_item("Python")
items.append_item("C#")
items.append_item("C++")
items.append_item("Java")

print("Current Linked List:\n")
for val in items.iterate_item():
    print(val)
print("\nHead: ", items.head.data)
print("Tail: ", items.tail.data)
print("=" * 40)

while True:
    print('''Choose your options below:
(a) Add Items
(b) Delete an item
(c) Terminate''')
    print("=" * 40)
    option = input("Input Here: ")

    if option == "a":
        items.append_item(input("\nItem to be added: "))
    elif option == "b":
        items.remove_item()
    elif option == "c":
        print("\nTerminated, Thank you!")

        break
    else:
        print("\nInvalid input, please input correctly.")

    print("=" * 40)
    print("Current Linked List:\n")
    for val in items.iterate_item():
        print(val)
    print("\nHead: ", items.head.data)
    print("Tail: ", items.tail.data)
    print("=" * 40)
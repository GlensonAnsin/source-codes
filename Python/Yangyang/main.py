#objective here 1,3

#Instructions
#Debug the code
#Explain the output

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None

  def add_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node

  def remove_node(self, data):
    if self.head is None:
      return

    if self.head.data == data:
      self.head = self.head.next
    else:
      current = self.head
      while current.next is not None:
        if current.next.data == data:
          current.next = current.next.next
          return
        current = current.next

  def print_list(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next
    print()

llist = Linkedlist()
llist.add_node(1)
llist.add_node(2)
llist.add_node(3)
llist.remove_node(2)
llist.print_list()
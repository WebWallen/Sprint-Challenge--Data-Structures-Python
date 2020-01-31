class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # Assign previous to None (will need to modify its pointers later)
    previous = None
    # Assign current to the head
    current = self.head
    # While current node has a value...
    while current is not None:
      # Add .next_node to current and assign to "next" (starts loop)
      next = current.next_node # Temp variable to store next (A --> B)
      # Assign previous to current.next_node (flips order for each node)
      current.next_node = previous # Flip order to B --> A
      # Assign current to previous (first step to restart loop)
      previous = current
      # Assign next to current (second step to restart loop)
      current = next
    # Assign previous to self.head (flips head position to last element)
    self.head = previous
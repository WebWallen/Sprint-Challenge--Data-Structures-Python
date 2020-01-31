from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.head = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If there's no head (empty list)...
        if not self.head:
            # Create new node, assign to self.head, and pass in item
            self.storage.add_to_head(item)
            # Assign head to next pointer (circles around self)
            self.head.next = self.head
        else:
            if self.capacity:
                self.storage.remove_from_tail()
                # Assign new node to variable and pass in item
            new_node = ListNode(item)
            self.storage.add_to_tail(new_node)
            # Assign self.head to current_node
            current_node = self.head
            # While the next node isn't the head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        return list_buffer_contents

buffer = RingBuffer(5)
buffer.append('a')
print(buffer)

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class RingBuffer:
    def __init__(self, capacity):
        # Maximum amount of nodes
        self.capacity = capacity
        # Current oldest node
        self.current = None
        # Storage object
        self.storage = DoublyLinkedList()

    # "Append puts it on the end"
    def append(self, item):
        # If the length of self.storage is less than capacity
        if len(self.storage) < self.capacity:
            # Add the input item to tail
            self.storage.add_to_tail(item)
            # Assign storage head to current (rearrange pointers to equal circle)
            self.current = self.storage.head
        # If the length of self.storage equals capacity
        elif len(self.storage) == self.capacity:
            # Insert the item before current node (now head)
            self.current.insert_before(item)
            # Increase storage length by 1
            self.storage.length += 1
            # If current equals the storage head...
            if self.current == self.storage.head:
                # Call move_to_front on storage and pass in current node's previous pointer
                self.storage.move_to_front(self.current.prev)
            # If current equals the storage tail...
            if self.current == self.storage.tail:
                # Assign storage head to current (rearranges pointer into a circle)
                self.current = self.storage.head
                # Delete the tail from storage to make room for the new element
                self.storage.delete(self.storage.tail)
            else:
                # Assign .next pointer to self.current
                self.current = self.current.next
                # Call delete on storage and pass in current's previous pointer
                self.storage.delete(self.current.prev)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass

import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

tree = BinarySearchTree('New')

for name_1 in names_1:
    tree.insert(name_1)
    
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)

# This method takes 0.19 seconds, which isn't bad considering input volume
# According to GeeksForGeeks, the time complexity is O(h), or height of the tree
# This would classify as O(n) due to the amount of inputs that must be searched one-at-a-time

duplicates = list(set(names_1).intersection(set(names_2)))

# The built-in Python sets method only takes 0.001 seconds, which is a huge improvement
# According to GeeksForGeeks, the time complexity is a factor of the added length of the sets you're comparing
# Only has to run once, so I'm assuming this qualifies as O(1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# Queues --> FIFO Data Structure --> First-In-First-Out.
# People standing in line at a bank
# First customer that comes into the bank is the first customer
# that gets serve and gets out of the bank
from collections import deque
queue_data_structure = [1, 2, 3]
queue_data_structure.append(4)
queue_data_structure.append(5)
print(queue_data_structure)
first_customer = queue_data_structure.pop(0)
print(first_customer)
print(queue_data_structure)
second_customer = queue_data_structure.pop(0)
print(second_customer)
print(queue_data_structure)

# Efficient implementation of queue
queue = deque([])
# we can add item onto the queue using the append() function
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
# we can remove item from the queue using the popleft() function
queue.popleft()
print(queue)
# Also, we can check if a queue is empty using 'not'.
# Similar to how we checked if a stack is empty using Python's built-in
# list data type
if not queue:
    print("empty")

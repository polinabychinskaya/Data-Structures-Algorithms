# List implementation

stock_price_queue = []
# We insert at index 0, because with 
# this method every subsequent value 
# displaces the intial one
stock_price_queue.insert(0, 131)
stock_price_queue.insert(0, 123)
stock_price_queue.insert(0, 165)
print(stock_price_queue)
print(stock_price_queue.pop())
# However, using a dynamic list is not memory 
# efficient, as when the capacity exceed, 
# then it needs more space, as it has 
# to double the previous capacity and copy all the elmnts

# Import deque implemetation
from collections import deque
q = deque()
# As we use .append to populate stack, 
# we use .appendleft for the queue
q.appendleft(5)
q.appendleft(8)
q.appendleft(23)
print(q.pop())

# Class implementation
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
queue = Queue()
queue.enqueue(5)
queue.enqueue(34)
print(queue.buffer)

import threading
import time

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        if food_order_queue.is_empty():
            print('All orders are served')
            break
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)


orders = ['pizza','coffee','pasta','beef','burger']
t1 = threading.Thread(target=place_orders, args=(orders))
t2 = threading.Thread(target=serve_orders)

t1.start()
t2.start()
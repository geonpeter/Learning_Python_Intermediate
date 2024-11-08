from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

q = Queue() #FIFO
q.put("Geon")
q.put("Sherin")
q.put("Miriam")
print("First In First Out")

while not q.empty():
    print(q.get())
    
print("\n")         
print("Last In First Out")
q = LifoQueue() # LIFO
q.put("Geon")
q.put("Sherin")
q.put("Miriam")
while not q.empty():
    print(q.get())
    
    
print("\n")    
print("Priority Queue")

q=PriorityQueue() #Priority Queue
q.put((3,"Geon"))
q.put((1,"Sherin"))
q.put((2,"Miriam"))
while not q.empty():
    print(q.get()[1])
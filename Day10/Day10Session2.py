
# QUEUE

'''
import time

myQueue = []
print("Queue implementation")
print()
size = int(input("Enter the size of the Queue: "))

for i in range(size):
     a = int(input("Add Item in Queue :"))
     myQueue.append(a)
else:
     print("Queue is full")
     print("Queue ELements are=",myQueue)

for i in range(size):
     time.sleep(3)
     j=0
     print(myQueue.pop(j),":Remove element from Queue")
else:
     print("Queue is empty")

for i in range(size):
     time.sleep(3)
     j=0
     print(myQueue.pop(j),":Remove element from Queue")
else:
     print("Queue is Empty")
     print("Queue Elements are=",myQueue)
'''


# LINKED LIST


class Nodes:
     def __init__(self,item):
          self.item = item
          self.next = None

class LinkedList:
     def __init__(self):
          self.head=None

linked_list = LinkedList()

linked_list.head = Nodes(1)
second= Nodes(2)
third = Nodes(3)

linked_list.head.next = second
second.next = third

while linked_list.head != None:
     print(linked_list.head.item,end="")
     linked_list.head = linked_list.head.next




'''

-----Python RoadMap (GOLDEN 5 MONTH)------

Basic - 150 QUESTION
DSA - 450 Question

MARCH -> HACKERRANK 5 QUESTION DAILY
APRIL,MAY,JUNE -> DSA 
         1. DSA Sheet(Love Babbar, Apna College[IMP], Striver(Advance Level))
         2. Apna College -> All solution

JULY -> OS, DBMS, OOPS

NOTES : --
1) 15 MIN REVISION EVERYDAY
2) NOTES - LOGIC CODES

'''
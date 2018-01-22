"""
@channel I'm going to be assigning a bunch of problems using 
linked lists for the week after thanksgiving, so you're challenge 
this week is to build an implementation of a singly linked list.  
Your data structure should implement the following methods:
1. insert(index, data) : insert a new node at the given index
2. pop(index) : remove the node at the given index and return its 
value
3. print_list(): Traverse the list and print all its values
4. reverse(): Reverse the list
Bonus points for making your linked list implement common container 
behavior like testing whether it contains an item, making it easily 
iterable, etc.  

I'll assign new problems next Monday and we'll talk about your 
implementations and a problem or two at the meeting next week.
"""

import sys 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            ### do not change above this line 

    def insert(self,head,data): 
    	node = Node(data) 
    	if head is None:
    		head = node
    	else:
    		current = head
    		while (current.next !=None):
    			current = current.next
    		current.next = Node(data)
    	return(head)

    def pop(self,head,data): 
    	node = Node(data)
    	if head is None:
    		head = node
    	else:
    		current = head



T=int(sys.argv[1])
mylist= Solution() 
head=None
for i in range(T):
    data=int(sys.argv[1])
    head=mylist.insert(head,data)    
mylist.display(head); 


"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

temp = Node(sys.argv[1])
print(temp.getData())
"""
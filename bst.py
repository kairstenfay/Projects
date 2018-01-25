class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

    def get(self):
        return self.data

class Solution:
    def __init__(self):
        self.root=None

    def _set_root(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root==None:
            self._set_root(data)
        else:
            self._insert(self.root,data)

    def _insert(self, current_node, data):
        if data <= current_node.data:
            if current_node.left:
                self._insert(current_node.left,data)
            else:
                current_node.left = Node(data)
        elif data > current_node.data:
            if current_node.right:
                self._insert(current_node.right, data)
            else:
                current_node.right = Node(data)

    def to_list(self):
        queue = []
        sorted_list = []
        if self.root is None:
            return sorted_list
        else:
            if self.root.left is not None:
                #queue.append(self.root.data)
                sorted_list.append(self._sort(self.root.left, sorted_list, queue))

            if self.root.right is not None:
                queue.append(self.root.data)
                sorted_list.append(self._sort(self.root.right, sorted_list, queue))
            return sorted_list, queue
            #current_node = self.root
            #previous_node = current_node
            #f current_node.left is not None:
            #    current_node = current_node.left
            #
            #self._check_left(current_node.left)
    def _sort(self, root, sorted_list, queue):
        if root.left is None:
            return root.data
        if root.left is not None:
            queue.append(root.data)
            return self._sort(root.left, sorted_list, queue)

    # def _check_left(self, current_node):
    #     if current_node.left is not None:
    #         previous_node = current_node
    #         current_node = current_node.left
    #     elif current_node.left is None:
    #         return current_node

    # def _check_right(self):
    #     if current_node.right is not None:
    #         pass 

    def get_height(self):
        if self.root is None: 
            return 0
        else:
            return max(self._height(self.root.left), self._height(self.root.right))

    def _height(self, root):
        if root is None: 
            return 0
        else:
            return max(self._height(root.left), self._height(root.right)) + 1

    def find(self, data):
        return self._find_node(self.root, data)

    def _find_node(self, current_node, data):
        if(current_node is None):
            return False
        elif(data == current_node.data):
            return True
        elif(data < current_node.data):
            return self._find_node(current_node.left, data)
        else:
            return self._find_node(current_node.right, data)


#T=int(input())
myTree=Solution()
#for i in range(T):
myTree.insert(3)
myTree.insert(5)
myTree.insert(2)
myTree.insert(1)
myTree.insert(4)
myTree.insert(6)
myTree.insert(7)
myTree.insert(8)


height=myTree.get_height()
#print(height)

myTree.find(1)
myTree.find(99)

myTree.to_list()


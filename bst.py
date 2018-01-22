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
    
    def get_height(self):
        if self.root is None:
            print("your tree is short")
            return 0
        elif self.root.left:
            return max(self._height(self.root.left), self._height(self.root.right)) + 1

    def _height(self, root):
        if self.root is None:
            print("your tree has no more children")
            return 0
        else:
            return max(self._height(self.root.left), self._height(self.root.right))
    """
    def get_tree_height(self,root):
        if self.root is None:
            return -1

        return max(self.get_tree_height(self.root.left), self.get_tree_height(self.root.right)) + 1
    """

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

        """
        if self.root:
            left = right = 0
            if self.root.left:
                print("yes")
                left = 1 + self.getHeight(self.root.left)
            if self.root.right:
                print("maybe")
                right = 1 + self.getHeight(self.root.right)
            height = max(left, right)
            return height
        else:
            print("error")
            """

#T=int(input())
myTree=Solution()
#for i in range(T):
myTree.insert(3)
myTree.insert(5)
myTree.insert(1)
myTree.insert(12)
myTree.insert(11)
myTree.insert(2)
myTree.insert(99)

height=myTree.get_height()
print(height)

#myTree.find(99)
#myTree.find(901)


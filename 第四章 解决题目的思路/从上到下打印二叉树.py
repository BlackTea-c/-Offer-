#逐层打印；从左到右

class Node():
    def __init__(self,item):
        self.item=item
        self.right=None
        self.left=None


class BinaryTree():
    def __init__(self):
        self.root=None


    def PrintFromToptoBottom(self):
        #队列
        if self.root==None:
            print('tree is empty')
            return
        queue=[]
        root=self.root
        queue.append(root)
        while root!=None:
         print(queue[0].item)
         if root.left!=None:
            queue.append(root.left)
         if root.right!=None:
            queue.append(root.right)
         queue.pop(0)
         if len(queue)==0:
             break
         root=queue[0]

tree=BinaryTree()
tree.root=Node(1)
tree.root.right=Node(2)
tree.root.left=Node(3)
tree.root.right.right=Node(4)
tree.PrintFromToptoBottom()
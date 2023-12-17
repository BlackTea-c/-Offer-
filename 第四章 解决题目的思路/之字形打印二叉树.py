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
        stack1=[]
        stack2=[]
        root=self.root
        stack1.append(root)
        sign=0 #0 左到右 1 右到左
        while stack1!=[] or stack2!=[]:
            if sign==0:
                for node in stack1:
                    if node.left!=None:
                     stack2.append(node.left)
                    if node.right!=None:
                     stack2.append(node.right)
                for i in range(len(stack1)):
                    print(stack1[-i].item,end=' ')
                print('')
                sign=1
                stack1=[]
            else:
                for node in stack2:
                    if node.right!=None:
                     stack1.append(node.right)
                    if node.left!=None:
                     stack1.append(node.left)
                for i in range(len(stack2)):
                    print(stack2[-i-1].item,end=' ')
                print('')
                sign=0
                stack2=[]


tree=BinaryTree()
tree.root=Node(1)
tree.root.right=Node(2)
tree.root.left=Node(3)
tree.root.left.right=Node(7)
tree.root.right.right=Node(4)
tree.root.right.left=Node(6)
tree.root.right.right.right=Node(5)
tree.PrintFromToptoBottom()
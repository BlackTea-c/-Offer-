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
        a=1 #表示当前层还没有打印的节点数
        b=0 #表示下一层节点的数目
        while root!=None:
         print(queue[0].item,end=' ')

         if root.left!=None:
            queue.append(root.left)
            b+=1
         if root.right!=None:
            queue.append(root.right)
            b+=1

         queue.pop(0)
         a-=1
         if len(queue)==0:
             break
         if a==0:
             print('')
             a=b
             b=0
         root=queue[0]

tree=BinaryTree()
tree.root=Node(1)
tree.root.right=Node(2)
tree.root.left=Node(3)
tree.root.left.right=Node(7)
tree.root.right.right=Node(4)
tree.root.right.left=Node(6)
tree.root.right.right.right=Node(5)
tree.PrintFromToptoBottom()
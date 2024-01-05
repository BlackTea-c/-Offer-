



class Node():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None


class Tree():
    def __init__(self):
        self.root=None



tree=Tree()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.left.left=Node(3)
tree.root.left.left.right=Node(4)
tree.root.right=Node(5)


list=[]
def Serialize(root): #递归吧~

    if root==None:
        return

    list.append(root.item)

    Serialize(root.left)

    if root.left==None:
        list.append('&')
    if root.right==None:
        list.append('&')

    Serialize(root.right)
Serialize(tree.root)
print(list)



#反向构建，即已知序列 构造二叉树


list=[1,2,4,'&','&','&',3,5,'&','&',6,'&','&']

def Serialize_reverse(list):


    def df():
        root_item=list.pop(0)
        if root_item=='&':
            return None
        else:
            node=Node(root_item)
            node.left=df()
            node.right=df()
        return node
    return df()
root=Serialize_reverse(list)
print(root.left.left.item)






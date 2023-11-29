#给定一个二叉树和其中一个节点，如何找出中序遍历序列的下一个节点？




#复习：重建二叉树,添加能指向父节点的指针
preorder=["a","b","d","e","h","i","c","f","g"]
midorder=["d","b","h","e","i","a","f","c","g"]

class Node():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
        self.father=None



class BinaryTree():

    def __init__(self):
        self.root=None


    def Rebuild(self,ps,pe,im,ie):

        if ps>pe:
            return None
        root = Node(preorder[ps])
        if ps==pe:
            return root


        root_index=midorder.index(preorder[ps])
        pm=root_index-im+ps

        root.left=self.Rebuild(ps+1,pm,im,root_index-1)

        root.right=self.Rebuild(pm+1,pe,root_index+1,ie)
        if root.left is not None:
           root.left.father=root
        if root.right is not None:
           root.right.father=root

        return root







Btree=BinaryTree()
Btree.root=Btree.Rebuild(0,len(preorder)-1,0,len(midorder)-1)

node_dict={}
def preorder( node):  # 前序遍历
    node_dict[node.item]=node
    if node.left != None:
        node1 = node.left
        preorder(node1)
    if node.right != None:
        node1 = node.right
        preorder(node1)


item=input("Which node's next do you want to find?")
preorder(Btree.root)
def find_next(item):
    node=node_dict[item]
    #如果节点有右子树，那么next就是其右子树的最左子节点
    if node.right is not None:
        nd=node.right
        while(nd.left is not None):
            nd=nd.left
        return nd.item
    #如果节点没有右子树，但是其是父节点的左子节点，那么next就是其父节点
    if node.right is None:
        if node.father.left==node:
            return node.father.item

        else:
            nd1=node.father
            while nd1 is not None:

                if nd1.father is not None:

                    if nd1.father.left==nd1:
                        break
                        return nd1.father.item
                    else:
                        nd1=nd1.father
                else:
                    return None
    #如果节点没有右子树且其为父子节点的右子节点，那么往上直到找到一个节点，该节点为它的父节点的左子节点，next即为其父节点；如果往上找的途中发现节点的父节点为None 则返回None



print(find_next(item))

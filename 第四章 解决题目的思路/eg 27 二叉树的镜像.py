

#输入一个二叉树，输出它的镜像
class node():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self):
        self.root=None



    def build(self,ps,pe,ms,me,data_pre,data_mid):
        if ps>pe:
            return None

        root=node(data_pre[ps])

        if ps==pe:
            return root


        root_index=data_mid.index(data_pre[ps])
        pm=root_index+ps-ms

        root.left=self.build(ps+1,pm,ms,root_index-1,data_pre,data_mid)

        root.right=self.build(pm+1,pe,root_index+1,me,data_pre,data_mid)

        return root




data=[1,2,4,7,3,5,6,8]#前序遍历
data1=[4,7,2,1,5,3,8,6]#中序遍历

tree=BinaryTree()
tree.root=tree.build(0,len(data)-1,0,len(data)-1,data,data1)

def MirrorRecursively(root):
    left_node=root.left
    root.left=root.right
    root.right=left_node
    if root.right!=None:
      MirrorRecursively(root.right)
    if root.left!=None:
      MirrorRecursively(root.left)

MirrorRecursively(tree.root)







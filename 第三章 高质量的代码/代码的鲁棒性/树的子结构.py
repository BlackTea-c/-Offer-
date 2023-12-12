
#输入两颗二叉树A，B 判断B是不是A的子结构


class Node():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self):
        self.root=None
    def build(self,pb, pe, ib, ie,data,data1):
        # (pb, pe)是当前前序遍历的起点和终点//起点pb则代表了root
        # (ib, ie)是当前中序遍历的起点和终点
        if pb > pe:
            # 递归出口
            return None
        root=Node(data[pb])
        if pb == pe:
            # 当前只有一个值, 自然就返回该节点本身
            return root
        # 找出根节点的值对应的中序遍历的下标, 利用valueToInorderIndex字典就能做到O(1)时间内找到中序下标
        # 以此作为分界点, 分成左右两个子问题解决即可
        im = data1.index(data[pb])
        # 由于子树节点数目固定, 所以对应部分的前序和中序长度应该相等, 即im-ib=pm-pb, 所以pm=pb+im-ib
        pm = pb + im - ib
        # 左子树部分: 前序就是(pb + 1, pm) (pb已经作为根节点用掉了), 中序就是(ib, im-1) (im用过了, 这里对应im左边部分)
        root.left = self.build(pb + 1, pm, ib, im - 1,data, data1)
        # 右子树部分: 前序就是(pm + 1, pe) (pm + 1开始, 就是右子树的根), 中序就是(im+1, ie) (im用过了, 这里对应im右边部分)
        root.right =self.build(pm + 1, pe, im + 1, ie,data, data1)
        return root

    def preorder(self,node): #前序遍历
        print(node.item)
        if node.left!=None:
            node1=node.left
            self.preorder(node1)
        if node.right!=None:
            node1=node.right
            self.preorder(node1)



data_A=[1,2,4,7,3,5,6,8]
data1_A=[4,7,2,1,5,3,8,6]

data_B=[2,4,7]
data1_B=[4,7,2]
A=BinaryTree()
A.root=A.build(0,len(data_A)-1,0,len(data1_A)-1,data_A,data1_A)

B=BinaryTree()
B.root=B.build(0,len(data_B)-1,0,len(data1_B)-1,data_B,data1_B)


def findpos(node,target_node,res): #返回A中所有与B相等的节点
    if node.item==target_node.item:
        res.append(node)
    if node.right is not None:
        node1=node.right
        findpos(node1,target_node,res)
    if node.left is not None:
        node1=node.left
        findpos(node1,target_node,res)


def checkifsame(nodeA,nodeB): #返回A中所有与B相等的节点
    if nodeA.item==nodeB.item:
      if nodeA.right==None and nodeB.right!=None:
          return False
      if nodeA.left==None and nodeB.left!=None:
          return False
      if nodeA.right!=None and nodeB.right!=None:
        node1=nodeA.right
        node2=nodeB.right
        res=checkifsame(node1,node2)
        if res==False:
            return False
      if nodeA.left!=None and nodeB.left!=None:
        node1=nodeA.left
        node2=nodeB.left
        res=checkifsame(node1,node2)
        if res==False:
            return False
      return True
    else:
        return False


#从A的根节点开始，首先看能不能找到B的root
def CheckifSubtree(B,A):
    if B==None or A==None:
        print('Error A or B can not be empty')

    B_root=B.root
    current=A.root
    res=[]
    findpos(current,B_root,res)
    for node in res:
        a=checkifsame(node,B_root)
    print(a)

CheckifSubtree(B,A)
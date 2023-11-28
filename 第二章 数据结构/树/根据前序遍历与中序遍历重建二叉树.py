



#先来写一个二叉树

#树的表示方式：
#1.前序遍历 2.中序遍历 3.后序遍历

#二叉树见图例.jpg
data=[1,2,4,7,3,5,6,8]#前序遍历
data1=[4,7,2,1,5,3,8,6]#中序遍历  :先访问左子节点，再访问根节点，最后访问右子节点;弥补了前序遍历难以知晓具体结构的缺点


##递归方法构建
#查询步骤是相同的 step1:从data中得到根节点==》 data1中知道左右子树  ==》 back to step1
class Node():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
class BinaryTree():
    def __init__(self):
        self.root=None

    def build(self,pb, pe, ib, ie):
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
        root.left = self.build(pb + 1, pm, ib, im - 1)
        # 右子树部分: 前序就是(pm + 1, pe) (pm + 1开始, 就是右子树的根), 中序就是(im+1, ie) (im用过了, 这里对应im右边部分)
        root.right =self.build(pm + 1, pe, im + 1, ie)
        return root


    def preorder(self,node): #前序遍历
        print(node.item)
        if node.left!=None:
            node1=node.left
            self.preorder(node1)
        if node.right!=None:
            node1=node.right
            self.preorder(node1)




    def midorder(self,node): #中序遍历
        #先访问左子节点 然后根 最后访问右子节点
        if node.left is not None:
            node1=node.left
            self.midorder(node1)
        print(node.item)
        if node.right is not None:
            node1=node.right
            self.midorder(node1)


Btree=BinaryTree()
Btree.root=Btree.build(0,len(data)-1,0,len(data)-1)

Btree.preorder(Btree.root)
print("=========================")
Btree.midorder(Btree.root)

#思考1:如果data有重复数字，能重建出唯一的二叉树吗？  不能 eg.[1,1]
#思考2:如何打印出前序/中序/后序?
#思考3:如果不允许使用递归,如何用遍历的方法重建二叉树








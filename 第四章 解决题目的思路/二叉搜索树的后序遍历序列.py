#输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果


'''
二叉搜索树（Binary Search Tree，BST）是一种常见的二叉树数据结构，它具有以下特点：
二叉树结构：每个节点最多有两个子节点，分别为左子节点和右子节点。
有序性质：对于任意节点，其左子树上的节点值都小于它，右子树上的节点值都大于它。这个特性使得二叉搜索树具有快速的查找、插入和删除操作。
中序遍历有序：对二叉搜索树进行中序遍历可以得到一个有序序列。'''



#注意到性质：二叉搜索树中序遍历一定是从小到大排序！
#所以如果给出后序遍历[5,7,6,9,11,10,8] 我们可以立刻写出中序遍历[5,6,7,8,9,11,10]



backorder=[7,4,6,5]


def VerifySquenceOfBST(backorder,length):
    root =backorder[length-1]
    lefttree=0
    for i in range(length):
        if backorder[i]>root:
            lefttree=i
            break #遍历找到左子树index

    for j in range(lefttree,length-1):
        if backorder[j]<root:
            return False
    #判断左子树是否为BST
    left=True
    if(lefttree>0):
        left=VerifySquenceOfBST(backorder,lefttree)
    right=True
    if (lefttree<length-1):
        right=VerifySquenceOfBST(backorder,length-lefttree-1)

    print(left,right)

    return left and right

a=VerifySquenceOfBST(backorder,len(backorder))
print(a)

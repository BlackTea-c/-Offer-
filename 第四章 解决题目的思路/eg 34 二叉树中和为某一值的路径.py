
#输入一颗二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径； 从树的根节点开始往下一直到叶节点
#所经过的节点形成一条路径


#递归调用的本质其实就是 stack。 先入后出 后入（先出


import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def create_random_binary_tree(depth):
    root = None
    elements = list(range(1, 30))  # 生成数字范围为10到99，可根据需要调整
    random.shuffle(elements)  # 打乱数字顺序

    for _ in range(2 ** depth):
        root = insert(root, elements.pop())

    return root

# 创建一个4层的二叉树
depth = 4
binary_tree = create_random_binary_tree(depth)

# 打印二叉树中序遍历结果（验证二叉树是否生成正确）
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

#print("Inorder Traversal of the Binary Tree:")
#inorder_traversal(binary_tree)

def findpath(root,expectedSum,path,currentSum):


    currentSum+=root.value
    path.append(root)
    isLeaf=True if root.right==None and root.left ==None else False
    if currentSum==expectedSum and isLeaf==True:
        print('A path if found')
        for node in path:
            print(node.value,end=' ')
        print('')

    if root.left!=None:
        findpath(root.left,expectedSum,path,currentSum)
    if root.right!=None:
        findpath(root.right,expectedSum,path,currentSum)
    path.pop(-1)



def Solution(root,expectedSum):

    currentSum=0
    path=[]
    findpath(root,expectedSum,path,currentSum)


root=Node(1)
root.right=Node(2)

Solution(root,3)
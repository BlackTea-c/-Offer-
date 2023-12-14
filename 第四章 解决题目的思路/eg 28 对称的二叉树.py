
#实现一个函数用来判断二叉树是否对称（是否与其镜像一样）



class node():
    def __init__(self,item):
        self.item=item
        self.right=None
        self.left=None

class BinaryTree():
    def __init__(self):
        self.root=None


tree=BinaryTree()
tree.root=node(1)
tree.root.right=node(2)
tree.root.left=node(3)
tree.root.left.left=node(4)


#前序遍历： 优先左； 如果是镜像，我们定义一个优先右的前序遍历   如果两个遍历相同！ 则说明镜像！
#注意得加上None部分
def preorder_left(root):
    left_pre=[]
    stack = [] #模拟栈结构
    cur = root
    while len(stack) != 0 or cur is not None:
        while cur is not None:# 一直到最左下
            left_pre.append(cur.item)
            if cur.left is None:
                left_pre.append(None)
            stack.append(cur) #一直左
            cur = cur.left
        cur = stack.pop() #弹出
        if cur.right is None:
            left_pre.append(None)
        cur = cur.right  #右
    return left_pre

def preorder_right(root):
    right_pre=[]
    stack = [] #模拟栈结构
    cur = root
    while len(stack) != 0 or cur is not None:
        while cur is not None:# 一直到最左下
            right_pre.append(cur.item)
            if cur.right is None:
                right_pre.append(None)
            stack.append(cur) #一直左
            cur = cur.right
        cur = stack.pop() #弹出
        if cur.left is None:
            right_pre.append(None)
        cur = cur.left  #右
    return right_pre

left=preorder_left(tree.root)
right=preorder_right(tree.root)

print(left)
print(right)




class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTToDLL:
    def __init__(self):
        self.head = None  # 双向链表的头结点
        self.prev = None  # 中序遍历时的前一个节点

    def convertToDLL(self, root):
        if root is None:
            return

        # 递归处理左子树
        self.convertToDLL(root.left)

        # 当前节点处理
        if self.prev is None:  # 如果前一个节点为 None，则当前节点为双向链表的头结点
            self.head = root
        else:
            root.left = self.prev  # 将当前节点的左指针指向前一个节点
            self.prev.right = root  # 将前一个节点的右指针指向当前节点

        self.prev = root  # 更新前一个节点为当前节点

        # 递归处理右子树
        self.convertToDLL(root.right)

    def printDLL(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.right

# 示例用法
bst = Node(5)
bst.left = Node(3)
bst.right = Node(8)
bst.left.left = Node(2)
bst.left.right = Node(4)
bst.right.left = Node(7)
bst.right.right = Node(9)

converter = BSTToDLL()
converter.convertToDLL(bst)

print("转换后的双向链表：")
converter.printDLL()

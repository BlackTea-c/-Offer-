
#给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点

class Node():
    def __init__(self,item):
        self.item=item
        self.next=None

class SingleLinklist():
    def __init__(self):
        self.head=None
        self.list=[]


    def add(self,item): #往链表尾添加节点
        if self.head is None:
            self.head=Node(item)
            self.list.append(self.head)
        else:
            node=self.head
            while(node.next is not None):
                node=node.next
            node.next=Node(item)
            self.list.append(node.next)
    def preorder(self):
        if self.head==None:
           print('Link is empty')
           return 1
        else:
            node=self.head
            while(node!=None):
                print(node.item)
                node=node.next



link=SingleLinklist()

for i in range(3):
    link.add(i)

link.preorder()

def delete(node,link):
    if node==None:
        print('node do not exist')
        return 1
    if node.next==None:
      if node!=link.head:
        current=link.head
        while(current.next!=node):
            current=current.next
        current.next=None
      else:
          link.head=None
      return 0
    if node.next!=None:
        node.item=node.next.item
        node.next=node.next.next
        return 0
delete(link.head.next.next,link)
link.preorder()




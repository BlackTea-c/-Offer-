

#如果一个链表中包含环(loop)，如何找出环的入口节点？（就是环指向的点） 1-2-3-4-5-->3  则是3

class Node():
    def __init__(self,item):
        self.item=item
        self.next=None

class SingleLinklist():
    def __init__(self):
        self.head=None

    def add(self,item): #尾部添加元素
        if self.head is None:
            self.head=Node(item)
        else:
            pointer=self.head
            #找到最后一个Node
            while pointer.next is not None:
                pointer=pointer.next
            pointer.next=Node(item)
    def addloop(self,node):#添加loop
        current=self.head
        while(current.next is not None):
            current=current.next
        current.next=node




def findentryofLoop(link):
    if link.head==None:
        print('link is empty')
        return 1
    if link.head.next==link.head:
       return link.head
    p1=link.head
    p2=link.head
    while True:
        if p1==None:
            print('link has not loop')
            return 1
        if p1.next==None:
            print('link has not loop')
            return 1
        p1=p1.next.next
        p2=p2.next
        if p1==p2:
            break
    #此时p1=p2:
    cout=1
    p1=p1.next
    while(p1!=p2):
        p1=p1.next
        cout+=1
    #得到loop内的节点数

    #此时初始化p1,p2
    p1=link.head
    p2=link.head
    #让p1先走cout步，然后同时走，最后相遇的点就是entry
    for i in range(cout):
        p1=p1.next
    while(p1!=p2):
        p1=p1.next
        p2=p2.next
    return p1 #返回节点，然后可以返回节点值


link=SingleLinklist()
for i in range():
    link.add(i)
print(link.head)

loop_node=link.head.next.next
link.addloop(loop_node)

print(findentryofLoop(link).item)



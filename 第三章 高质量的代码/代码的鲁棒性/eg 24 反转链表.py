

#输入一个链表的头节点，反转该链表并输出反转后的head


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



def reverselink(link):
    if link.head==None:
        print('link is empty')
        return 1
    if link.head.next==None:
        print(link.head.item)
        return link
    p1=link.head.next
    p2=link.head
    while(p1.next is not None):
        tem=p1.next
        p1.next=p2
        p2=p1
        p1=tem


    #print(p1.item)
    link.head.next=None
    link.head=p1
    p1.next=p2
    return link

link=SingleLinklist()
for i in range(5):
    link.add(i)

reverselink(link)

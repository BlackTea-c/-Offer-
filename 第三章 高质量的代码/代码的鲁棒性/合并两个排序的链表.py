


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

    def preorder(self):
        current=self.head
        if self.head==None:
            print('link is empty')
            return 1
        while(current!=None):
            print(current.item)
            current=current.next



link1=SingleLinklist()
link2=SingleLinklist()

for i in range(6):
    link1.add(i)
link2.add(3)
link2.add(4)
link2.add(7)
link2.add(8 )

def mergelink(link1,link2):
    if link1.head==None:
        return link2
    if link2.head==None:
        return link1
    p1=link1.head
    p2=link2.head
    link3=SingleLinklist()
    while True:
        if p1.item<=p2.item:
            link3.add(p1.item)
            p1=p1.next
        else:
            link3.add(p2.item)
            p2=p2.next

        if p1==None:
            while(p2!=None):
              link3.add(p2.item)
              p2=p2.next
            break
        if p2==None:
            while(p1!=None):
              link3.add(p1.item)
              p1=p1.next
            break
    return link3

link3=mergelink(link1,link2)
link3.preorder()
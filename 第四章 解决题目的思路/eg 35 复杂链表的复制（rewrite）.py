



#
class Link():
    def __init__(self,item):
        self.item=item
        self.next=None
        self.Sibling=None #指向任意节点

link1=Link(1)
link1.next=Link(2)
link1.Sibling=Link(3)
link1.next.next=link1.Sibling



def LinkClone(head):

    #先处理next指针
    if head==None:
        print('head is None')
        return

    clone_head=head
    link2=clone_head
    current=head
    while(current.next!=None):
        clone_head.next=current.next
        clone_head=clone_head.next
        current=current.next
    return link2

link2=LinkClone(link1)
print(link2.Sibling.item,link2.next.item,link2.next.next.item)



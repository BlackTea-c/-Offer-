


#输入一个链表，输出链表的倒数第k个节点，且只遍历一次！

#这还是个双指针！两个指针从起点不同时出发

#假设链表长度为n（未知）,要倒数第k个节点，我们让p1先出发，走k-1步，然后p2出发；此时p1需要走n-k步到达尾部,p2同时走了n-k+1,这刚好是倒数第k个位置！ 卧槽！


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
    def findkthfromTail(self,k):
        if self.head==None:
            print('link is empty')
            return None
        if type(k)!=int:
            print('k must be int')
            return 1
        if k<=0:
            print('k must >=1')
            return 1
        p1=self.head
        p2=self.head
        i=1
        while(i<k):
            p1=p1.next
            i+=1
            if p1.next==None:
                print('k out of range')
                return 1
        while(p1.next!=None):
            p2=p2.next
            p1=p1.next
        return p2.item


link=SingleLinklist()
for i in range(8):
    link.add(i)

print(link.findkthfromTail('str'))

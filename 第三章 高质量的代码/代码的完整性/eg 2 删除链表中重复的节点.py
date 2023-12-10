


#在一个排序的链表中！！！如何删除重复的节点

#当前节点与next节点值相同就是重复的节点。就一起删除，直到没有重复的节点
class Node():
    def __init__(self,item):
        self.item=item
        self.next=None


class SingleLink():
    def __init__(self):
        self.head=None

    def add(self,item): #往链表尾添加节点
        if self.head is None:
            self.head=Node(item)
        else:
            node=self.head
            while(node.next is not None):
                node=node.next
            node.next=Node(item)
    def preorder(self):
        if self.head==None:
           print('Link is empty')
           return 1
        else:
            node=self.head
            while(node!=None):
                print(node.item)
                node=node.next


    def DeleteDuplication(self):
        if self.head==None:
            print('link is empty')
            return 1
        current=self.head
        former=self.head #former=current   #获取连续node的第一个node的前节点
        consis=0 #记录是否有连续情况 比如2233 这种情况下的former不再跟随current.former
        while(current.next is not None):

            judge=-1 #等于0代表头连续情况，等于1代表中部连续情况
            if (current.item!=current.next.item):
                consis=0 #没有连续则清零！

            while(current.item==current.next.item):
               if self.head==current:
                  judge=0 #头连续
                  current=current.next
               else:
                   judge=1
                   current=current.next
               consis=1 #代表进行了删除操作一次
               if current.next==None:
                   break



            if judge==0:
               self.head=current.next
            if judge==1:
                former.next=current.next
            if consis==0:
               former=current
            if current.next!=None:
               current=current.next





link=SingleLink()
link.add(1)
link.add(2)
link.add(3)

link.DeleteDuplication()

link.preorder()

#感觉自己写得超级复杂= = 虽然最后还是写出来了哈哈，看下别人写的吧，我这个还是有点乱
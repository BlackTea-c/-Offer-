#队列：先进先出
#栈：先进后出




class Stack():
    def __init__(self):
        self.content=[]


    def push(self,item):
        if item!=None:
          self.content.append(item)
        return item

    def pop(self):
      if len(self.content)!=0:
        pop_item=self.content[-1]
        self.content.pop(-1)
        return pop_item
      else:
          return None



class Queue():
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def appendTail(self,item):
        self.stack1.push(item)
    def deleteHead(self):
        if self.stack2.content==[]: #stack2为空时:
          n=len(self.stack1.content)
          for i in range(n):
             self.stack2.push(self.stack1.pop())

          pop_item=self.stack2.pop()
          return pop_item
        else:
          pop_item=self.stack2.pop()
          return pop_item


    def show(self):
        print("stack1:",self.stack1.content)
        print("stack2:",self.stack2.content)



queue=Queue()

queue.appendTail("a")
queue.appendTail("b")
queue.appendTail("c")

queue.show()
print(queue.deleteHead())
queue.show()
print(queue.deleteHead())
queue.show()
queue.appendTail("d")
queue.show()
print(queue.deleteHead())
queue.show()
queue.appendTail("e")
queue.appendTail("f")
queue.show()
print(queue.deleteHead())

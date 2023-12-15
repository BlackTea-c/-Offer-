
#定义stack结构，使得在该类型中可以实现min 调用min,push,pop时间复杂度都为O(1)



class Stack1():
    def __init__(self):
        self.items=[]#存储items


    def push(self,item): #压入元素,每压入一个元素便检查其与下面一个元素大小，更大则交换; 但这种思路不能保证最后压入栈的元素最先出栈
        if self.items==[]:
            self.items.append(item)
        else:
            if item>self.items[-1]:
                tem=self.items[-1]
                self.items[-1]=item
                self.items.append(tem)
    def pop(self): #弹出
        self.items.pop(-1)

    def min(self):
        return self.items[-1]



#那我们用一个指针来记录最小值
class Stack():
    def __init__(self):
        self.items = []  # 存储items
        self.mstack=[0,]
        self.min_pos=0

    def push(self, item):  # 压入元素,每压入一个元素便检查其与下面一个元素大小，更大则交换; 但这种思路不能保证最后压入栈的元素最先出栈
        if self.items == []:
            self.items.append(item)
        else:
            if item <= self.items[self.min_pos]:
                self.items.append(item)
                self.min_pos=len(self.items)-1
                self.mstack.append(self.min_pos)
            else:
                self.items.append(item)

    def pop(self):  # 弹出
        if self.items[-1]==self.items[self.mstack[-1]]:
           self.mstack.pop(-1)
        self.items.pop(-1)

    def min(self):
        return self.items[self.mstack[-1]]



stack=Stack()
stack.push(3)
stack.push(4)
stack.push(1)
stack.push(2)

print(stack.min())
print(stack.mstack)
stack.pop()
print(stack.min())


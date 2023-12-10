#输入整数数组，使得所有奇数位于数组的前半部分，偶数位于后半buf

list=[100,1,3,4,5,2,3,4,-51,2,56,6,7,8,88,6,1,2]
def sortOddandEven(list):
    odd=[]
    even=[]
    for i in list:
        if i&1:
            odd.append(i)
        else:
            even.append(i)
    odd.extend(even)
    return odd

#sortOddandEven(list)

#拓展性！！！！！  如果改成<0在前面 大于0在后面？  能被3整除的在前面 不能的在后面？  能不能写出通用的代码？


#另外上面这种实现方法还是不太好，因为相当于新建了数组而非从原始数组进行修正

#还是双指针
def sortoddeven(list): #ps指针遇到偶数则不动，pe指针遇到奇数则不动
    ps=0
    pe=len(list)-1

    while(ps<=pe):
        if list[ps]&1==0 and list[pe]&1==1: #偶数在奇数前面
           tem=list[ps]
           list[ps]=list[pe]
           list[pe]=tem
           #交换
           ps+=1
           pe-=1
           continue
        if list[ps]&1==1:
            ps+=1
        if list[pe]&1==0:
            pe-=1
    return list
sortoddeven(list)






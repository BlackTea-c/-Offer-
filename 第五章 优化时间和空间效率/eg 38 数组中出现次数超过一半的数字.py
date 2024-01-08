


A=[1,2,2,2,2,3,4,2,9]

#数组长度为9，2出现了5次>4.5 所以输出2



#方案一：快速排序；选中a,比a大的在右边，比a小的在左边，如果此时a的下标为n/2则就是a；如果比n/2大，说明中位数在左边反之在右边;在哪边就在哪边找

def Swap(A, i, j): #交换
    A[i], A[j] = A[j], A[i]
def Partition(A, left, right):  # 划分函数 范围left===>right
    pivot = A[right]               # 这里每次都选择最后一个元素作为基准
    tail = left - 1                # tail为小于基准的子数组最后一个元素的索引
    for i in range(left,right):  # 遍历基准以外的其他元素
        if A[i] <= pivot:            # 把小于等于基准的元素放到前一个子数组末尾
            tail += 1
            Swap(A, tail, i)
    # 最后把基准放到前一个子数组的后边，剩下的子数组既是大于基准的子数组
    # 该操作很有可能把后面元素的稳定性打乱，所以快速排序是不稳定的排序算法
    Swap(A, tail + 1, right)
    return tail + 1                    # 返回基准的索引


def MorethanhalfNum(A,left,right):
    #假设一定有这样一个数字，我们这里就不做check了
    pivot_index=Partition(A,left,right)
    if pivot_index==(len(A)-1)//2:
        print(A[pivot_index])
        return

    if pivot_index>=(len(A)-1)//2:
        MorethanhalfNum(A,left,pivot_index-1)
    else:
        MorethanhalfNum(A,pivot_index+1,right)


MorethanhalfNum(A,0,len(A)-1)

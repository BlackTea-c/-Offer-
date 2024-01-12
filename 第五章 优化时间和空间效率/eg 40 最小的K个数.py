

#输入n个整数，求出最小的k个数
A=[5,7,3,2,4,1]


def Partition(A,left,right):


    pivot = A[right]
    tail=left-1
    for i in range(left,right):
        if A[i]<=pivot:
            tail+=1
            A[i],A[tail]=A[tail],A[i]

    A[right],A[tail+1]=A[tail+1],A[right]
    return  tail+1



#方案一:
def FindminK(A,K,left,right):
    #我们同样可以基于Partition解决这个问题

    if left>=right:
        return

    tail=Partition(A,left,right)
    print(tail,A)
    if tail==K-1 or tail==K:
        for i in range(0,K):
            print(A[i])
        return
    if tail>K-1:
        FindminK(A,K,left,tail-1)
    else:
        FindminK(A,K,tail+1,right)



FindminK(A,5,0,len(A)-1)


#解法2  适合处理海量数据



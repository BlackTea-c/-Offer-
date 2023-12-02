




def mergesort(list,ps,pe):
    if pe-ps<=1:
        if list[ps]>list[pe]:
            tem=list[ps]
            list[ps]=list[pe]
            list[pe]=tem
        return list
    pm=(ps+pe)//2

    mergesort(list,ps,pm)
    mergesort(list,pm+1,pe)
    merge(list,ps,pe)
    return list
def merge(list,ps,pe):

    B = []
    #确定中间的index
    pm=(ps+pe)//2
    #print(pm)
    #辅助数组
    i=ps
    j=pm+1
    #两个数组排序合并: (ps,pm),(pm+1,pe),如果是[a,b]这种只有两个元素的 仍然可以[a],[b]
    while(i<=pm and j<=pe):
          if list[i]<=list[j]:
            B.append(list[i])
            i+=1
          else:
            B.append(list[j])
            j+=1
    while(j<=pe):
        B.append(list[j])
        j+=1
    while(i<=pm):
        B.append(list[i])
        i+=1

    list[ps:pe+1]=B



list=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]

print(mergesort(list,0,len(list)-1))


#参考答案:

# 合并两个已排好序的数组A[left...mid]和A[mid+1...right]
def Merge(A, left, mid, right):
    len = right - left + 1
    temp = []
    i, j, index = left, mid + 1, 0
    while i <= mid and j <= right:
        # 带等号保证归并排序的稳定性
        if A[i] <= A[j]:
            temp[index+1] = A[i]
            i += 1
        else:
            temp[index+1] = A[j]
            j += 1
        index += 1
    while i <= mid:
        temp[index] = A[i]
        index += 1
        i += 1
    while j <= right:
        temp[index] = A[j]
        index += 1
        j += 1
    for k in range(len):
        A[left+k] = temp[k]
# 递归实现的归并排序(自顶向下)
def MergeSortRecursion(A, left, right):
    # 当待排序的序列长度为1时，递归开始回溯，进行merge操作
    if left == right:
        return
    mid = (left + right) / 2
    MergeSortRecursion(A, left, mid)
    MergeSortRecursion(A, mid + 1, right)
    Merge(A, left, mid, right)
# 非递归(迭代)实现的归并排序(自底向上)
def MergeSortIteration(A, len):
    # 子数组索引,前一个为A[left...mid]，后一个子数组为A[mid+1...right]
    i = 1
    while i < len:
        left = 0
        # 后一个子数组存在(需要归并)
        while left + i < len:
            mid = left + i - 1
            # 后一个子数组大小可能不够
            if mid + i < len:
                right = mid + i
            else:
                right = len - 1
            Merge(A, left, mid, right)
            # 前一个子数组索引向后移动
            left = right + 1
        i *= 2
def main():
    A1 = [6, 5, 3, 1, 8, 7, 2, 4]   # 从小到大归并排序
    A2 = [6, 5, 3, 1, 8, 7, 2, 4]
    n1 = len(A1)
    n2 = len(A1)
    MergeSortRecursion(A1, 0, n1 - 1)     # 递归实现
    MergeSortIteration(A2, n2)           # 非递归实现
    print("递归实现的归并排序结果：")
    for i in range(n1):
        print("%d ", A1[i])
    print("\n")
    print("非递归实现的归并排序结果：")
    for i in range(n2):
        print("%d ", A2[i])
    print("\n")




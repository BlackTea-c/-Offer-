from random import randint

# 来咯，四大排序算法：插入排序，冒泡排序，归并排序，快速排序



#1.快速排序
list=[6,5,8,7,10,1,12,3,4,4]


def quick_sort(list,ps,pe): #ps=0,pe=len(list)-1
    if ps>=pe:
        return list
    choose=randint(ps,pe)


    print("start=",list)
    st=list[ps]
    list[ps]=list[choose]
    list[choose]=st



    i=ps
    j=pe

    pivot=list[ps]
    print("i,j,pivot:", ps,pe,pivot)
    print("middle:", list)
    while(i<j):

        while i<j and list[j]>=pivot:
            j-=1
        list[i]=list[j] #从后往前找直到找到第一个比它小的数字，然后交换，若没有则不变,list[j]=pivot
        #i+=1 不应该有这个，搞了半天原来是这里出问题了！！！！！！
        list[j]=pivot
        while i <j and list[i] <= pivot: #从前往后找比它大的然后交换
            i += 1
        list[j]=list[i]
        list[i]=pivot
        j-=1


    im=list.index(pivot)
    print("end=", list)
    quick_sort(list,ps,im-1)
    quick_sort(list,im+1,pe)
    return list


quick_sort(list,0,len(list)-1)
print("result=",list)





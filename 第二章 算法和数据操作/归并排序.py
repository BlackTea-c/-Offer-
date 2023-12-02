




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




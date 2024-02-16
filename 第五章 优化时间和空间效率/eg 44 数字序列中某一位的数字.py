

# 01234567891011121314
#求第n位对应的数字





def coutofintegers(n):
    if 0<=n<10:
        return n

    cout=1 #位   #cout这里出现了问题
   #锁定位数
    while(n>=0):
        if n-9*10**(cout-1)*cout<=0:
            break
        n-=9*10**(cout-1)*cout
        cout+=1



    print('new_n:',n)
    print('cout:',cout)

    #得到新的n；从cout开始计算
    mi=0
    while(cout*mi<n):
        if cout*(mi+1)>=n:
            break
        mi+=1
    print('mi',mi)

    final=10**(cout-1) +mi
    yu=n-mi*cout-1


    return str(final)[yu]





print(coutofintegers(191))
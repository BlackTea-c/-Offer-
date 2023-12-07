
#本质上求x1+..+xn=m  max(x1*x2*x3*..xn)  这个优化问题


#分解： f(n)=max{f(i)*f(n-i)}

#f(1)=1 f(2)=2

list=[1,2,3]

#动态规划法
def max_find(n,list):
    max = 0
    for i in range(1,n): #长度i  n-i
        if list[i-1]*list[n - i] >= max:
            max = list[i-1] * list[n - i]
    return max
def f(n):
    #注意因为要求至少剪一刀，计算n<=3时的f(n)值 与list中的值会不相同
    if n<=3:
        return n-1

    m=len(list)
    while(m<=n):
        list.append(max_find(m,list))
        m+=1
    print(list)
    return list[n-1]
#f(110)
#print(list)



#贪心算法
def f1(n):
    if(n<2):
        return 0
    if(n==2):
        return 1
    if(n==3):
        return 2

    #尽可能多的去剪长度为3的绳子段:
    timesOf3=n//3

    #当绳子最后剩下的长度为4时，不能再去剪长度为3的绳子段
    #此时更好的办法是把绳子剪成长度为2的两端 因为2*2 > 1*3
    if(n-timesOf3*3==1):
        timesOf3-=1
    timesOf2=(n-timesOf3*3)//2
    return (3**timesOf3)*(2**timesOf2)
print(f1(22),f(22))


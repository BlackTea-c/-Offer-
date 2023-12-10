#实现函数 x**(n)  x为实数  n为整数


def Power(x,n):
    if (x==0 or x==1) and n!=0:
        return x
    if n==0 and x!=0:
        return 1
    if n==0 and x==0:
        print('0 can not powered by n=0')
        return False
    if n <0:
        x=1/x
        n=-n
    sum=1
    for i in range(n):
        sum*=x
    return sum


print(Power(0,-1))


def Power_eff(x,n):#现在来编写一个更高效的计算方式; 实际上x^n = x^(n/2) * x^(n/2) n为偶数    n为奇数 x^n=x^(n-1/2) * x^(n-1/2) *x
    if (x==0 or x==1) and n!=0:
        return x
    if n==0 and x!=0:
        return 1
    if n==0 and x==0:
        print('0 can not powered by n=0')
        return False
    if n <0:
        x=1/x
        n=-n
    result=power_cout(x,n)
    return result


def power_cout(x,n):#递归  此时x为正实数 n为正整数
    if n==1:
        return x
    result=power_cout(x,n>>1) #用位运算代替除法
    result*=result
    if(n&2==1): #判断是否是偶数
        result*=x
    return result


print(Power(3,8))
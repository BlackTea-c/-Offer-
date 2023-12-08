#输入一个整数，计算其二进制表示中1的个数.



def coutnumberone(n):
    sum=0
    while(n>=1):
        a=n%2
        if a==1:
          sum+=1
        n=n//2
    return sum

print(coutnumberone(1))

#弊端是除法运算的效率要比移位运算要低得多!


#python中的移位运算符"<<"  ">>"与C++是一样的


def coutnumberone2(n):
    sum=0
    while(n):
        if(n&1):#与运算 0&0=0  0&1=0  1&1=1
            sum+=1
        n=n>>1
    print(sum)


'''按位与运算（AND）是针对两个二进制数的操作，它会对两个数的每一对对应位进行逻辑与操作。具体来说，如果两个对应位都为 1，则结果为 1；否则结果为 0。

例如，如果 n 是一个整数，n & 1 就是对 n 和二进制数 1 进行按位与运算。1 的二进制表示形式是 0001，而任何数与 1 进行按位与运算，结果都取决于该数的最低位（最右边的位）是 1 还是 0。

如果 n 的最低位是 1，则 n & 1 的结果为 1；如果 n 的最低位是 0，则 n & 1 的结果为 0。这种操作通常用于检查整数的最低位是否为 1。'''

print(9>>1) #实际编程中尽可能用位运算代替乘除法

#负数的表示就是0变1 1变0 最后再+1
#那么输入的n有负数怎么办？
def coutnumberone3(n):
   sum=0
   flag=1
   while(flag<=-n):
       if(n&flag):
           sum+=1
       flag=flag<<1

   print(sum)
#草算了暂时没搞懂


def numberof1(n):
    sum=0

    while(n):
        sum+=1
        n=(n-1)&n

    return sum

print(numberof1(-9))
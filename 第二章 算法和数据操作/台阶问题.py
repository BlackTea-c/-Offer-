# 书中P77页

#动态规划，仍然是简单地求斐波那契数列


#但是给出一个拓展，就是可以一次可以调1,2..,n级，此时跳上一个n级台阶有多少种方法？  2^(n-1)




# 书中P79页 矩形无重叠覆盖问题
#f(8) 记作2*8的矩形
#从矩形最左边决定第一个矩形怎么覆盖，竖着放则剩下的就是f(7) 横着就是f(6)  so f(8)=f(7)+f(6)不难发现仍然是斐波那契数列
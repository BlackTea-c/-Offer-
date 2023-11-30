#递归调用效率没有循环高喵




#Fibonacci数列
# 输入n,求Fibonacci数列的第n项


#先写一个递归~
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>=2:
        return fibo(n-1)+fibo(n-2)
#print(fibo(12)) #自行感受n=100，慢的很
#效率低。


#想个新法子
f_n=[0,1] #储存已经计算好的f(n)，计算时如果发现有目标f(m),则直接拿来用，如果没有，则计算后将f(m)添加上

n=12
for i in range(n+1):
   if i>=2:
       f_n.append(f_n[i-1]+f_n[i-2])
print(f_n[n])




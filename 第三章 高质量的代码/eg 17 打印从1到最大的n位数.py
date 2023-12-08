

#输入数字n，按顺序打印出从1到最大的n位十进制数 eg n=3  1-999

#python不必担心大数问题...


def f(n): #n>=1
    max=0
    for i in range(n):
        max=max+9*10**(i)

    for i in range(1,max+1):
        print(i)
#f(10)
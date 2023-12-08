

#输入数字n，按顺序打印出从1到最大的n位十进制数 eg n=3  1-999

#python不必担心大数问题...


def f(n): #n>=1
    max=0
    for i in range(n):
        max=max+9*10**(i)

    for i in range(1,max+1):
        print(i)
#f(10)





#用全排列的方法解决,递归

def printToMaxOfNDigits(n):
    if n <= 0:
        return

    number = ['0'] * n #初始化n位数
    for i in range(10):
        number[0] = str(i)
        printToMaxOfNDigitsRecursively(number, n, 0)

def printNumber(number): #省略为0的开头 00000102 从第一个不为0的开始打印
    isBeginning0 = True
    for i in range(len(number)):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            print(number[i], end='')
    print()

def printToMaxOfNDigitsRecursively(number, length, index):
    if index == length - 1:
        printNumber(number)
        return

    for i in range(10):
        number[index + 1] = str(i)
        printToMaxOfNDigitsRecursively(number, length, index + 1)

# 测试示例
n = 3
printToMaxOfNDigits(n)
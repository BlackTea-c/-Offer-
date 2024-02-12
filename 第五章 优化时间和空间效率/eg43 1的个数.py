
def numberof1temp(n):
    if 0 < n < 10:
        return 1
    if n <= 0:
        return 0
    sum_1 = 0
    str_n = str(n) #化为字符串
    len_n = len(str_n) #长度
    temp = int(str_n[1:]) #批分 1-100 => temp=00
    first_number = int(str_n[0])  #首位数字 1
    numberoffirst = numberof1firstnumber(str_n) #首位数字>1 则10**len次方   小于等于1 则要考虑上限
    sum_1 += numberoffirst
    numberofleft = first_number * (len_n - 1) * 10**(len_n -2) #剩下的几位中

    sum_1 += numberofleft
    sum_1 += numberof1temp(temp)

    return sum_1

def numberof1firstnumber(str_n):
    first_number = int(str_n[0])
    if first_number > 1:
        number = 10**(len(str_n ) -1)
    else:
        number = int(str_n[1:]) + 1
    return number

cout=numberof1temp(100)
print(cout)
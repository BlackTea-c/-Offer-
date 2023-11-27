


string="We are happy."

#将空格替换为%20

#错误展示：
def space_alter(string):
    for i in range(len(string)):
        if string[i]==" ":
            string[i]="%20"  #错误原因，python中字符串不支持直接赋值！！！！

    return string

#新建列表，拼接成新的字符串
def space_alter1(string):
    string_new=""
    for str in string:
        if str==" ":
            string_new+="%20"
        else:
            string_new+=str
    print(string_new)
space_alter1(string)

#string.replace(" ","%20")


#因为我用的python，书上讲的C++用双指针来解决，我不知道python这里是个什么情况///有懂得小伙伴指教一下（

#指针p1,p2指向同一位置即表示替换停止。
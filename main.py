

def test(a):
    a+=1
    if a<=10:
        test(a)
    else:
        return False

b=test(100)
print(b)
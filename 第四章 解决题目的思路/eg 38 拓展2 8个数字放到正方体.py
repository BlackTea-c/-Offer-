#要求与对面数字和相同，判断有无可能

#这相当于先求8个数字的所有排列，然后判断有没有一种排列满足那三个等式



numbers=[1,3,3,3,3,1,1,1] #对应a1,a2,a3,a4...a8

def equalcheck(numbers):
    check=False
    if numbers[0]+numbers[1]+numbers[2]+numbers[3]==numbers[4]+numbers[5]+numbers[6]+numbers[7]:
        if numbers[0] + numbers[3] + numbers[4] + numbers[7] == numbers[1] + numbers[2] + numbers[5] + numbers[6]:
            if numbers[0] + numbers[1] + numbers[4] + numbers[5] == numbers[2] + numbers[3] + numbers[6] + numbers[7]:
                check=True

    return check



Permu=[]
def Permutation(numbers,ps):

    if ps==len(numbers)-1:
       Permu.append(numbers)
    else:
        for j in range(ps,len(numbers)):
            numbers[j],numbers[ps]=numbers[ps],numbers[j]
            Permutation(numbers,ps+1)
            numbers[j], numbers[ps] = numbers[ps], numbers[j]

Permutation(numbers,0)
for number in Permu:
    check=equalcheck(number)
    if check==True:
       print(number,check)
       break




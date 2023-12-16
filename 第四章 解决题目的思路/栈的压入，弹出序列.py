


stack_pushlist=[1,2,3,4,5]
stack_poplist=[4,3,5,1,2]



def isPoporder(stack_pushlist,stack_poplist):
    if len(stack_pushlist)!=len(stack_poplist):
        return False
    p1=0
    p2=0
    stack_tem=[]

    check=True
    while(p2<=len(stack_poplist)-1):
          if stack_pushlist[p1]==stack_poplist[p2]:
            p2+=1
            p1+=1
          else:
            stack_tem.append(stack_pushlist[p1])
            p1+=1
          if p1>len(stack_poplist)-1:
              break
    check_stack=[stack_tem[-1-i] for i in range(len(stack_tem))]
    if check_stack==stack_poplist[p2:]:
        return True
    else:
        return False

print(isPoporder(stack_pushlist,stack_poplist))









isPoporder(stack_pushlist,stack_poplist)
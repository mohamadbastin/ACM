#F


def first_line(a):
    a = a.split(' ')
    return int(a[-1])


d = first_line(input())


def room_number(a):
    a = a.split(' ')
    a = [int(i) for i in a]
    return a


def a_maker(a):
    b = []
    for i in range(max(a)+1):
        if i in a:
            b.append(1)
        elif i not in a:
            b.append(0)
    return b


def cut(a,d):
    a.sort()
    count = 0
    base = a[0]
    b=[]

    for i in range(len(a)):
        if a[i] > base+d:
            base=a[i]
            count+=1
            b.append(a[i])
    if a==b:
        return count
    else:
        return count+1
    # if a[0]==a[-1]:
    #     return count+1
    # else:
    #     return count

    # for i in range(len(a)-d):
    #     if a[i]==0:
    #         continue
    #     elif a[i]==1:
    #         count+=1
    #         for j in range(i,i+d+1):
    #             a[j]=0
    # for i in range(len(a)-d-1,len(a)):
    #     if len(a)-d-1 < 0:
    #         for j in range(len(a)):
    #             if a[j] == 1:
    #                 count += 1
    #                 break
    #         break
    #     elif a[i]==1:
    #         count+=1
    #         break


def out(a,d):
    return cut((room_number(a)),d)




secline = input()

print(out(secline,d))

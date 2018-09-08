line =  int(input().strip("\n"))
bunmer = list(map(int,input().split(" ")))

def dd(li,num):
    if len(li) <=0:
        return num
    else:
        num += li[0]
        if li[0]%2 ==0:
            if len(li) <2:
                newli = []
            else:
                newli = li[2:]

        else:
            newli = li[1:]

        dd(newli, num)

print(dd(bunmer,0))
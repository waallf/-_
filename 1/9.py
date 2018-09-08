length,num = list(map(int,input().split(" ")))
chuan = list(map(int,input().split(" ")))
index_li = []
for index,i in enumerate(chuan):
    if i==0:
        index_li.append(index)

max_length = 0
for index,j in enumerate(index_li[:-2]):
    if index ==0:
        max_length = index_li[index +2]
    else:
        if max_length < index_li[index+2] - index_li[index-1] -1 :

            max_length = index_li[index+2] - index_li[index-1] -1

if max_length < length - index_li[-3] -1:
    max_length = length - index_li[-3]-1
print(max_length)
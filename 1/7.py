nm = list(map(int,input().split(" ")))

all = int((nm[0] + nm[1]) /3.)
if nm[0] >= all and nm[1] >=all:
    print (all)
    exit()
elif nm[0] < all:
    print(nm[0])
else:
    print(nm[1])
line = input()
# line = "1+6/3"
fuhao = ("+","-","*","/")
def yunsuan(a,b,c):
    if c == "+":
        return a+b
    if c == "-":
        return b-a
    if c == "*":
        return a*b
    if c == "/":
        return b/a
fuzhan = ["#"]
shuzhan = []
for i in line:
    if i in fuhao:
        if (i =="*" or i =="/") and (fuzhan[-1] =="+" or fuzhan[-1] =="-") : # 后一个操作符的优先级没有前一个高
            yusuan = fuzhan.pop()
            all= yunsuan(int(shuzhan.pop()),int(shuzhan.pop()),yusuan)
            fuzhan.append(i)
            shuzhan.append(all)
        else:
            fuzhan.append(i)
    else:
        shuzhan.append(i)

all= yunsuan(int(shuzhan.pop()),int(shuzhan.pop()),fuzhan.pop())
print(int(all))
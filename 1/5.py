line = input()
# line = "1-8/3+1"
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
all = int(line[0])
for i in line:
    if i in fuhao:
        if ((i == "*" or i == "/") and fuzhan[-1] !="#") or ((i == "+" or i == "-") and (fuzhan[-1]== "+" or fuzhan[-1]== "-")):

            yusuan = fuzhan.pop()
            all= yunsuan(float(shuzhan.pop()),float(shuzhan.pop()),yusuan)
            fuzhan.append(i)
            shuzhan.append(all)
        else:
            fuzhan.append(i)
    else:
        shuzhan.append(i)
while fuzhan[-1] != "#":
    all= yunsuan(float(shuzhan.pop()),float(shuzhan.pop()),fuzhan.pop())
    shuzhan.append(all)
print(int(all))
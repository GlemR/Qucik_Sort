y = [12, 11, 13, 5, 6]
x = []
i = 1
while True:
    k = pow(2,i)-1
    if k < len(y):
        x.append(k)
    else:
        break
    i+=1
x = x[::-1]
print(x)

for z in range(len(x)):
    for i in range(1,len(y),x[z]):
        for j in range(i,0,-x[z]):
            if y[j] < y[j-1]:
                y[j], y[j - 1] = y[j - 1], y[j]
            else:
                break
print(y)

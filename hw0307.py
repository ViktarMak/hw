f = open("mylist.txt")
summa = 0
n = 0
for i in f:
    g = int(i[len(i)-2])
    summa += g
    n += 1
    if g < 3:
        print(i[:-1])
print('Average mark: %.2f' % (summa/n))


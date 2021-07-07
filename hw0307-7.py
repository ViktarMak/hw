a = [25, 4, 2, 'a', 6, 10, 18]
b = [2, 'a', 18, 6, 1, "tree"]
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)
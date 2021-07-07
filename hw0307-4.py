def mylist(s1, s2, amount, l):
    from random import randint
    for i in range(amount):
        l.append(randint(s1, s2))


def algorithm(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


lst = []
dct = {}

mn = int(input('Minimum: '))
mx = int(input('Maximum: '))
qty = int(input('Number of elements: '))

mylist(mn, mx, qty, lst)
algorithm(lst, dct)

for item in sorted(dct):
    print("'%d':%d" % (item, dct[item]))
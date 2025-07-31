from collections import OrderedDict

od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

print(list(od.items()))


from collections import OrderedDict

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)

print("OrderedDict:")
od = OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3)])
for k, v in od.items():
    print(k, v)
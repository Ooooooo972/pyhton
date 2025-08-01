from collections import defaultdict

d = defaultdict(list)

d['fruits'].append('apple')
d['vegetables'].append('carrot')
d['fruits'].append('banana')
d['juices'].append('orange juice')
print(d)

print(d['juices'])
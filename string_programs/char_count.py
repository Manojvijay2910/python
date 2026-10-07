s = 'bbbbaaaannnnzzzzzaaaaaiiiii'
d = {}
for c in s:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

for k, v in d.items():
    print("{} = {}".format(k, v))
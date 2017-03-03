f = open('history.txt', 'r', encoding = 'utf-8')
hs = f.readlines()
f.close()
s = []
for el in hs[1:9]:
    el = el.strip('\n')
    s.append(el)

print(s)

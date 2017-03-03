base = [
       {
         'name' : 'на всю катушку',
         'definition': 'intensificator',
         'examples': ['Beautiful day in Portland! Rock!1! На всю катушку']
       },
       {
         'name' : 'в полной мере',
         'definition': 'intensificator',
         'examples': ['The Avengers movie впечатлило меня в полной мере!']
       }]
i = 0
names = []
while i < len(base):
    for key in base[i]:
        if key == 'name':
            names.append(base[i][key])
    i += 1
print(names)

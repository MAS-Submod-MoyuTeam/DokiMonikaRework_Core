a = list()

b = {
    'Id':'DateTestb',
    'Count':0
}

c = {
    'Id':'DateTestc',
    'Count':112
}

a.append(b)
a.append(c)
try:
    print(c['J'])
except KeyError:
    print('None')
    
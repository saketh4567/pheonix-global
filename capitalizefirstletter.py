#capitalize first letter in every word
a=input('hello world')
b=list(a)
space=False
for i in range(len(b)):
    if i==0:
        b[i]=b[i].upper()
    elif b[i]==' ':
        space=True
    elif space:
        space=False
        b[i]=b[i].upper()
print(''.join(b))
"""b=a.split(" ")
for i in range(len(b)):
    b[i]=b[i].capitalize()
print(b)
print(' '.join(b))"""

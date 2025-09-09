s = 'AaBbCcDd'

u = ''.join(c for c in s if c.isupper())
l = ''.join(c for c in s if c.islower())

print('Заглавные:', u)
print('Строчные:', l)

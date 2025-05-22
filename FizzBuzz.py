f = ['', '', 'Fizz']
b = ['', '', '', '', 'Buzz']
for i in range(1, 101):
    print((f[0] + b[0]) or i)
    f.append(f.pop(0))
    b.append(b.pop(0))
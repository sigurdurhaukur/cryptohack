msg = 'label'
flag = ''
for char in msg:
    flag += chr(ord(char) ^ 13)

print('crypto{' + flag + '}')

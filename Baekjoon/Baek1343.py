#폴리오미노

str = input()
n = 0

while True:

    if n >= len(str):
        break

    if str[n:n+4] == 'XXXX':
        n = n+4
        str = str.replace('X','A',4)

    elif str[n:n+2] == 'XX':
        n = n+2
        str = str.replace('X', 'B', 2)
    
    elif str[n] == '.':
        n = n + 1
    
    else:
        str = -1
        break

print(str)

#뒤집기 0을 1로 1을 0으로 모든 숫자가 같게끔 하는 최소 횟수 구하기

s = input()
l = len(s)
 
temp = s[0]
zero = 0
one = 0
 
if s[0] == '0':
  zero += 1
else:
  one += 1
 
for i in range(l):
  if s[i] != temp:
    if temp == '0':
      one += 1
      temp = s[i]
    else:
      zero += 1
      temp = s[i]
 
print(min(zero, one))
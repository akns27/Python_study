n = int(input())
num = 0
for i in range(1, n+1):
  num += i#ex)6이면 1+2+3 = 6

for i in range(1, n+1):
  for j in range(1, i+1):
    print(num, end =' ')
    num -= 1
  print( )


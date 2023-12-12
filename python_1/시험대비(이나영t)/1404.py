n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
  print(*numbers)
  last = numbers.pop(0)
  numbers.append(last)
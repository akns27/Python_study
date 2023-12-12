#1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가, 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력

a = int(input())
sum = 0

for i in range(1, 1001):
  sum += i
  if sum >= a:
    break


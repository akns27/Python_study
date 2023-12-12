#백준 2747
def fibo(n):
  if n <= 1:
    return n
  
  fiboList = [0] * (n+1)
  fiboList[0] = 0
  fiboList[1] = 1

  for i in range(2, n+1):
    fiboList[i] = fiboList[i-1] + fiboList[i-2]

  return fiboList[n]

insert = int(input())
result = fibo(insert)
print(result)


#백준 10870

def fivonacci(num):
  if num == 0:
    return num
  if num == 1:
    return num
  return fivonacci(num - 1) + fivonacci(num - 2)

n = int(input())
print(fivonacci(n))
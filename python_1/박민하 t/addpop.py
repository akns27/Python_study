#입력받은 값을 모두 더하는 코드

def add(a):
  if len(a) == 0:
    return 0
  num = a.pop()
  return num + add(a)

a = list(map(int, input().split()))
result = add(a)
print(result)

"""
def add(a):
  if len(a) == 0:
    return 0
  num = a.pop()
  return num + add(a)

if __name__ == "__main__":
  b = list(map(int, input().split()))
  result = add(b)
  print(result)

"""


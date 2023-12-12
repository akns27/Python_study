"""
def f(a,b):
    while(b!=0):
      a, b = b, a%b
    return a

a, b = map(int, input().split())
print(f(a,b))
"""
#선생님의 코드
a,b = map(int, input().split())

while a%b !=0:
  a,b= b, a%b

print(b)
a, b, c = map(int, input().split())
def f(a,b):
    while(b!=0):
      a, b = b, a%b
    return a


save = f(a,b)
print(f(save, c))

#3개있으면 2개를 해서 하나로 만들고 이 하나를 나머지랑
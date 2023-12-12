stack_size = 5
list=[None]*stack_size
top = -1

def isEmpty():
  global top
  if top == -1:
    return True
  else:
    return False

def isFull():
  global stack_size
  global top
  if top == stack_size-1 :
    return True
  else:
    return False
"""
return top == stack_size-1해도 됨
"""

def push(e):#매개변수 e, push(매개변수)로 넣기
  global top
  if isFull():
    print("스택이 가득찼습니다.")
  else:
    top = top+1
    list[top] = e

def pop():
  global top
  if isEmpty():
    print("스택이 비어있습니다.")
  else:
    top = top-1
    return list[top+1]#top-1해서 빼준 거 다시 반환
# 파이썬에서만 함수 안에 global로 선언해줘야함
def peek():
  if not isEmpty():
    return list[top]
  else:
    pass


push(1)
push(2)
push(3)#push(매개변수)
print(pop())
print(peek())
print(pop())


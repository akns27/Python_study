#중위 표기 -> 후위 표기
#(a+b)*c -> ab+c*

#1. a+b*c -> abc*+
#2. a*b+c -> ab*c+
#3. (a+b)*c -> ab+c*

class stack:
  def __init__(self, stack_size):#생성자
    self.stack_size = stack_size
    self.list=[None]*stack_size
    self.top = -1
#class내의 요소에 접근하려면 self를 꼭 적어줘야함
  def isEmpty(self):#1개
    return self.top == -1
  #True, False로 결과가 나옴
  def isFull(self):#2개
    return self.top == self.stack_size-1


  def push(self,e):#매개변수 e, push(매개변수)로 넣기, 3개
    #정의할때만 self적어주면 됨
    if self.isFull():#호출할때는 self없는 셈
      print("스택이 가득찼습니다.")
    else:
      self.top = self.top+1
      self.list[self.top] = e

  def pop(self):#4개
    if self.isEmpty():
      print("스택이 비어있습니다.")
    else:
      self.top = self.top-1
      return self.list[self.top+1]#top-1해서 빼준 거 다시 반환, 사용자에게 돌려줌 -> 사용자는 돌려받은걸 출력하거나 함

  def peek(self):#5개
    if self.isEmpty():
      print("스택이 비어있습니다.")
    else:
      return self.list[self.top]
    
  
  #연산자 우선 순위 계산 함수
def precedence(op):
  if op == '*' or op == '/' : return 2
  elif op == '+' or op == '-' : return 1
  elif op == '(' or op == ')' : return 0
  else : return -1
  
  #중위표기 -> 후위표기로 바꾸는 함수
def Infix2postfix(expr):
    s = stack(100)#a라는 거에 원래 있던 stack이라는 이름의 스택을 찍어냄
    output = []#결과물을 찍어낼 리스트
    for term in expr: #표현식을 순서대로 순회, term을 expr만큼 순회
      if term == '(':
        s.push('(')#term 을 push해도 됨

      elif term in ')':
        while not s.isEmpty():#스택이 비어있지 않다면 왼쪽 괄호가 나올 때까지 pop, 괄호를 먼저 처리해야 하므로
          op = s.pop()
          if op == '(':
            break
          else:
            output.append(op)#output이라는 리스트의 제일 뒤에 op를 추가함, 스택이 아닌 리스트라서 append씀

      elif term in "*/+-":
        while not s.isEmpty():#스택이 안 비어있다면
          op = s.peek()#op에 담아서 비교
          if( precedence(term) <= precedence(op)):#현재 가장 스택 위에 있는 요소와 입력받는 걸 비교해서 스택 위에 있는게 크거나 같다면
            output.append(op)#op를 아웃풋에 append 해주고
            s.pop()#삭제해줘야지 완전히 처리된거임
          else: break#아니면 끝
        s.push(term)
      else:
        output.append(term)

    while not s.isEmpty():
      output.append(s.pop())
    return output

infix1=input()#중위
infix1=list(infix1)
postfix1=Infix2postfix(infix1)
print(*postfix1)
#리스트 기반으로 입력받아서 리스트로 출력

"""
박강원의 생각 알고리즘

  #연산자 우선 순위 계산 함수ㅁ+
  def precedance(op):
    op.priority = {}
  #우선 순위를 일단 미리 지정해주는 게 더 편할 듯
  #stack에 입력받은 연산자를 넣음, 
  #만약 입력받은 연산가가 이미 들어가있던 연산자보다 우선 순위가 나중이면 바로 우선 순위가 빠른 연산자를 pop시킨다
  #괄호는 그냥 무시
  
  #중위표기 -> 후위표기로 바꾸는 함수
  def Infix2postfix(expr):
    #연산자면 predance함수 불러서 넣고, 아니라면 아래 코드 실행
    #output에 수를 넣는다
    #숫자 다 넣었다면 연산자 전부 pop
"""
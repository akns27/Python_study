class stack:
  def __init__(self, stack_size):#클래스를 만들겠다.
    self.stack_size = stack_size#stack_size지정
    self.list=[None]*stack_size#stack_size만큼 None으로 초기화
    self.top = -1#top을 -1로 초기화
#class내의 요소에 접근하려면 self를 꼭 적어줘야함
  def isEmpty(self):#1개
    return self.top == -1 #top이 -1이라면 true 아니면 false
  #True, False로 결과가 나옴
  def isFull(self):#2개
    return self.top == self.stack_size-1#top이 stack_size -1(배열이라 0부터 시작) 이라면 가득 찬거임


  def push(self,e):#매개변수 e, push(매개변수)로 넣기, 3개
    #정의할때만 self적어주면 됨
    if self.isFull():#호출할때는 self없는 셈치기
      print("스택이 가득찼습니다.")
    else:
      self.top = self.top+1 #top +1해주기 
      self.list[self.top] = e#top +1 해준 자리에 e라는 걸 넣기,e는 사용자가 넣는 것

  def pop(self):#4개
    if self.isEmpty():#비어있다면
      print("스택이 비어있습니다.")
    else:
      self.top = self.top-1#top을 -1해줌
      return self.list[self.top+1]#top-1해서 빼준 거 다시 반환, 사용자에게 돌려줌 -> 사용자는 돌려받은걸 출력하거나 함

  def peek(self):#5개
    if self.isEmpty():#비었다면
      print("스택이 비어있습니다.")
    else:
      return self.list[self.top]#top 반환
    
  def printAll(self):#6개
    if self.isEmpty():#비었다면
      print("스택이 비어있습니다.")
    else:
      for i in range(self.top, -1, -1):#top에서 -1까지, -1씩 줄어들며
        print(self.list[i])#리스트를 출력하기

  def clear(self):#7개, 전부 없애기 기능
    if self.isEmpty():
      print("큐가 이미 비어있습니다.")
    self.top = -1#top도 초기화
    self.list = [None]*self.stack_size#리스트에 none을 넣으며 초기화(Stack_size만큼 초기화)

  def size(self):#8개, 스택 안 요소의 개수 반환
    if self.isEmpty():
      print("큐가 이미 비어있습니다.")
    return self.top + 1#top에 0부터 시작하니 +1을 하면 현재 요소의 개수가 나옴
  
#반환값이 없는 함수에 print를 씀으로써 none이 나오던 문제가 해결됨

classInstance = stack(5)#매개변수 stack_size 값 전달

classInstance.push(1)
classInstance.push(2)
classInstance.push(3)
classInstance.push(4)
classInstance.push(5)
print(classInstance.pop())
print(classInstance.peek())
print(classInstance.pop())
classInstance.printAll()
print(classInstance.size())
classInstance.clear()
print(classInstance.size())
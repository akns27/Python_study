#덱은 front와 rear에서 삭제&삽입 둘 다 할 수 있다.

class Deque:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity  # 큐의 최대 크기
        self.list = [None] * capacity  # 큐의 요소를 저장할 리스트
        self.front = 0  # 큐의 앞부분을 가리키는 인덱스
        self.rear = 0   # 큐의 뒷부분을 가리키는 인덱스
        # 프론트와 리어 초기화

    
    def isEmpty(self):
        return self.front == self.rear#프론트와 리어가 같으면 비어있음
    def isFull(self):#프론트 위치와 다음 요소를 추가할 위치가 같다면 가득참
        return self.front == (self.rear+1)%self.capacity
    def addFront(self, e):
        if not self.isFull():#가득 차지않았다면
            self.list[self.rear] = e  # 현재 rear 위치에 
            self.rear += 1#입력받은 요소 추가
        else:
            print("덱이 가득 찼습니다.")
    
    def deleteFront(self):
        if not self.isEmpty():
            self.rear -= 1#rear가 -1를 가리키게하고
            item =  self.list[self.rear]#삭제할 요소를 아이템에 저장
            self.list[self.rear] = None#원래 있던 곳은 None으로
            return item#제거된 요소 리턴
            
        else:
            print("덱이 비어있습니다.")
    
    def addRear(self, e):
        if not self.isFull():#가득 차지 않았다면
            self.front -= 1 #front가 -1(=앞쪽)을 가리키게하고
            self.list[self.front] = e#입력받은 요소를 넣기
            
        else:
            print("덱이 가득 찼습니다.")


    def deleteRear(self):
        if not self.isEmpty():#비어있지 않다면
            item =  self.list[self.front]#삭제할 요소를 아이템에 저장
            self.list[self.front] = None#self.front(=원래 위치)에 있던 것을 None으로 만들기
            self.front +=  1#front가 다음 요소를 가리키게하고
            return item#제거된 요소 리턴
            
        else:
            print("덱이 비어있습니다.")


queue = Deque(5)

queue.addFront(1)
queue.addFront(2)
queue.addRear(3)
queue.addRear(4)
queue.addRear(5)


print(queue.list)

queue.deleteRear()

print(queue.list)

queue.deleteFront()

print(queue.list)
"""
출력 결과
[1, 2, 5, 4, 3]
[1, 2, None, 4, 3]
[1, None, None, 4, 3]
"""
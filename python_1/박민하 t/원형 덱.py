
class Deque:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity  # 큐의 최대 크기
        self.list = [None] * capacity  # 큐의 요소를 저장할 리스트
        self.front = -1  # 큐의 앞부분을 가리키는 인덱스 초기화
        self.rear = 0   # 큐의 뒷부분을 가리키는 인덱스 초기화

    def isEmpty(self):
        return self.front == self.rear#프론트와 리어가 같으면 비어있음
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity

    def addFront(self, e):
        if not self.isFull():
            if self.front == -1:
                self.front = 0
            self.front = (self.front - 1) % self.capacity  # 원형 덱에서 앞쪽으로 이동
            self.list[self.front] = e  # 현재 front 위치에 요소 추가

    def deleteFront(self):
        if not self.isEmpty():
            item = self.list[self.front]  # 삭제할 요소를 아이템에 저장
            self.list[self.front] = None  # 원래 있던 곳은 None으로
            if self.front == self.rear:  # 마지막 요소를 삭제한 경우
                self.front = -1
                self.rear = 0
            else:
                self.front = (self.front + 1) % self.capacity  # front를 다음 요소로 이동
            return item  # 제거된 요소 리턴

    def addRear(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity  # 원형 덱에서 뒤쪽으로 이동
            self.list[self.rear] = e  # 입력받은 요소를 넣기

    def deleteRear(self):
        if not self.isEmpty():
            item = self.list[self.rear]  # 삭제할 요소를 아이템에 저장
            self.list[self.rear] = None  # self.rear(=원래 위치)에 있던 것을 None으로 만들기
            if self.front == self.rear:  # 마지막 요소를 삭제한 경우
                self.front = -1
                self.rear = 0
            else:
                self.rear = (self.rear - 1) % self.capacity  # rear를 이전 요소로 이동
            return item  # 제거된 요소 리턴

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
원형덱은 선형덱과 달리 공간이 낭비됨

원형 덱에서는 공간이 하나 낭비되는 이유는 원형 덱의 데이터는 원형으로 저장되기 때문입니다. 원형 덱의 데이터는 첫 번째 요소 다음에 마지막 요소가 이어지는 형태로 저장됩니다. 따라서 데이터의 삽입, 삭제, 검색 등의 작업을 수행할 때 데이터의 위치를 계산하기가 더 복잡합니다.

원형 덱에서 데이터의 위치를 계산하기 위해서는 데이터의 순서를 고려해야 합니다. 예를 들어, 원형 덱의 첫 번째 요소 다음에 데이터를 삽입하려면 데이터의 순서를 고려하여 데이터를 삽입해야 합니다. 따라서 원형 덱에서는 데이터의 위치를 계산하기 위한 공간이 하나 필요합니다.
"""
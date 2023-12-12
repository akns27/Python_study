class LinearQueue:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity  # 큐의 최대 크기
        self.list = [None] * capacity  # 큐의 요소를 저장할 리스트
        self.front = 0  # 큐의 앞부분을 가리키는 인덱스
        self.rear = 0   # 큐의 뒷부분을 가리키는 인덱스
				# 프론트와 리어 초기화

    # 큐가 비었는지 확인, 1개
    def isEmpty(self):
        return self.front == self.rear#프론트와 리어가 같으면 비어있음

    # 큐가 가득 찼는지 확인, 2개
    def isFull(self):
        return self.rear == self.capacity#리어와 큐의 최대 크기외 같으면 가득 차 있음

    # 큐에 원소를 추가, 3개
    def enQueue(self, item):
        if not self.isFull():#가득 차지않았다면
            self.list[self.rear] = item  # rear에 요소 추가
            self.rear += 1 #인덱스를 증가시킴
        else:
            print("큐가 가득 찼습니다. 엔")

    # 큐에서 원소를 제거
    def dequeue(self):
        if not self.isEmpty():  # 큐가 비어있지 않다면
            item = self.list[self.front]  # front 위치의 요소를 item에 저장
            self.front += 1  # front 인덱스를 증가시켜 요소를 제거
            return item  # 제거된 요소를 반환
        else:
            print("큐가 비어있습니다. 디")


    # 큐의 맨 앞 원소를 반환
    def peek(self):
        if self.isEmpty():
            print("큐가 비어있습니다. 픽")
        else:
            return self.list[self.front]#가장 위의 값인 프론트 반환

    # 큐의 모든 요소를 출력
    def queue_print_all(self):
        if self.isEmpty():
            print("큐가 비어있습니다. 프")
            return
        for i in range(self.front, self.rear):#front에서 rear까지
            print(self.list[i], end=' ')#리스트의 요소를 전부 출력
        print()#줄바꿈

    # 큐를 초기화
    def clear(self):
        if self.isEmpty():
            print("큐가 이미 비어있습니다. 클")
        self.front = self.rear  # front와 rear를 같은 위치로 설정
        self.list = [None] * self.capacity  # 리스트를 초기화

    # 큐에 들어있는 요소의 개수 반환
    def size(self):
        return self.rear - self.front

# 선형 큐 생성 및 요소 추가
queue = LinearQueue(5)

queue.enQueue(1)
queue.queue_print_all()
queue.enQueue(2)
queue.queue_print_all()
queue.enQueue(3)
queue.queue_print_all()
queue.enQueue(4)
queue.queue_print_all()
queue.enQueue(5)
queue.queue_print_all()
queue.dequeue()
queue.queue_print_all()
queue.dequeue()
queue.queue_print_all()
queue.dequeue()
queue.queue_print_all()
queue.dequeue()
queue.queue_print_all()
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 

위의 테스트 코드와 연결해서 실행시킬 때 결과
"""

queue.enQueue(1)
queue.enQueue(2)
print(queue.peek())
queue.enQueue(3)
queue.enQueue(4)
queue.dequeue()
queue.queue_print_all()
print(queue.size())
queue.clear()
print(queue.size())

"""
큐가 가득 찼습니다. 엔
큐가 가득 찼습니다. 엔
5
큐가 가득 찼습니다. 엔
큐가 가득 찼습니다. 엔
큐가 비어있습니다. 프
0
큐가 이미 비어있습니다. 클
0
"""


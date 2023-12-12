class CircularQueue:
    def __init__(self, capacity):#생성자 __init__
        self.capacity = capacity#max_queue_size와 같은 역활
        self.list = [None] * capacity#capacity크기만큼 초기화된 리스트를 만들어 줌
        self.front = 0
        self.rear = 0
				#front와 rear를 초기화
    def isEmpty(self):#1개, 큐가 비었는지 확인하는 함수/ front와 rear가 같으면,,,, 비어있음
        return self.front == self.rear#동일하면 true 아니면 false반환

    def isFull(self): #2개, 큐가 가득 찼는지 확인하는 함수
        return (self.rear + 1) % self.capacity == self.front#rear + 1(=다음 값) 이 front와 같다면 가득 참, %self.capacity는 원형 큐를 넘을 때를 고려한 코드 

    def enQueue(self, item):#3개, 큐에 원소를 넣는 함수
        if not self.isFull():#꽉 차지 않았다면
            self.rear = (self.rear + 1) % self.capacity#리어의 다음 값을 가리키게 %self.capacity는 원형 큐를 넘을 때를 고려한 코드 
            self.list[self.rear] = item#리어가 가리키고 있는 곳에 새로운 아이템(=요소)를 넣어줌
        else:
            print("큐가 가득 찼습니다.")

    def dequeue(self):#4개, 큐에 원소를 제거하는 함수
        if not self.isEmpty():#비어있지 않다면
            self.front = (self.front + 1) % self.capacity#프론트가 가리키고 있는 값에 
            return self.list[self.front]#다음 값을 넣어줌
        else:
            print("큐가 비어있습니다.")
    
    def peek(self):#5개, 큐의 맨 앞 원소를 반환하는 함수
        if self.isEmpty():#비었다면
            print("큐가 비어있습니다.")
        else:
            return self.list[self.rear]#top요소, 즉 rear를 반환


    def queue_print_all(self):#6개, 큐 속 요소 전부 출력
        if self.isEmpty():#비었다면
            print("큐가 비어있습니다.")
            return
        i = self.front#i를 front로 초기 설정
        while True:#무한 반복
            i = (i + 1) % self.capacity#i의 값 하나씩 늘려가며
            print(self.list[i], end=' ')#리스트 출력
            if i == self.rear:#프론트와 리어가 같으면 
                break#멈춤
        print()#줄 바꿈
    
    def clear(self):#7개, 큐 속 원소 전부 제거
        if self.isEmpty():#비어있다면
            print("큐가 이미 비어있습니다.")
        self.front = self.rear#front와 rear를 처음처럼 같은 곳에 두고
        self.list = [None]*self.capacity#리스트 크기만큼 None으로 초기화 
    
    def size (self):#8개, 현재 큐에 들어가있는 원소의 개수 반환
        if self.isEmpty():#비었다면
            print("큐가 이미 비어있습니다.")
        elif self.front <= self.rear:#rear가 front보다 크면
            return self.rear - self.front#front를 빼주기만 하면 됨
        else:#front가 rear보다 클 때
            return (self.capacity - self.front + self.rear+1) % self.capacity#개수 반환

# 원형 큐 생성 및 요소 추가
queue = CircularQueue(5)


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
실행결과

1 
1 2 
1 2 3 
1 2 3 4 
큐가 가득 찼습니다.
1 2 3 4 
2 3 4 
3 4 
4 
큐가 비어있습니다.
"""

queue.enQueue(1)
queue.enQueue(2)
print(queue.peek())
queue.enQueue(3)
queue.enQueue(4)
queue.queue_print_all()
print(queue.size())
queue.clear()
queue.size()

"""
실행결과
2#peek
1 2 3 #queue_print_all
3
#clear
큐가 이미 비어있습니다#size.
"""
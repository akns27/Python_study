class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0  # 추가된 플래그: 큐에 저장된 요소의 개수를 추적

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enQueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.list[self.rear] = item
            self.size += 1  # 요소가 추가될 때마다 크기 증가
        else:
            print("큐가 가득 찼습니다.")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            item = self.list[self.front]  # 반환할 아이템 저장
            self.list[self.front] = None  # 반환된 위치를 None으로 설정
            self.size -= 1  # 요소가 제거될 때마다 크기 감소
            return item
        else:
            print("큐가 비어있습니다.")

    def queue_print(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
            return
        i = self.front
        while True:
            i = (i + 1) % self.capacity
            print(self.list[i], end=' ')
            if i == self.rear:
                break
        print()

# 테스트 코드는 동일하게 사용
queue = CircularQueue(5)
queue.enQueue(1)
queue.queue_print()
queue.enQueue(2)
queue.queue_print()
queue.enQueue(3)
queue.queue_print()
queue.enQueue(4)
queue.queue_print()
queue.enQueue(5)
queue.queue_print()
queue.enQueue(5)
queue.queue_print()

queue.dequeue()
queue.queue_print()
queue.dequeue()
queue.queue_print()
queue.dequeue()
queue.queue_print()
queue.dequeue()
queue.queue_print()
queue.dequeue()
queue.queue_print()
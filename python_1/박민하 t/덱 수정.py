class Deque:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0

    # 프론트와 리어 초기화
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def addFront(self, e):
        if not self.isFull():
            self.list[self.front] = e
            self.front = (self.front - 1) % self.capacity
        else:
            print("덱이 가득 찼습니다.")

    def deleteFront(self):
        if not self.isEmpty():
            item = self.list[self.front]
            self.list[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return item
        else:
            print("덱이 비어있습니다.")

    def addRear(self, e):
        if not self.isFull():
            self.list[self.rear] = e
            self.rear = (self.rear + 1) % self.capacity
        else:
            print("덱이 가득 찼습니다.")

    def deleteRear(self):
        if not self.isEmpty():
            item = self.list[self.rear]
            self.list[self.rear] = None
            self.rear = (self.rear - 1) % self.capacity
            return item
        else:
            print("덱이 비어있습니다.")


if __name__ == "__main__":
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

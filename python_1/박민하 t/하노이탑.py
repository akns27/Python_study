def hanoi(n, a, b, c):#재귀함수 hanoi(n, a, b, c)를 지정
    if n == 1:#n이 1개 즉 남은 원판이 하나 일때
        print(f"Disk {n} : {a} to {c}")#a to b로 n원판을 이동한 경로
    else:#남은 원판이 하나가 아니면
        hanoi(n-1,a,c,b)  # c를 이용해서 a를 b로 이동
        print(f"Disk {n} : {a} to {c}")#a to c로 n원판을 이동한 경로
        hanoi(n-1,b,a,c)#a를 이용해서 b를 c로 이동
#n-1을 쓰는 이유는 1개인 경우는 if문으로 빠지고 2개 이상인 경우 제일 위에서 아래에 있는 원판을 n-1 지정해주는 것
if __name__ == "__main__":#이 아래 코드는 직접 실행 할때만 실행되게 하겠다.
    n = int(input())#입력
    hanoi(n,'A','B','C')#원판의 수와 기둥을 def로 보냄

#백준11729
n = int(input())
def top(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        top(n-1, a, c, b) 
        print(a, c)
        top(n-1, b, a, c)
sum = 2 ** n - 1
print(sum)
top(n, 1, 2, 3)

#백준 입력 코드 위치만 바꿈
def top(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        top(n-1, a, c, b) 
        print(a, c)
        top(n-1, b, a, c)
        
n = int(input())
sum = 2 **n -1
print(sum)
top(n, 1, 2, 3)
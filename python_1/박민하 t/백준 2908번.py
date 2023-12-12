# 입력 받기
a, b = input().split()

# 숫자를 거꾸로 뒤집기
a = int(a[::-1])
b = int(b[::-1])

# 큰 수 출력
if a > b:
    print(a)
else:
    print(b)
 
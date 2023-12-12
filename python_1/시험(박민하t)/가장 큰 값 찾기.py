def find_num(a):#find_num라는 함수 선언
  if len(a) == 0:#list의 길이가 0 => 리스트에 들어있는 값이 없다면
    return 0#0을 반환
  return max(a)#함수를 재귀적으로 반복하며 max값을 리턴

n = list(map(int, input().split()))#list로 정수를 입력받음, 띄어쓰기로 구분
result = find_num(n)#result에 find_num(n)한 값을 넣고
print(result)#result값을 출력
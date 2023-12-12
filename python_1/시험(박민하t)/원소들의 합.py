def add(a):#add라는 함수 선언
  if len(a) == 0:#list의 길이가 0 => 리스트에 들어있는 값이 없다면
    return 0#0을 반환
  num = a.pop()#pop으로 제일 마지막 수를 num에 넣음
  return num + add(a)#num + add(a), add(a)은 자기 자신을 재귀적으로 호출해서 결국은 전부 다 더해지게 만듦

n = list(map(int, input().split()))#리스트로 정수를 입력받은 띄어쓰기로 구분
result = add(n)#result에 add(n)한 값을 넣고
print(result)#result를 출력

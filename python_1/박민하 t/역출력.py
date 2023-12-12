def out(a):
  if len(a) == 0:
    return
  print(a[-1], end = ' ')#[-1]은 리스트 a의 마지막을 의미함, [-1]은 리스트 형식으로 나지 않고 그대로 역으로 바뀌어서 나옴
  out(a[:-1])#[:-1]은 마지막 숫자 앞까지를 뜻함(슬라이싱), 마지막 숫자 제외 나머지를 반환

insert = list(input().split())
out(insert)



for i in enumerate(['A', 'B', 'C']):
  print(i)
#기본적으로 enumerate()함수는 기본적으로 인덱스와 원소로 이루어진 튜플을 만들어줌

#만약 인덱스와 원소를 다른 변수에 따로 따로 넣고싶다면
for i, letter in enumerate(['a', 'b', 'c']):
  print(i, letter)
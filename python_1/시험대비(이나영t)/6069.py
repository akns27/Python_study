#평가 입력받아 다르게 출력하기
a = input()
if a =='A':
  print('best!!!')
elif a == 'B':
  print('good!!')
elif a == 'C':
  print('run!')
elif a == 'D':
  print('slowly~')
else:
  print('what?')

i = input()
print({'A': 'best', 'B': 'good', 'C': 'run', 'D': 'slowly'}.get(i,'what?'))
#앞의 딕셔너리에 입력한 값이 없으면 what 출력
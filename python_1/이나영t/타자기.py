import random
import time

WORD_LIST = [
  "따라 적어보세요",
  "즐코딩하세용",
  "겟겟겟겟어기타",
  "memoria",
  "빠빠빠빨간맛"
]
random.shuffle(WORD_LIST)

for i in WORD_LIST:#i라는 변수를 이용해서 for문을 돌릴게
  start_time = time.time()#문장이 시작된 시간을 타임 스탬프로 만들어줘
  user_input = str(input(i+'\n')).strip()#input하기 전에 뭘 따라쳐야하는 지(=i)보여주고 입력받음, .strip()은 사용자가 스페이스를 치고난 뒤 입력하거나, 입력한 뒤 스페를 할 수 있으니 .strip()이라는 공백 제거 사용
  end_time = time.time()-start_time#문장이 지금 떠있는 시간을 잰 뒤 시작시간 빼주기
  if user_input == "exit":
    break

correct=0#맞춘 개수 카운트
for index, c in enumerate(user_input):#enumerate.py참고
  if index >= len(i):
    break
  if c==i[index]:
    correct+=1
  total_len = len(i)
  c = correct/total_len*100#정확도아무
  e=(total_len-correct)/total_len*100#오타율
  speed=correct / end_time *60#오타율

  print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 {:0.2f}".format(speed, c, e))



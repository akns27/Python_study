#월 입력받아 계절 출력하기
a = int(input())
b = ['winter','spring', 'summer', 'fall']


if a//4 == 2: #//는 몫을 구하는 것
    print(b[3])#8,9,10,11
    
elif a//3 == 1:
    print(b[1])#3,4,5,
    
elif a//6 == 1:
    print(b[2])#6,7
    
else :
    print(b[0])#12,1,2

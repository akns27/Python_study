print(type(bool))
print(type(list))
print(type(tuple))
print(type(dict))
print(type(set))
list = [1, 2, 3, 4, 5] # 인덱스는 0부터 시작
print(list[1:3]) #2, 3출력
print(list[:3])#1,2,3 출력
print(list[1:])#2,3,4,5 출력

a = input()
reverse_a = ''

for i in a:
  reverse_a = i+reverse_a 

print(reverse_a)
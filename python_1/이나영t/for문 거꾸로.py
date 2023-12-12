"""
s = 'abcde'
for i in range(len(s)-1,-1,-1):
    s_rev = i + s_rev
    print(s[i], end ='')
    
"""

s ='abcde'
s_rev = ''
for i in s:#i라는 변수를 이용해서 s를 돔
  s_rev =  i + s_rev

print(s_rev, end = ' ')


"""
클래스 : 서로 관련있는 요소(변수, 기능 함수)를 한 곳에 모아서 관리하기 위한 툴
객체: 클래스 틀을 이용해서 찍어낸 실체
   -> 동일한 클래스를 이용해서 생성한 각 객체는 서로 독립적임!
메소드를 클래스 내부에 선언할 때 첫번째 매개변수는 무조건 현재 클래스의 객체가 되어야함
   -> 관습적으로 self 사용
   -> 두 번째 매개변수부터 사용자가 직접 정의해서 사용함
클래스 내부에서 본인 클래스에 속한 메소드를 호출 : self.메소드명(매개변수)



class 클래스명:
  def __init__(self, 매개변수1, ....):
            속성 정의
__init__():인스턴스를 만들 때 실행되는 초기화 함수 = 생성자/ 객체가 처음 만들어지는 순간 딱 한번만 호출되며, 객체의 초기값을 설정하는 역활 

-1-
class bssm:
  def __init__(self, name, age, position):#self는 나 자신을 호출하는 것이니 없는 거로 치기
    self.team = "부소마" #bssm 클래스로 찍어낸 객체들은 모두 team변수에 부소마가 들어가도록
    self.enname = "jake"
    self.name = name
    self.age = age
    self.position = position

  def intro(self):
      print("안녕하세요, 저는 %s의 %s이고 %d살입니다. 저는 %s을/를 담당하고있습니다. 영어 이름은 %s입니다" %(self.team, self.name, self.age, self.position, self.enname))

박강원 = bssm("박강원",17,"반장")
박강원.intro()
__________________

"""
class grade:
   def __init__(self, name, score):#틀만 만들어 주기/__init__ 초기화, 생성자 역활
    self.name = name
    self.score = score
   def s_grade(self):
      if self.score >= 90:#꼭 self 붙여주기
         self.grade="A"

      elif self.score >= 80:
         self.grade="B"

      else:
         self.grade="C"

   def __str__(self):
      return "%s: %c등급" %(self.name, self.grade)
   
a1 = grade("박강원", 88)
a1.s_grade()
print(a1)
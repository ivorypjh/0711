class Super:
    def __init__(self) -> None:
        # Super 클래스에 name 속성이 생김
        self.name = "default"
    def superClassMethod(self):
        print("상위 클래스 메서드")

# Super 클래스를 상속 받는 Sub
class Sub(Super):
    # 하위 클래스에서 init 을 생성하면 상위 클래스의 init 을 호출하지 않음
    # 하위 클래스에서 init 을 만들 때는 상위 클래스의 init 을 호출해줘야 함.
    def __init__(self) -> None:
        super().__init__() # 이 문장 없이 init 을 사용하면 에러 발생
        self.grade = "b"

    def subClassMethod(self):
        print("하위 클래스 메서드")

# Sub(하위) 클래스의 인스턴스 생성
practice = Sub()
practice.subClassMethod()
# Sub 에 없는 메서드를 상속을 통해 불러올 수 있음
practice.superClassMethod()
# Super 클래스의 속성을 상속 받아서 사용
print(practice.name)
print(practice.grade)


class Study:
    def __init__(self) -> None:
        self.name = "park"
        # 속성을 만들 때 __ 로 시작하면 인스턴스는 직접 접근 불가
        # 메서드를 사용해서만 접근할 수 있음.
        self.__age = 15
        
student1 = Study()
print(student1.name)
# private 이므로 아래 방법으로는 접근 불가능
# print(student1.__age)
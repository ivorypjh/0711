class Study:
    def __init__(self, name) -> None:
        self.name = name
    __slots__ = [name] # name 만 속성으로 만들 수 있도록 제한

student1 = Study()
# 파이썬에서는 기본적으로 클래스에 없던 속성을 생성할 수 있음.
student1.name = "park"
# 만들 수 없는 속성이므로 grade 에서 에러 발생.
# student1.grade = "B"
print(student1.name)
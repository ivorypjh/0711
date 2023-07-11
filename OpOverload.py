class Study:
    def __init__(self, name = "default") -> None:
        self.name = name
    # + 연산자에 대한 overloading
    def __add__(self, other) -> str:
        return self.name + other.name
    # == 연산자에 대한 overloading
    # id를 비교하는게 아니라 name 이 같은지 판별함
    def __eq__(self, other) -> bool:
        return self.name == other.name

student1 = Study("park")
student2 = Study("park")
# 기본적으로 연산을 할 수 없으므로 에러
# 오버로딩을 통해 이름을 더하게 됨
print(student1 + student2) 
# 기본적으로는 아래 둘 다 False
# 별도로 생성되었으므로 id가 다름
# 연산자 오버로딩을 통해 name만 비교하므로 위는 True
print(student1 == student2)
print(student1 is student2)
class Study:
    # 생성자 - 인스턴스를 생성할 때 호출하는 메서드
    # 특정한 상수로 생성하고자 하는 경우 내부에서 직접 설정
    # 매개변수를 이용해서 초기화하면 다양한 값으로 초기화 가능
    # 매개변수를 이용해서 초기화 할 때 매개변수에 기본 값을 설정하지 않으면
    # 인스턴스를 생성할 때 반드시 매개변수에 값을 대입해야 함. 
    def __init__(self, name = "default") -> None:
        print("생성자를 통해 인스턴스 생성")
        # self.name = "defalut" 이 방식의 단점은 기본값으로만 초기화 가능
        # 매개변수로 name 을 사용하고 기본값으로 'defalut' 를 설정
        self.name = name

    # 소멸자 - 인스턴스가 소멸될 때 호출되는 메서드
    def __del__(self):
        print("소멸자를 통해 인스턴스 소멸")
    def display(self):
        # 클래스에 만들어졌지만 인스턴스 없이는 호출할 수 없는 메서드
        print("인스턴스의 메서드")
    # setter - 속성을 수정하거나 생성하는 메서드
    def setName(self, name):
        # name 이라는 속성이 없으면 만들어서 대입하고 있으면 수정
        self.name = name
    # getter - 속성의 값을 사용할 수 있도록 리턴하는 메서드
    def getName(self):
        return self.name


# 인스턴스 생성
student1 = Study()
# unbound 호출 : 클래스가 인스턴스의 메서드를 호출
Study.display(student1)
# bound 호출 : self 에 인스턴스가 대입 되어서 메서드를 호출
student1.display()

stuName = student1.getName()
print(stuName) # default
student1.setName("park")
stuName = student1.getName()
print(stuName) # park
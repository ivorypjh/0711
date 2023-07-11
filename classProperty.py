class Study:
    def __init__(self, name = "defalut") -> None:
        # __ 로 시작하므로 인스턴스로 접근 불가능
        self.__name = name
        
    # property 를 데코레이터로 바로 적용
    @property # getter 설정
    def name(self):
        print("getter 호출")
        return self.__name
    
    @name.setter # setter 설정
    def name(self, name):
        print("setter 호출")
        self.__name = name

    '''
    # 데코레이터를 사용하지 않는 기존의 방식

    def getName(self):
        print("getter 호출")
        return self.__name
    def setName(self, name):
        print("setter 호출")
        self.__name = name
    
    # property 생성
    # name을 호출하면 getName 메서드가 호출되고
    # name에 값을 대입하면 setName 메서드가 호출됨.
    name = property(fget=getName, fset=setName)
    '''

student1 = Study("park")
# student1.__name = "park"   private 이므로 에러
# print(student1.__name)     마찬가지로 에러
# getter 와 setter 를 직접 호출
print(student1.getName())
student1.setName("lee")
print(student1.getName())
# property 를 이용해서 getter 와 setter 호출
# 속성을 바로 이용하는 것처럼 보이지만 사실 메서드 호출
student1.name = "bae"
print(student1.name)

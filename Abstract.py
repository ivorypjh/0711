import abc

# 추상 클래스 - 자신의 인스턴스를 생성할 수 없음.
class AbsClass(metaclass = abc.ABCMeta):
    # 추상 메서드 - 내용이 없는 메서드로 하위 클래스에서
    # 구현해서 사용해야 함.
    @abc.abstractclassmethod
    def method():
        pass
# 추상 클래스를 상속받는 클래스
# 추상 클래스를 상속받는 경우 반드시 추상 메서드를 implement 해줘야 함
class InheritClass(AbsClass):
    def __init__(self) -> None:
        print("인스턴스 생성")
    # 추상 클래스의 메서드를 구현하지 않으면 에러
    def method():
        print("추상 메서드 구현")

# 추상 클래스는 인스턴스를 만들 수 없으므로 에러
# abstract = AbsClass() 
abstract = InheritClass() # 인스턴스 생성
class Study:
    # 클래스 속성
    auto_increment = 0

    # 클래스 속성과 생성자를 이용해 일련번호 만들기
    def __init__(self) -> None:
        Study.auto_increment += 1
        self.num = Study.auto_increment

    def __del__(self) -> None:
        # 기본적으로 프로그램이 끝날 때 인스턴스도 소멸
        # 프로그램 중간에 없애려면 인스턴스에 None 을 지정하면 됨.
        print("인스턴스 소멸")

# 생성자를 통해 인스턴스가 생성되면 참조 카운트(ref count)가 1이 됨.
student1 = Study() 
print(student1.num) # 1
# 참조를 가리키는 변수에 None 을 대입하면 참조 카운트가 1 감소
# 참조 카운트가 0이 되면 인스턴스는 소멸
student1 = None 
student2 = Study()
studetn3 = student2 # 다른 변수에 대입하므로 카운트 1 증가
print(student2.num) # 2
student2 = None # 카운트가 1 감소해도 소멸되지 않음
print("프로그램 종료") 

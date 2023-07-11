class Study:
    # 클래스 속성
    auto_increment = 0
    
    @staticmethod
    def static():
        print("매개변수를 사용하지 않는 static method")

student1 = Study()
# 인스턴스를 만들 필요 없이 사용 가능한 static method
Study.static()

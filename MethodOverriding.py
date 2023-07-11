class Super:
    def classMethod(self):
        print("상위 클래스 메서드")

# Super 클래스를 상속 받는 Sub
class Sub(Super):
    # 상위 클래스에 존대하던 메서드를 하위 클래스에서 다시
    # 정의하는 overriding. 목적은 기능의 확정.
    def classMethod(self):
        # 상위 클래스의 메서드를 호출
        # 하위 클래스의 기능을 추가해서 기능 확장
        super().classMethod()
        # 상위 클래스의 메서드를 호출하지 않더라도 에러는 아님
        print("하위 클래스 메서드")

practice = Sub()
# 하위 클래스의 메서드를 실행.
# 상위, 하위 둘 다 출력
practice.classMethod() 
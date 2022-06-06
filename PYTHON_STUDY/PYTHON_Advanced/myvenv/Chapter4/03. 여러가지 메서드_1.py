# Unit 클래스
class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체마다 다른 값을 가지는 속성
    """
    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp # 비공개 속성
        self.shield = shield
        self.demage = demage
        Unit.count += 1 # 클래스 속성
        print(f"[{self.name}](이)가 생성 되었습니다.")

    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.demage}"

    # 인스턴스 메서드 (instance method)
    # 인스턴스 속성에 접근할 수 있는 메서드
    def hit(self, demage):
        # 방어막 변경
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0

        # 체력 변경
        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0 

    # 클래스 메서드 (class method)
    # 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}개]")

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)

probe.hit(16)
print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)

Unit.print_count()

print(dir(probe))
# 抽象クラスのモジュール
import abc

class Person(metaclass = abc.ABCMeta):
    def __init__(self,age=1):
        self.age=age

    # def drive の実装を必須にするということで、サブクラスで必ずオーバーライド（実装）しないといけない
    # 抽象クラスは「継承されることを前提にしたクラス」
    @abc.abstractmethod
    def drive(self):
        pass
        
class Baby(Person):
    def __init__(self, age=1):
        if age < 18 :
            super().__init__(age)
        else:
            raise ValueError
        
    # personで定義した抽象クラスのdrive関数が未実装だとエラーがでる。
    # def drive(self):
    #     print("No!")
        
class Adult(Person):
    def __init__(self, age=18):
        if age >= 18 :
            super().__init__(age)
        else:
            raise ValueError
    
    # こちらはpersonで定義した抽象クラスのdrive関数が実装されているのでOK
    def drive(self):
        print("No!")
        
baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self,model=None):
        self.model = model
    def run(self):
        print("run")
    def ride(self,person):
        person.drive()

car = Car()
car.ride(adult)
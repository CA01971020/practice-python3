class Person(object):
    def talk(self):
        print("talk")

    # def run(self):
    #     print("person_run")

class Car(object):
    def run(self):
        print("run")

# PersonとCarを継承した新たなクラスPersonCarRobot
# 第一引数（左側）が優先される
class PersonCarRobot(Person, Car):
    def fly(self):
        print("fly")

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
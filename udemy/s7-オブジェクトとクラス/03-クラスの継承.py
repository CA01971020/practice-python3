class Car(object):
    def run(self):
        print("run")

# Carクラスを継承
class ToyoCar(Car):
    pass

# Carが持つメソッドと、独自のメソッドを使用できる
class TesCar(Car):
    def auto_run(self):
        print("auto run")

car = Car()
car.run()
print("#########")
# ToyoCarの親であるCarがprint("run")を持っているので、runと出力
toto_car = ToyoCar()
toto_car.run()
print("#########")
tes_Car = TesCar()
tes_Car.run()
tes_Car.auto_run()
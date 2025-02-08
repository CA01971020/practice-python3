class Car(object):
    def __init__(self,model=None):
        self.model = model
    def run(self):
        print("run")

# Carクラスを継承
class ToyoCar(Car):
    def run(self):
        print("fast")
    pass

# Carが持つメソッドと、独自のメソッドを使用できる
class TesCar(Car):
    def __init__(self, model="Model S",enable_auto_run=False):
        # 親を呼び出す
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
    ## 親のクラスを上書きできる
    def run(self):
        print("super fast")
    def auto_run(self):
        print("auto run")

car = Car()
car.run()
print("#########")
# ToyoCarの親であるCarがprint("run")を持っているので、runと出力
toyo_car = ToyoCar("Lexus")
print(toyo_car.model)
toyo_car.run()
print("#########")
tes_Car = TesCar("Model S")
print(tes_Car.model)
tes_Car.run()
tes_Car.auto_run()
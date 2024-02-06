class Vehicle:
    def __init__(self, started=False, speed=0) -> None:
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def increase_speed(self, delta: int):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooom!')
        else:
            print('You need to start the car first')

    def stop(self):
        self.speed = 0
        print('Halting')


class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True

    def close_trunk(self):
        self.trunk_open = False


class Motorcycle(Vehicle):
    def __init__(self, center_stand_out=False) -> None:
        self.center_stand_out = center_stand_out
        super().__init__()

    def start(self):
        print('Sorry, out of fuel!')


car = Car()
car.increase_speed(10)
car.start()
car.increase_speed(40)
car.stop()

car1 = Car()

print(id(car))
print(id(car1))

c1 = Car()
c2 = Car(True)
c3 = Car(True, 50)
c4 = Car(started=True, speed=40)

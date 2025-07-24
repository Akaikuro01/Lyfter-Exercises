class Engine:
    def start_engine(self):
        print("Engine started.")

class Radio:
    def play_radio(self):
        print("Playing radio.")


class Car(Engine, Radio):
    def drive(self):
        print("Car is driving.")


my_car = Car()
my_car.start_engine()   
my_car.drive()          
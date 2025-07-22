class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Bus():    
    def __init__(self):
        self.max_passengers = 3
        self.passengers = 0
        self.person = []
    
    def add_passengers(self, Person):
        if(self.passengers < self.max_passengers):
            self.passengers += 1
            self.person.append(Person)
            print(f"Current passengers: {self.passengers}")
        else:
            print("The bus is full!")


new_person = Person("Luffy", 19)
new_person1 = Person("Nami", 20)
new_person2 = Person("Chopper", 17)
new_person3 = Person("Ussop", 19)
new_bus = Bus()
new_bus.add_passengers(new_person)
new_bus.add_passengers(new_person1)
new_bus.add_passengers(new_person2)
new_bus.add_passengers(new_person3)
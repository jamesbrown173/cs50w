class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 8)
j = Point(5, 9)

# print(p.x, p.y)
# print(j.x, j.y)


class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Fred", "Mike", "Steve", "Bastille"]
for person in people:
    if flight.add_passenger(person):
        print(f"added {person} to flight")
    else:
        print(f"no room for {person}")

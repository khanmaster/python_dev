class Car:
    def __init__(self, max_speed):
        self._speed = 0
        self.max_speed = max_speed

    def get_speed(self):
        return self._speed

    def accelerate(self, speed_increase):
        print("Vrrrm!")
        if self._speed + speed_increase > self.max_speed:
            self._speed = self.max_speed
        else:
            self._speed += speed_increase

    def brake(self, speed_decrease):
        print("Screeeeech!")
        if self._speed - speed_decrease < 0:
            self._speed = 0
        else:
            self._speed -= speed_decrease

#   Alternate accelerate method - more concise but less obvious what it's doing:
#
#     def accelerate(self, speed_increase):
#         self._speed = min(self.max_speed, self._speed + speed_increase)


reliant_robin = Car(85)
print(reliant_robin.get_speed())
reliant_robin.accelerate(30)
print(reliant_robin.get_speed())
reliant_robin.brake(15)
print(reliant_robin.get_speed())
reliant_robin.accelerate(30)
print(reliant_robin.get_speed())
reliant_robin.accelerate(200)
print(reliant_robin.get_speed())

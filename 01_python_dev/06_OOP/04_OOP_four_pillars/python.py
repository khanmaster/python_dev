from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def constrict(self):
        return "and .. squeeez..."

    def digest_large_prey(self):
        return "yum..... yumm yummyyy"

    def clim(self):
        return "up we go....."

    def shed_skin(self):
        return "time to grow out of myself...!"

python_object = Python()

print(python_object.breathe())
# if we put an _use_tongue_to_smell method it should not be available in python

# key concept is we need to know how to drive a car but don't need to know how the engine works

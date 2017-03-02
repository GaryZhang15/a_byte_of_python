class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        """
        say hi
        """
        print('Hello, my name is', self.name)

p = Person('Gary Zhang')
p.say_hi()

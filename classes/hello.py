# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
    
# jerry = Dog(name="Jerry", breed="labrodor")

# jerry.name
# jerry.breed

class Dog:
    def __init__(self, name):
        self.name = name
dog1 = Dog("buddy")
dog2 = Dog(name="Max")

print(dog1.name)
print(dog2.name)

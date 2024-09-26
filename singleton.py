# Singleton pattern in Python it is a design pattern ensures that a class has only one instance and provides a global point of access to it.
class Singleton:
    __instance = None

    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
singleton1 = Singleton.getInstance()
singleton2 = Singleton.getInstance()

print(singleton1 == singleton2)  # Output: True

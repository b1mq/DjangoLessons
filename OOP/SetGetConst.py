
class Person:
    __slots__ = ("__name","__age")
    def __init__(self)->None:
        self.__name = "name"
        self.__age = 0
    @property #getter
    def set_Name(self)->str:
        return self.__name
    @property #setter
    def set_Name(self,newName:str):
        self.name = newName
        
    @property #getter
    def get_Age(self)->str:
        return self.__age
    @property #setter
    def set_Age(self,new_Age:str):
        self.__age = new_Age
    def __str__(self)->str:
        return f"Hello my name is {self.name} my age is{self.age}."
        
class Student(Person):
    __slots__ = ("__grades")
    def __init__(self):
        super.__init__(self)
        self.__grades = dict
    @property #getter
    def get_Grades(self)->dict:
        return self.__grades
    @property #setter
    def set_Grades(self,newGrades:str):
        self.__grades = newGrades
    def __str__(self)->str:
        return f"Hello my name is {self.name} my age is{self.age}."
        
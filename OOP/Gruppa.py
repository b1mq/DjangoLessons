from SetGetConst import Student
class Grupp:
    __slots__ = ("__name","__course","__students")
    def __init__(self):
        self.__name = "Group"
        self.__course = "C++"
        self.__students = []
    @property #getter
    def set_Name(self)->str:
        return self.__name
    @property #setter
    def set_Name(self,newName:str):
        self.name = newName
            
    @property #getter
    def get_Course(self)->str:
        return self.__course
    @property #setter
    def set_Course(self,new_course:str):
        self.__course = new_course
    @property #getter
    def get_Students(self):
        return self.__students
    @property #setter
    def set_Student(self,Student:Student):
        self.__students.append(Student)
    
    def __str__(self)->str:
        return f"Hi im group {self.__name} course {self.__course}"
    def __getitem__(self, index: int) -> Student:
        return self.__students[index]
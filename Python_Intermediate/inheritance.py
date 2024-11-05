class Student:
    id =1001
    def __init__(self,name):
        self.id = Student.id
        Student.id += 1
        self.name = name
    def __str__(self) -> str:
        return f"Student_ID: {self.id}, Student_Name: {self.name}"
        
class Enrollemnt(Student):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course
        
    def __str__(self) -> str:
        text = super().__str__()
        text+= f", Student_Course: {self.course}"
        return text
    
if __name__ == "__main__":
    s1 = Enrollemnt("Geon","CS")
    print(s1)
from abc import ABC ,abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print(" age must be greter than 0!")

    @abstractmethod
    def display_info(self): pass


class Student(Person):
    def __init__(self, student_id, name, age, department, gpa):
        super().__init__(name, age)
        self.__id = student_id
        self.__department = department
        self.__gpa = gpa

    @property
    def id(self):
        return self.__id

    @property
    def department(self):
        return self.__department

    @property
    def gpa(self):
        return self.__gpa

    @department.setter
    def department(self, new_department):
        self.__department = new_department

    @gpa.setter
    def gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
        else:
            print(" المعدل لازم بين 0.0 و 4.0")


    def display_info(self):
        return f"ID: {self.id} | name:{self.name} | age:{self.age} | dpt:{self.department} | gpa:{self.gpa}"



class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(" اضيف الطالب بنجاح!\n")

    def show_all(self):
        if not self.students:
            print(" لا يوجد طلاب مسجلين.\n")
        else:
            print("\n قائمة الطلاب:")
            for s in self.students:
                print(s.display_info())
            print()

    def update_student(self, student_id, new_name=None, new_age=None, new_department=None, new_gpa=None):
        for s in self.students:
            if s.id == student_id:
                if new_name:
                    s.name=new_name
                if new_age is not None:
                    s.age=new_age
                if new_department:
                    s.department=new_department
                if new_gpa is not None:
                    s.gpa=new_gpa
                print(" تم تحديث بيانات الطالب.\n")
                return
        print(" لم يتم العثور على الطالب.\n")

    def delete_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                self.students.remove(s)
                print("🗑 تم حذف الطالب.\n")
                return
        print(" لم يتم العثور على الطالب.\n")




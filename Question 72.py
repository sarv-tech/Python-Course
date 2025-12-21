# Q. Create a class Student with private attributes _name, _roll_no, and _marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 & name cannot be empty).


class Student:
    def __init__(self, name, roll_no, marks):        # Constructor
        self.__name = name                # private
        self.__roll_no = roll_no          # private
        self.__marks = marks              # private

    def get_name(self):                   # getter
        return self.__name

    def get_roll_no(self):                # getter
        return self.__roll_no

    def get_marks(self):                   # getter
        return self.__marks

    def set_name(self, name):               # setter
        if name.strip() != "":
            self.__name = name
        else:
            print("Name Cannot be Empty")

    def set_marks(self, marks):                # setter
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks Cannot be negative")

    def set_roll_no(self, roll_no):              # setter
        if roll_no >= 1 and roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must to be between 1 and 100")

s = Student("Sarvesh Pingale", 231229, 81)      # create object of class Student
s.set_marks(90)                             # update setter

print(s._Student__name, s._Student__roll_no, s._Student__marks)
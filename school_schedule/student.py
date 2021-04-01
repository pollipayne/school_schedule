from typing import NoReturn


class Student:
    def __init__(self, name, grade, classes = None):
        if self.classes == None:
            self.classes = []
        else: 
            self.classes = classes
        if grade == "9":
            self.grade = "Freshman"
        elif grade == "10":
            self.grade = "Sophomore"
        elif grade == "11":
            self.grade = "Junior"
        elif grade == "12":
            self.grade = "Senior"
        elif self.grade.isnumeric():
            raise TypeError 
        else: 
            self.grade = grade  

        self.name = name
         
        
        #possible test cases: 
        # happy case: valid results for valid parameters 
        # class list not passed, still gives empty one 
        # year passes as int, not string - out of range 
        # year passes as int, not string, in range btwn 9-12




    def add_class(self, new_class):
        self.classes.append(new_class)
        return self.classes


    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        print("A string of some things about student.")

    def display_classes(self):
        print(self.classes) 


    
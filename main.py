from school_schedule.student import Student 
from school_schedule.middleschoolstudent import MiddleSchoolStudent

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")
quinn.get_num_classes()
quinn.summary()

# second instance
claire = MiddleSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ], True
            )

claire.get_num_classes()
claire.summary()



# Extra:
# - create a function that will return the student with more classes
# - create a test for that function
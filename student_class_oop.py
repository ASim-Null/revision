#Write a base class to represent a student.
#As a minimum a student has a name and age and a unique ID.
#Create a new subclass from student to represent a concrete student doing a specialization, for example:
#Software Student and Data Science student.
import statistics
class Student:
    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
class CFGStudent(Student):
    def __init__(self, name, age,id, subjects,specialisation):
        super().__init__(name, age, id, subjects)
        self.subjects = subjects
        self.average_mark = 0
        self.specialisation = specialisation
    def add_subject(self,new_subject,new_grade):
        self.subjects[new_subject] = new_grade
        pass
    def remove_subject(self,pop_subject):
        if pop_subject in self.subjects.keys():
            self.subjects.pop(pop_subject)
        else:
            print("This subject does not exist. Please enter a valid subject.")
        pass
    def view_allsubjects(self):
        print("Below is the list of all the subjects for the student:")
        print(self.subjects.keys())
        pass
    def avg_mark(self):
        values = self.subjects.values()
        marks_list = list(values)
        average_mark = statistics.mean(marks_list)
        return average_mark
        pass
subjects = {'Maths':50, 'English': 70}
Lakshika = CFGStudent('Lakshika', 25, 'E45',subjects,'Software')
Lakshika.add_subject('French', 90)
Lakshika.view_allsubjects()
Lakshika.remove_subject('French')
Lakshika.view_allsubjects() #view after removing a subject
avg_score = Lakshika.avg_mark()
print("Average score:",avg_score)

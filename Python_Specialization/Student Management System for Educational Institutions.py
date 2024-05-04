# Define a class for a person
class personne:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    def display(self):
        print(f"Your name : {self.Name}\nYour age is : {self.Age}")


# Define a class for a student, inheriting from personne
class Student(personne):

    def __init__(self, Name, Age, Subjects=None, Scores=None, Timings=None, Absences=None, Status=None):
        super().__init__(Name, Age)
        self.Subjects = Subjects or []
        self.Scores = Scores or []
        self.Timings = Timings or []
        self.Absences = Absences or []
        self.Status = Status

    def display(self):
        super().display()
        for subject, score, timing, absence in zip(self.Subjects, self.Scores, self.Timings, self.Absences):
            print(f"Subject: {subject}, Score: {score}, Timing: {timing}, Absence: {absence}")
        print(f"Status: {self.Status}")

    def justify_absence(self, Subject, proof):
        if Subject not in self.Subjects:
            print("The student does not have this Subject in his programme")
        else:
            Abscence_proof = [Subject, proof]
            print(tuple(Abscence_proof))

    def Grade(self):
        Grade = sum(self.Scores) / len(self.Scores)
        print("Your Grade is :", Grade)
        return Grade


# Define a class for an employee, inheriting from personne
class employee (personne):
    def __init__(self,Name, Age, Salary):
        super().__init__(Name, Age)
        self.Salary = Salary

    def display(self):
        super().display()
        print(f"Your salary is: ${self.Salary}")



# Define a class for a group of students
class groupe:
    def __init__(self, students):
        self.students = students
        self.Nb_students = len(students)

    def display(self):
        print('The students in this group are:')
        for i in self.students:
            print(i.Name)
        print('The total number in this class is', self.Nb_students)

    def add_student(self, x):
        if self.Nb_students >= 35:
            print("Cannot add a student to this group, it is full")
        else:
            self.students.append(x)
            print("The student was added successfully!")



# Define a class for a field of study
class field:

    def __init__(self, groupes, Name):
        for element in groupes:
            if not isinstance(element, groupe):
                print("Your List should only contains objects of groupe type")
            else:
                pass
        self.Name = Name
        self.groupes = groupes
        self.Nb_groupes = len(self.groupes)

    def add_groupe(self, x):
        if len(self.groupes[-1] < 35):
            print('You still can not add an other group, the last one is not fully!')
        else:
            self.groupes.append(x)

    def best_student_field(self):
        best_student = None
        best_grade = 0

        for grp in self.groupes:
            for std in grp.students:
                if std.Grade() > best_grade:
                    best_student = std
                    best_grade = std.Grade()

        if best_student:
            print('The best student is:', best_student.Name)
        else:
            print('No student found.')

        return best_student

    def delete_groupe(self):
        global count
        for grp in self.groupes:
            for std in grp.students:
                if std.Grade() < 10:
                    count += 1
            if count > 3:
                self.groupes.remove(grp)
        print("Groups deleted with success !")



# Define a class for a school
class School:
    def __init__(self, fields, Nb_floor):
        for element in fields:
            if not isinstance(element, field):
                print("Your List should only contain objects of field type")
                return
        self.fields = fields
        self.Nb_floor = Nb_floor

    def add_floor(self):
        if self.Nb_floor >= 9:
            print("The School is full, You cannot add a new floor")
        else:
            self.Nb_floor += 1
            print("The floor was added successfully!")

class Teacher(employee, Student):


    def __init__(self, Name, Age, Salary):
        super().__init__(Name, Age, Salary)

    def display(self):
        super().display()

    def add_grade(self, student, subject, score):
        if subject in student.Subjects:
            student.Scores[student.Subjects.index(subject)] = score
            print("Score added with Success !")
        else:
            print("The student is not enrolled in this subject.")


    def field_choice_CS(self, student):
        for i in student.Subjects:
            if i == 'OOP':
                if self.Scores[i] > 10:
                    print("You are accepted !")
                else:
                    print("You are rejected !")


# Define a class for administrative operations
class Administration:


    @staticmethod
    def Decision_Filiere(student, teacher_opinion):
        subject_index = student.Subjects.index("IIR") if "IIR" in student.Subjects else -1
        if subject_index == -1:
            print(f"{student.Name} is not enrolled in the IIR program.")
            return

        absences = student.Absences[subject_index]
        if absences < 10 and teacher_opinion == "favorable":
            print(f"{student.Name} is enrolled in the IIR program.")
        else:
            print(f"{student.Name} cannot be enrolled in the IIR program.")


    @staticmethod
    def Modify_Grade(student, subject, new_grade):
        if subject in student.Subjects:
            index = student.Subjects.index(subject)
            student.Scores[index] = new_grade
            print(f"{student.Name}'s grade in {subject} has been modified to {new_grade}.")
        else:
            print(f"{student.Name} does not have a grade for {subject}.")


    @staticmethod
    def Add_Absence(student, subject):
        if subject in student.Subjects:
            index = student.Subjects.index(subject)
            student.Absences[index] += 1
            print(f"{student.Name}'s absence in {subject} has been added.")
        else:
            print(f"{student.Name} does not have a class for {subject}.")

    @staticmethod
    def Modify_Absence(student, subject, justification):
        if subject in student.Subjects:
            index = student.Subjects.index(subject)
            if justification == "Illness":
                student.Absences[index] -= 1
                print(f"{student.Name}'s absence in {subject} has been removed.")
            else:
                print(f"{student.Name} does not have an unexcused absence for {subject}.")
        else:
            print(f"{student.Name} does not have a class for {subject}.")




# Example Usage
s1 = Student("Alice", 20, ["Math", "Physics"], [15, 16], ["8:00 - 10:00", "10:00 - 12:00"], [0, 1], "New")
s2 = Student("Bob", 21, ["Chemistry", "Biology"], [14, 17], ["8:00 - 10:00", "10:00 - 12:00"], [0, 2], "Old")
g1 = groupe([s1, s2])
f1 = field([g1], "Science")
sch = School([f1], 1)

print("--- School Information ---")
print("Number of floors:", sch.Nb_floor)
sch.add_floor()
print("Number of floors after addition:", sch.Nb_floor)

print("\n--- Field Information ---")
print("Field name:", f1.Name)
print("Number of groups:", f1.Nb_groupes)

print("\n--- Group Information ---")
g1.display()

print("\n--- Student Information ---")
s1.display()

print("\n--- Administration ---")
Administration.Decision_Filiere(s1, "favorable")
Administration.Modify_Grade(s1, "Math", 18)
Administration.Add_Absence(s1, "Math")
Administration.Modify_Absence(s1, "Math", "Illness")









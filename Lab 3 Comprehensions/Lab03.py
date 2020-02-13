import functools
# Python II - Lab 3 - Annie Yen


"""Part 1 """


class Student(object):
    def __init__(self, id, firstName, lastName, courses=None):
        """ Student instance with id, first namde,
        last name and courses properties """
        self. id = id
        self.firstName = firstName
        self.lastName = lastName
        if courses is None:
            self.courses = dict({})
        else:
            self.courses = courses

    def gpa(self):
        """ Return gpa from the values of dictionary """
        gpa = 0
        if not bool(self.courses):
            gpa = 0
        else:
            gpa = functools.reduce(
                lambda x, y: x+y, [
                    value for value in self.courses.values()
                ])/len(self.courses)
        return gpa

    def addCourse(self, course, score):
        """ Update courses dictionary with new course
        and score key-value pair """
        assert type(score) is not int or float, "Score must be number"
        assert 0 <= score <= 4, "Score must be wihtin 0 and 4"
        self.courses[course] = score

    def addCourses(self, courses):
        """ Update courses dictionary """
        assert type(courses) or type(courses[0]) is not dict, "Courses must be dictionary"
        self.courses.update(
            (key, value)
            for key, value in courses.items()
        )

    def __str__(self):
        """ Return readable string representation of Student """
        return f"{self.id:<9} {self.lastName:<15} {self.firstName:<15} {self.gpa():<7,.3f} {''*15}"+", ".join(
            f'{key}' for key in self.courses.keys())

    def __repr__(self):
        """ Return string representation of Student meaningful to developers """
        return f"{self.id}, {self.lastName}, {self.firstName}, {self.gpa():.3f}, {self.courses}"

    def header():
        """ Return a string representation for header """
        return f"{'ID':<9} {'Last Name':<15} {'First Name':<15} {'GPA':7} {'Courses':<15}\n{'='*96}"


"""Part 2"""


def printStudents(students):
    return f"{Student.header()}\n" + '\n'.join(str(x) for x in students)


def start_my_program():
    # list vairiable for students and courses dictionary
    students = []
    students_courses = []
    # add the first 6 Students
    students.extend([
        Student(123456, "Johnnie", "Smith"),
        Student(234567, "Jamie", "Strauss"),
        Student(345678, "Jack", "O'Neill"),
        Student(456789, "Susie", "Marks"),
        Student(567890, "Frank", "Marks"),
        Student(654321, "Annie", "Marks"),
    ])
    # add the first 6 courses dictionary
    students_courses.extend([
        {'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00},
        {'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00},
        {'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00},
        {'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00},
        {'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00},
        {'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00}
    ])
    try:
        # when length of students list equal length of courses dictionary list
        if len(students) == len(students_courses):
            # Use function addCourses() on first 3 Students
            [students[d].addCourses(
                dict(students_courses[d])
                )for d in range(0, 3)
            ]
            # Use function addCourse() on the following 3 Students
            [students[d].addCourse(key, value)
            for d in range(3, 6) 
            for key, value in students_courses[d].items()
            ] 
        else: 
            print ("students list and courses dictionary list do not have equal length")
        # add the remaining 6 Students
        students.extend([
                Student(456987, "John", "Smith", {'CSE-101': 2.50, 'CSE-103': 3.00, 'CSE-210': 3.50,'CSE-260': 4.00}),
                Student(987456, "Judy", "Smith", {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00}),
                Student(111354, "Kelly", "Williams",{'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50}),
                Student(995511, "Brad", "Williams", {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00})
        ])
    except Exception as e:
        print("error " + str(e))

    """Part 3"""

    try:
        # Querry 1
        students.sort(key=lambda x: (x.lastName, x.firstName))
        print(f"{'Sort list by lastName and firstName'}\n"
              + printStudents(students)+"\n")
		
		# Querry 2
        students.sort(key = lambda x: (x.gpa()),reverse=True)
        print(f"{'Sort list by GPA'}\n"
		      + printStudents(students)+"\n")

        # Querry 3
        querry3 = {vale
                for sublist in [
                    list(students[i].courses.keys())
                    for i in range(len(students))] 
                for vale in sublist
                }
        print(f"{'The set of unique courses: '}" 
              + ", ".join(f'{i}' for i in querry3) + "\n")

        # Querry 4
        querry4 = [students[i]
            for i in range(len(students))
            if 'CSE-201' in students[i].courses
            ]
        print(f"{'List of students who have taken CSE-201'}\n"
              + printStudents(querry4)+"\n")

        # Querry 5
        querry5=[students[i]
            for i in range(len(students))
            if students[i].gpa() >= 3.5
            ]
        print(f"{'List of honor roll students'}\n"
              + printStudents(querry5))

    except Exception as e:
        print("error " + str(e))


if __name__ == "__main__":
    start_my_program()

import time
import itertools

class Course:
    def __init__(self, name, days="Mon", start="15:00", end="16:30", utils=5):
        self.name = name
        self.days = [time.strptime(day, "%a") for day in days]
        self.start = time.strptime(start, "%H:%M")
        self.end = time.strptime(end, "%H:%M")
        self.utils = utils
    def __str__(self):
        return "{} {} {}".format(self.name, time.strftime("%H:%M",self.start), time.strftime("%H:%M",self.end))
    def __repr__(self):
        return "{} {} {}".format(self.name, time.strftime("%H:%M",self.start), time.strftime("%H:%M",self.end), self.days)

def overlap(course1, course2):
    overlapping = list(set(course1.days).intersection(set(course2.days)))
    if overlapping != [] and ((course1.start <= course2.start and course2.end <= course1.end) or (course2.start <= course1.start and course1.end <= course2.end)):
        return True
    else:
        return False


courses = [Course("cs 441: quantum computing",
                 ["Tue","Thu"],
                 "15:10",
                 "16:30",
                 9),

           Course("math 342: topology",
                  ["Mon","Wed","Fri"],
                  "10:00",
                  "10:50",
                  4),

           Course("cs 382: algorithms",
                  ["Mon","Wed","Fri"],
                  "12:00",
                  "12:50",
                  10),

           Course("cs 388: crypto",
                  ["Mon","Wed","Fri"],
                  "15:10",
                  "16:00",
                  7),

            Course("math 311: complex analysis",
                  ["Mon","Wed","Fri"],
                  "14:40",
                  "15:30",
                  6),

           Course("eng 212: early modern woman",
                  ["Tue","Thu"],
                  "12:00",
                  "13:20",
                  8),

           Course("eng 242: british romantic poetry",
                  ["Mon","Wed","Fri"],
                  "13:10",
                  "14:00",
                  2),

           Course("hist 220: late imperial china",
                  ["Mon","Wed","Fri"],
                  "13:10",
                  "14:00",
                  7),

           Course("hist 384: the mexican revolution",
                  ["Mon","Wed","Fri"],
                  "12:00",
                  "12:50",
                  2),

           Course("hist 278: us 1929-79",
                  ["Tue","Thu"],
                  "15:10",
                  "16:30",
                  2),

           Course("chin 325: ci-poetry w hyong",
                  ["Tue","Thu"],
                  "10:30",
                  "11:50",
                  4)]

def no_overlaps(selection):
    for course in selection:
        for coursep in selection:
            if overlap(course,coursep) and course != coursep:
                return False
    return True

def weight(solution):
       return sum([course.utils for course in solution])

def find_solutions(courses, num_courses):
    combs = itertools.combinations(courses, num_courses)
    return [(sol, weight(sol)) for sol in sorted([comb for comb in combs if no_overlaps(comb)],key=weight)]

# for sol in find_solutions(courses, 5):
#        print("utils: {} solution: {}".format(sol[1], sol[0]))
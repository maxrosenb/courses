#original courses.py and associated algorithms by Jay Kruer

import tkinter as tk
import datetimespinner as dts
from courses import *

root = tk.Tk()
entryFrame = tk.Frame()
entryFrame.pack(side="top", fill="both", expand=True)
list1Frame = tk.Frame()
list1Frame.pack(side="top", fill="x", expand=True)
bottomFrame = tk.Frame()
bottomFrame.pack(side="bottom", fill="both", expand=True)


#Tkinter vars
onMon = tk.BooleanVar()
onTue = tk.BooleanVar()
onWed = tk.BooleanVar()
onThu = tk.BooleanVar()
onFri = tk.BooleanVar()
errorMessage = tk.StringVar()
nameText= tk.StringVar()
utils_text= tk.StringVar()


weekdaysCourseOn = []
wantedCourses = [Course("cs 441: quantum computing",
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


#functions
def getWeekdays():
	if onMon.get():
		weekdaysCourseOn.append("Mon")
	if onTue.get():
		weekdaysCourseOn.append("Tue")
	if onWed.get():
		weekdaysCourseOn.append("Wed")
	if onThu.get():
		weekdaysCourseOn.append("Thu")
	if onFri.get():
		weekdaysCourseOn.append("Fri")


def addCourseButtonClicked():
	getWeekdays()
	nameStr = nameText.get()
	startTime = e3.hour.get() + ":" + e3.min.get()
	startTimeStr = time.strptime(startTime, "%H:%M")
	endTime = e4.hour.get() + ":" + e4.min.get()
	endTimeStr = time.strptime(endTime, "%H:%M")
	print(endTime, endTimeStr, endTimeStr > startTimeStr)
	courseUtilsStr = utils_text.get()

	if (endTimeStr > startTimeStr):
		try:
			newCourse = Course(nameStr, weekdaysCourseOn, startTime, endTime, int(courseUtilsStr))
			wantedCourses.append(newCourse)
			list1.insert(tk.END, newCourse)
			errorMessage.set("")
		except ValueError:
			errorMessage.set("Oops! There was a problem with your entry.")
		
	else:
		errorMessage.set("ERROR: End time must be later than start time")
	cleanInput(nameText, nameStr, startTime, endTime, weekdaysCourseOn)
	


def calculateScoreButtonClicked():
	for sol in find_solutions(wantedCourses, 4):
		solutionString = "Points: {} Solution: {}".format(sol[1], sol[0])
		list2.insert(tk.END, solutionString)

def deleteCourseButtonClicked(deletedCourse):
	#todo
	pass

def cleanInput(name, nameS, startT, endT, weekdays):
	name.set("")
	nameS = ""
	startT = ""
	endTime = ""
	weekdays.clear()


#list boxes and scrollbars

list1 = tk.Listbox(list1Frame, height=6,width=35)
list2 = tk.Listbox(bottomFrame, height=12,width=70)

#ERROR label

l0 = tk.Label(root, textvariable=errorMessage,fg="red",font=("Helvetica", 8))
l0.pack(side= tk.LEFT)

#COURSE NAME
l1=tk.Label(entryFrame, text="Course Title")
l1.pack()


e1=tk.Entry(entryFrame, textvariable=nameText)
e1.pack()

l2=tk.Label(entryFrame, text="Days")
l2.pack()


#Checkbuttons


tk.Checkbutton(entryFrame, text = "Monday", variable = onMon, height = 2, width = 20).pack()
tk.Checkbutton(entryFrame, text = "Tuesday", variable = onTue, height = 2, width = 20).pack()
tk.Checkbutton(entryFrame, text = "Wednesday", variable = onWed, height = 2, width = 20).pack()
tk.Checkbutton(entryFrame, text = "Thursday", variable = onThu, height = 2, width = 20).pack()
tk.Checkbutton(entryFrame, text = "Friday", variable = onFri, height =2, width = 20).pack()



#Start Time and End Time



l3=tk.Label(entryFrame, text="Start Time")
l3.pack()

e3 = dts.DateTimeSpinner(entryFrame)
e3.pack()

l4=tk.Label(entryFrame, text="End Time")
l4.pack()

e4 = dts.DateTimeSpinner(entryFrame)
e4.pack()

l5=tk.Label(entryFrame, text="Score for Class out of 10")
l5.pack()


e5 = tk.Spinbox(master = entryFrame, from_=0,to=10,wrap=True,textvariable=utils_text,width=2,state="normal")
e5.pack()


l6 = tk.Label(list1Frame, text="Courses Selected:")
l6.pack()

l7 = tk.Label(bottomFrame, text="Potential Schecules:")


       
addCourseButton = tk.Button(entryFrame,text="Add Course", width=12, command=lambda :addCourseButtonClicked()).pack()
# deleteCourseButton = tk.Button(root, text="Delete Course", width=12, command= lambda:deleteCourseButtonClicked(list1.get(list1.curselection()))).pack()
calculateScoreButton = tk.Button(bottomFrame,text="Calculate Schedule", width=24, bg="blue", fg="red", command=lambda :calculateScoreButtonClicked()).pack()
l7.pack()


list1.pack()
list2.pack()
root.mainloop()



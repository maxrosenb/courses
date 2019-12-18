import tkinter as tk
import datetimespinner as dts
from courses import *



root = tk.Tk()

#Data Variables
courseName = ""
weekdaysCourseOn = []
onMon = tk.BooleanVar()
onTue = tk.BooleanVar()
onWed = tk.BooleanVar()
onThu = tk.BooleanVar()
onFri = tk.BooleanVar()
startTime = ""
endTime = ""
wantedCourses = []

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
		newCourse = Course(nameStr, weekdaysCourseOn, startTime, endTime, int(courseUtilsStr))
		wantedCourses.append(newCourse)
		list1.insert(tk.END, newCourse)
		errorMessage.set("")
	else:
		errorMessage.set("ERROR: End time must be later than start time")
	cleanInput(nameText, nameStr, startTime, endTime, weekdaysCourseOn)
	


def cleanInput(name, nameS, startT, endT, weekdays):
	name.set("")
	nameS = ""
	startT = ""
	endTime = ""
	weekdays.clear()

def calculateScoreButtonClicked():
	for sol in find_solutions(wantedCourses, 4):
		solutionString = "utils: {} solution: {}".format(sol[1], sol[0])
		list2.insert(tk.END, solutionString)

def deleteCourseButtonClicked(deletedCourse):
	#todo
	pass


#list boxes and scrollbars

list1 = tk.Listbox(root, height=6,width=35)
list2 = tk.Listbox(root, height=12,width=70)

#ERROR label
errorMessage = tk.StringVar()
l0 = tk.Label(root, textvariable=errorMessage,fg="red",font=("Helvetica", 8))
l0.pack(side= tk.LEFT)

#COURSE NAME
l1=tk.Label(root, text="Course Title")
l1.pack()

nameText=tk.StringVar()
e1=tk.Entry(root, textvariable=nameText)
e1.pack()

l2=tk.Label(root, text="Days")
l2.pack()


#Checkbuttons


tk.Checkbutton(root, text = "Monday", variable = onMon, height = 2, width = 20).pack()
tk.Checkbutton(root, text = "Tuesday", variable = onTue, height = 2, width = 20).pack()
tk.Checkbutton(root, text = "Wednesday", variable = onWed, height = 2, width = 20).pack()
tk.Checkbutton(root, text = "Thursday", variable = onThu, height = 2, width = 20).pack()
tk.Checkbutton(root, text = "Friday", variable = onFri, height =2, width = 20).pack()



#Start Time and End Time



l3=tk.Label(root, text="Start Time")
l3.pack()

e3 = dts.DateTimeSpinner(root)
e3.pack()

l4=tk.Label(root, text="End Time")
l4.pack()

e4 = dts.DateTimeSpinner(root)
e4.pack()

l5=tk.Label(root, text="Score for Class out of 10")
l5.pack()

utils_text=tk.StringVar()
e5 = tk.Spinbox(from_=0,to=10,wrap=True,textvariable=utils_text,width=2,state="readonly").pack()


       
addCourseButton = tk.Button(root,text="Add Course", width=12, command=lambda :addCourseButtonClicked()).pack()
# deleteCourseButton = tk.Button(root, text="Delete Course", width=12, command= lambda:deleteCourseButtonClicked(list1.get(list1.curselection()))).pack()
calculateScoreButton = tk.Button(root,text="Calculate Schedule", width=12, command=lambda :calculateScoreButtonClicked()).pack()



list1.pack()
list2.pack()
root.mainloop()



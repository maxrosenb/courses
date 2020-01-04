import tkinter as tk
import courses
import datetimespinner as dts

class EntryWindow:
    def __init__(self, master):
        self.master = master
        self.topFrame = tk.Frame(self.master)
        self.bottomFrame = tk.Frame(self.master)
        #CURRENT COURSE DATA
        self.courseName = tk.StringVar()
        self.onMon = tk.BooleanVar()
        self.onTue = tk.BooleanVar()
        self.onWed = tk.BooleanVar()
        self.onThu = tk.BooleanVar()
        self.onFri = tk.BooleanVar()
        #List of days courses is on
        self.courseDaysOn = []
        self.courseStartTime = ""
        self.courseEndTime   = ""
        self.courseUtils = 0
        self.currCourses = []


        self.button1 = tk.Button(self.topFrame, text = "Add Course", width = 25, command = self.addCourse)
        self.button2 = tk.Button(self.topFrame, text = "Generate Schedule", width = 25, command = self.generateSchedule)
        self.e1=tk.Entry(self.topFrame, textvariable=self.courseName)
        self.e1.pack()
        self.checkBox1 = tk.Checkbutton(self.topFrame, text = "Monday", variable = self.onMon, height = 2, width = 20)
        self.checkBox1.pack()
        self.checkBox2 = tk.Checkbutton(self.topFrame, text = "Tuesday", variable = self.onTue, height = 2, width = 20)
        self.checkBox2.pack()
        self.checkBox3 = tk.Checkbutton(self.topFrame, text = "Wednesday", variable = self.onWed, height = 2, width = 20)
        self.checkBox3.pack()
        self.checkBox4 = tk.Checkbutton(self.topFrame, text = "Thursday", variable = self.onThu, height = 2, width = 20)
        self.checkBox4.pack()
        self.checkBox5 = tk.Checkbutton(self.topFrame, text = "Friday", variable = self.onFri, height =2, width = 20)
        self.checkBox5.pack()

        self.l5=tk.Label(self.topFrame, text="Score for Class out of 10")
        self.l5.pack()
        self.e5 = tk.Spinbox(master = self.topFrame, from_=0,to=10,wrap=True,textvariable=self.courseUtils,width=2,state="normal")
        self.e5.pack()

        self.l3=tk.Label(self.topFrame, text="Start Time")
        self.e3 = dts.DateTimeSpinner(self.topFrame)
        self.l4=tk.Label(self.topFrame, text="End Time", textvariable = self.courseEndTime)
        self.e4 = dts.DateTimeSpinner(self.topFrame)
        self.l3.pack()
        self.l4.pack()
        self.e3.pack()
        self.e4.pack()
        self.button1.pack()
         
        
        
        self.button2.pack()
        self.topFrame.pack()

        self.coursesListBox = tk.Listbox(self.topFrame, height=12,width=140)
        self.coursesListBox.pack(fill=tk.BOTH, expand=1)

        #Current Course data
        
    def addCourse(self):
        self.setCourseDaysOn()

        self.courseStartTime = self.e3.hourstr.get() + ":" +self.e3.minstr.get()
        self.courseEndTime = self.e4.hourstr.get() + ":" +self.e4.minstr.get()
        self.currCourseAsCourseObject = courses.Course(self.courseName.get(), self.courseDaysOn, self.courseStartTime, self.courseEndTime)
        self.currCourses.append( self.currCourseAsCourseObject)
        self.coursesListBox.insert(tk.END, repr(self.currCourseAsCourseObject))
        self.courseDaysOn = []
        print(self.currCourses)

       


    def setCourseDaysOn(self):
        if self.onMon.get():
            self.courseDaysOn.append("Mon")
        if self.onTue.get():
            self.courseDaysOn.append("Tue")
        if self.onWed.get():
            self.courseDaysOn.append("Wed")
        if self.onThu.get():
            self.courseDaysOn.append("Thu")
        if self.onFri.get():
            self.courseDaysOn.append("Fri")

    def generateSchedule(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ScheduleWindow(self.newWindow, self)

class ScheduleWindow:
    def __init__(self, master, entryFrame):
        self.master = master
        self.entryFrame = entryFrame
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.scheduleListBox = tk.Listbox(self.frame, height=12,width=140)
        self.quitButton.pack()
        self.frame.pack()
        self.scheduleListBox.pack(fill=tk.BOTH, expand=1)
        print("list of courses", self.entryFrame.currCourses)
        sols = []
        for sol in courses.find_solutions(self.entryFrame.currCourses, 4):
            sols.append("Points for this schedule: {} solution: {}".format(sol[1], sol[0]))
        for sol in sols:
            self.scheduleListBox.insert(tk.END, sol)

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = EntryWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import time
#import for game
import random


def RequestQuickHelp():
    """Ask for student name and appear to the list
    """
    name = simpledialog.askstring("Input", "What is your name?", parent = root)
    if name == None:
        return
    try:
        LeftQueue.addName(name)
    except:
        messagebox.showinfo("Notice", name+" already in quick help queue")


def RequestLongHelp():
    """Ask for student name and appear to the list
    """
    name = simpledialog.askstring("Input", "What is your name?", parent = root)
    if name == None:
        return
    try:
        RightQueue.addName(name)
    except:
        messagebox.showinfo("Notice", name+" already in long help queue")            

class QueueStudent:
    """list the students in the queue
    """
    def __init__(self, name, questionsAsked):
        """Initialise the queue list

        Parameters:
        name - name of the students
        questionsAsked - the number of times that students have already asked quesiton
        """
        self.name = name
        self.questionsAsked = questionsAsked
        self.time = time.time()

    def get_name_string(self):
        """get the student names
        """
        return self.name

    def waitingTime(self):
        """Calculate the waiting time
        """
        return int(time.time() - self.time)

        
class Queue():
    """Create the function of queue list
    """
    def __init__(self, QuickOrLongFrame, averageTimeString):
        """Initialise the queue function to let student apppear to the list and remove
        and report waiting time

        Parameters:
        QuickOrLongFrame - either the LeftQueue or the RightQueue
        averageTimeString - text to state the average waiting time from number of students
        """
        self.questionsAsked = dict()
        self.nameExisted = set()
        self.queueStudents = []
        self.averageTimeString = averageTimeString
        self.QuickOrLongFrame = QuickOrLongFrame
        self.exist_widgets = []
        self.average_wait_time_in_seconds = 0
        self.attributeName()

    def on_red_or_green_button_clicked(self, item_index, is_green_button_clicked):
        """check if the green or red button have been clicked
        """
        name = self.queueStudents[item_index].name
        assert name in self.nameExisted
        self.nameExisted.remove(name)
        assert name in self.questionsAsked
        if is_green_button_clicked:
            self.questionsAsked[name] += 1
        del self.queueStudents[item_index]
        self.update_view()
        
    def ReportwaitingTime(self, seconds):
        """update the waiting time by seconds

        Parameters:
        seconds - Time students wait
        """
        if  seconds< 60:
            return 'a few seconds ago'
        elif seconds < 120:
            return 'a minute ago'
        elif seconds < 3600:
            return '{} minutes ago'.format(seconds // 60)
        elif seconds < 3600*2:
            return '1 hour ago'
        else:
            return '{} hours ago'.format(seconds // 3600)

    def update_average_wait_time_in_seconds(self):
        if len(self.queueStudents) == 0:
            self.average_wait_time_in_seconds = -1
        else:
            self.average_wait_time_in_seconds = 0
            for item in self.queueStudents:
                    self.average_wait_time_in_seconds += item.waitingTime()
            self.average_wait_time_in_seconds //= len(self.queueStudents)

    def sortStudents(self):
        """sort the students by the number of questionsAsked and waitingTime
        """
        self.queueStudents.sort(key=lambda x: (x.questionsAsked, -x.waitingTime()))

    def addName(self, name):
        """update the name to the queue list

        Parameters:
        name - student names
        """
        if name in self.nameExisted:
            raise Exception(name+" already in this type of queue")
        self.nameExisted.add(name)
        if name not in self.questionsAsked:
            self.questionsAsked[name] = 0
        new_item = QueueStudent(name, self.questionsAsked[name])
        self.queueStudents.append(new_item)
        self.sortStudents()
        self.update_view()

    def show_widgets_by_position(self, row, column, new_string):
        """show the informations of students and red green buttons

        Parameters:
        row - students
        column - students information
        new_string - new students
        """
        while len(self.exist_widgets) < row + 1:
            self.exist_widgets.append([])
        while len(self.exist_widgets[row]) < column + 1:
            assert column < 6
            if column < 4:
                widget = tk.Label(self.QuickOrLongFrame, text='', bg='white')
            elif column == 4:
                widget = tk.Button(self.QuickOrLongFrame, text='', bg='#F08080', fg='white', font='Arial 7', command=lambda: self.on_red_or_green_button_clicked(row - 1, False), width=1, height=1)
            elif column == 5:
                widget = tk.Button(self.QuickOrLongFrame, text='', bg='#5cb85c', fg='white', font='Arial 7', command=lambda: self.on_red_or_green_button_clicked(row - 1, True), width=1, height=1)
            widget.grid(row=row, column=len(self.exist_widgets[row]), padx=3, pady=2)
            self.exist_widgets[row].append(widget)

        assert row < len(self.exist_widgets) and column < len(self.exist_widgets[row])

        widget = self.exist_widgets[row][column]
        if column < 4:
            widget.configure(text=new_string)
        widget.grid(row=row, column=column, padx=3, pady=2)

    def update_view(self):
        """update the new students or informations to the list 
        """
        if len(self.queueStudents) == 0:
            self.averageTimeString.configure(text="No student in the queue.")
        else:
            self.averageTimeString.configure(text="An average wait time of {} for {} student.".format(self.ReportwaitingTime(self.average_wait_time_in_seconds), len(self.queueStudents)))
        self.update_average_wait_time_in_seconds()
        current_row = 0
        for item in self.queueStudents:
            current_row += 1
            line_string = [str(current_row), item.get_name_string(), item.questionsAsked, self.ReportwaitingTime(item.waitingTime())]
            for col in range(4):
                self.show_widgets_by_position(current_row, col, line_string[col])
            for col in range(4, 6):
                self.show_widgets_by_position(current_row, col, "")

        for row in range(len(self.exist_widgets)):
            if row > len(self.queueStudents):
                for widget in self.exist_widgets[row]:
                    widget.grid_forget()

    def attributeName(self):
        """set the column names
        """
        for col in range(4):
            widget = tk.Label(self.QuickOrLongFrame, text=["#", "Name", "Questions Asked", "Time"][col], bg='white', font="Arial 9 bold")
            widget.grid(row=0, column=col, padx=25)
            self.QuickOrLongFrame.columnconfigure(col, weight=1)
                


def openGame():
    """
    a small game when students want to play
    """
    game = tk.Toplevel(root)
    game.title("GUESS NUMBER")
    game.configure(bg='blue')
    game.resizable(0,0)
    canvas = tk.Canvas(game,width=300,height=200)
    canvas.pack()
    messagebox.showinfo("Prompt", "Click to start game", parent=game)
    
    lowestNUMBER = simpledialog.askstring("Input", "Set the lowest number: ", parent = game)
    #lowestNUMBER = int(input('Set the lowest number:'))
    largestNUMBER = simpledialog.askstring("Input", "Set the largest number: ", parent = game)
    #largestNUMBER = int(input('Set the largest number:'))
    number = random.randint(lowestNUMBER,largestNUMBER)
    guessNUMBER = 'guessNUMBER'
    #print("TRY TO GUESS THE CORRECT NUMBER")
    messagebox.showinfo("Notice", "TRY TO GUESS THE CORRECT NUMBER") 
    i = 0
    while guessNUMBER != number:
        i += 1
        guessNUMBER = simpledialog.askstring("Input", "What's your guess number:  ", parent = game)
        #guessNUMBER = int(input("What's your guess number: "))
        if guessNUMBER == number:
            messagebox.showinfo("Notice", "Congras@!!! You got the correct answer") 
            #print("Congras@!!! You got the correct answer")
        elif guessNUMBER < number:
            messagebox.showinfo("Notice", "Try some number larger>>>") 
            #print("Try some number larger>>>")
        else:
            messagebox.showinfo("Notice", "Try some number smaller<<<") 
            #print("Try some number smaller<<<")
            
    messagebox.showinfo("Notice", "You got %d" %i + "numbers corret!!!", end = '') 
    #print("You got %d" %i + "numbers corret!!!", end = "")

root = tk.Tk()
root.geometry('950x800')

##class Webpage(tk.Frame):
##    def __init__(self, master, *args, **kwargs):  
##        """Initialise the webpage layout
##            with a header and left and right frame
##
##        Parameters:
##            master(Tk): Main window for the application
##        """
##tk.Frame.__init__(self, *args, **kwargs)
"""Initialise the webpage layout
    with a header and left and right frame

    Parameters:
    root(Tk): Main window for the application
"""
root.title("CSSE1001 Queue")
frameHeader = tk.Frame(root, bg='#fefbed')
frameHeader.pack(side=tk.TOP, fill=tk.X)
"""creat a frame to contain the header text
"""
label1 = tk.Label(frameHeader, text="Important",font="Arial 12 bold",bg='#fefbed',fg='#C09853')
label1.pack(side=tk.TOP, anchor='w', pady=(15,0), ipadx=20)

label2 = tk.Label(frameHeader, text="Individual assessment items must be solely your own work. While students are encouraged to have high-level conversations about the problems they are\ntrying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically\ndetect similarity between assignment submissions."
                  ,font="Arial 10",bg='#fefbed', justify=tk.LEFT)
label2.pack(side=tk.LEFT,ipadx=20,pady=(0,15))


"""creat a frame to contain the left texts
"""
frame1 = tk.Frame(root, bg='white')
frame1.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
"""creat a frame to contain the right texts
"""
frame2 = tk.Frame(root, bg='white')
frame2.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

frameleft1 =tk.Label(frame1, text="Quick Questions", font="Arial 20 bold", fg="#3c763d", bg='#dff0d8')
frameleft1.pack(side=tk.TOP, fill=tk.X, ipady=20, padx=15, pady=(20,0))
frameleft2 =tk.Label(frame1, text="< 2 mins with a tutor", font="Arial 10", fg="#666", bg="#dff0d8")
frameleft2.pack(side=tk.TOP, fill=tk.X, ipady=15, padx=15, pady=(0,20))
frameleft3plus = tk.Frame(frame1, bg="white")
frameleft3plus.pack(side=tk.TOP, fill=tk.X, ipady=20, padx=15)
frameleft3 = tk.Label(frameleft3plus, text="Some examples of quick questions:\n    • Syntax errors\n    • Interpreting error output\n    • Assignment/MyPyTutor interpretation\n    • MyPyTutor submisson issues",
                      font="Arial 10", bg="white", justify=tk.LEFT)
frameleft3.pack(side=tk.TOP, anchor='w')
##        canvas_width = 445
##        canvas_height = 5
##        canvasLeft1 = Canvas(frame1, width=canvas_width,height=canvas_height)
##        canvasLeft1.pack(side=tk.TOP)
quickButton = tk.Button(frame1, text="Request Quick Help", bg="#5cb85c", fg="white",command=RequestQuickHelp)
quickButton.pack(side=tk.TOP, anchor='center',ipady=5,ipadx=5)
GreyLineL1= tk.Canvas(frame1, width=445, height=-2)
GreyLineL1.pack(side=tk.TOP,pady=(15,0))

frameright1 =tk.Label(frame2, text="Long Questions", font="Arial 20 bold", fg="#31708f", bg='#d9edf7')
frameright1.pack(side=tk.TOP, fill=tk.X, ipady=20, padx=15, pady=(20,0))
frameright2 =tk.Label(frame2, text="> 2 mins with a tutor", font="Arial 10", fg="#666", bg="#d9edf7")
frameright2.pack(side=tk.TOP, fill=tk.X, ipady=15, padx=15, pady=(0,20))
frameright3plus = tk.Frame(frame2, bg="white")
frameright3plus.pack(side=tk.TOP, fill=tk.X, ipady=20, padx=15)
frameright3 = tk.Label(frameright3plus, text="Some examples of long questions:\n    • Open ended questions\n    • How to start a problem\n    • How to improve code\n    • Debugging\n    • Assignmnent help",
                       font="Arial 10", bg="white", justify='left')
frameright3.pack(side=tk.TOP, anchor='w')
longButton = tk.Button(frame2, text="Request Long Help", bg="#5bc0de", fg="white",command=RequestLongHelp)
longButton.pack(side=tk.TOP, anchor='center',ipady=5,ipadx=5)
GreyLineR1= tk.Canvas(frame2, width=445, height=-2)
GreyLineR1.pack(side=tk.TOP,pady=(15,0))


queueLabelLeft = tk.Label(frame1, text = 'An average wait time of a few seconds for 1 student.', font="Arial 10", bg='white')
queueLabelLeft.pack(side=tk.TOP, padx=20, anchor= 'w', pady=20)
GreyLineL2= tk.Canvas(frame1, width=445, height=-2)
GreyLineL2.pack(side=tk.TOP,pady=(0,10))
queueLabelRight = tk.Label(frame2, text = 'An average wait time of about 5 minutes for 2 students.', font="Arial 10", bg='white')
queueLabelRight.pack(side=tk.TOP, padx=20, anchor= 'w', pady=20)
GreyLineR2= tk.Canvas(frame2, width=445, height=-2)
GreyLineR2.pack(side=tk.TOP,pady=(0,10))
"""creat a frame to contain the left queue list
"""
frameLeftQueue = tk.Frame(frame1, bg='white')
frameLeftQueue.pack(side=tk.TOP)
"""creat a frame to contain the right queue list
"""
frameRightQueue = tk.Frame(frame2, bg='white')
frameRightQueue.pack(side=tk.TOP)

LeftQueue = Queue(frameLeftQueue, queueLabelLeft)
RightQueue = Queue(frameRightQueue, queueLabelRight)

GameButton=tk.Button(frame1, text="PLAY BOARD", bg='black', fg='green', font="Arial 14", command=openGame)
GameButton.pack(side=tk.BOTTOM, anchor='center',ipady=5,ipadx=5)

##        queueLabelLeft2 = tk.Label(frameLeftQueue, text = ["1", "Barry B.Benson", "0", "a few seconds ago"], font="Arial 10", bg='white')
##        queueLabelLeft2.pack(side=tk.TOP, padx=20, anchor= 'w', pady=20)
##        queueLabelRight2 = tk.Label(frameRightQueue, text = ["1", "Vanessa Bloome", "0", "a few seconds ago"], font="Arial 10", bg='white')
##        queueLabelRight2.pack(side=tk.TOP, padx=20, anchor= 'w', pady=20)


LeftQueue.addName("Barry B.Benson")
RightQueue.addName("Vanessa Bloome")
RightQueue.addName("Adam Flayman")



def on_timer():
    LeftQueue.update_view()
    RightQueue.update_view()
    root.after(10000, on_timer)



root.mainloop()
on_timer()

##lowestNUMBER = int(input('Set the lowest number:'))
##highestNUMBER = int(input('Set the highest number:'))
##number = random.randint(lowestNUMBER,highestNUMBER)
##guessNUMBER = 'guessNUMBER'
##print("TRY TO GUESS THE CORRECT NUMBER")
##i = 0
##while guessNUMBER != number:
##    i += 1
##    guessNUMBER = int(input("What's your guess number: "))
##    if guessNUMBER == number:
##        print("Congras@!!! You got the correct answer")
##    elif guessNUMBER < number:
##        print("Try some number larger>>>")
##    else:
##        print("Try some number smaller<<<")
##
##print("You got %d" %i + "numbers corret!!!", end = "")

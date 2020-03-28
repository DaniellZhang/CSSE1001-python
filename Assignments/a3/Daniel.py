import tkinter as tk


class Webpage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        """Initialise the webpage layout
            with a header and left and right frame

        Parameters:
            master(Tk): Main window for the application
        """
        tk.Frame.__init__(self, *args, **kwargs)
        master.title("CSSE1001 Queue")
        frameHeader = tk.Frame(master, bg='light yellow')
        frameHeader.pack(side=tk.TOP, fill=tk.X)
        label1 = tk.Label(frameHeader, text="Important",font="Arial 12 bold",bg='light yellow',fg="dark orange")
        label1.pack(side=tk.TOP, anchor='w', pady=(10,0), ipadx=10)
        label2 = tk.Label(frameHeader, text="Individual assessment items must be solely your own work. While students are encouraged to have high-level conversations about the problems they are\ntrying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically\ndetect similarity between assignment submissions."
                          ,font="Arial 10",bg='light yellow', justify=tk.LEFT)
        label2.pack(side=tk.LEFT,ipadx=10,pady=(0,10))

        frame1 = tk.Frame(master, bg='white')
        frame1.pack(side=tk.LEFT,fill=tk.BOTH, expand=True, ipady=20)
        frame2 = tk.Frame(master, bg='white')
        frame2.pack(side=tk.LEFT,fill=tk.BOTH, expand=True, ipady=20)
        
        frameleft1 =tk.Label(frame1, text="Quick Questions", font="Arial 15 bold", fg="dark green", bg='light green')
        frameleft1.pack(side=tk.TOP, fill=tk.X, ipady=10, padx=5)
        frameleft2 =tk.Label(frame1, text="< 2 mins with a tutor", font="Arial 10", fg="grey", bg="light green")
        frameleft2.pack(side=tk.TOP, fill=tk.X, ipady=5, padx=5)
        frameleft3plus = tk.Frame(frame1, bg="white")
        frameleft3plus.pack(side=tk.TOP, fill=tk.X, ipady=20, padx=5)
        frameleft3 = tk.Label(frameleft3plus, text="Some examples of quick questions:\n    • Syntax errors\n    • Interpreting error output\n    • Assignment/MyPyTutor interpretation\n    • MyPyTutor submisson issues",
                              font="Arial 10", bg="white", justify=tk.LEFT)
        frameleft3.pack(side=tk.TOP, anchor='w')
        self.quickButton = tk.Button(frame1, text="Request Quick Help", bg="light green", fg="white",command=self.RequestQuickHelp)
        self.quickButton.pack(side=tk.TOP, anchor='center')
        
        
        frameright1 =tk.Label(frame2, text="Long Questions", font="Arial 15 bold", fg="dark blue", bg='light blue')
        frameright1.pack(side=tk.TOP, fill=tk.X, ipady=10, padx=5)
        frameright2 =tk.Label(frame2, text="> 2 mins with a tutor", font="Arial 10", fg="grey", bg="light blue")
        frameright2.pack(side=tk.TOP, fill=tk.X, ipady=5, padx=5)
        frameright3plus = tk.Frame(frame2, bg="white")
        frameright3plus.pack(side=tk.TOP, fill=tk.X, ipady=20, padx=5)
        frameright3 = tk.Label(frameright3plus, text="Some examples of long questions:\n    • Open ended questions\n    • How to start a problem\n    • How to improve code\n    • Debugging\n    • Assignmnent help",
                               font="Arial 10", bg="white", justify='left')
        frameright3.pack(side=tk.TOP, anchor='w')
        self.longButton = tk.Button(frame2, text="Request Long Help", bg="light blue", fg="white",command=self.RequestLongHelp)
        self.longButton.pack(side=tk.TOP, anchor='center')
        
        
    def RequestQuickHelp(self):
        print('yeah')

    def RequestLongHelp(self):
        print('haSS')





root = tk.Tk()

root.geometry('600x400')

a = Webpage(root)

#frame_name = tk.Frame(root).pack(expand=True)


root.mainloop()

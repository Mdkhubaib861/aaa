from tkinter import *
home_screen = Tk()
home_screen.resizable(False,False)
home_screen.title("MMANTC Academics Data")
Label(home_screen,text="MMANTC Academics Data",font=("Open Sans",25,"bold")).grid(row=0,column=0,columnspan=2)

b1=Button(home_screen,text="Admin",font=("Open Sans",20,"bold")).grid(row=1,column=0,padx=10,pady=10)
home_screen.mainloop()

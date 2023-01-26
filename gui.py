from tkinter import *
from ss import Take
root = Tk()
root.title("App")
root.geometry("644x434")
root.minsize(100, 100)
# gui logic

# Frame logic
class FirstFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

class SecondFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


# variables
uservalue = StringVar()
passvalue = StringVar()


# condition for running script
condition=False

# main_function for taking actions
def infinite_loop():
	print(condition)
	print("Running infinite_loop")
	if condition:
		a = Take()
		a.main()
		root.after(5000, infinite_loop)
	else:
		root.after(5000, infinite_loop)

# start button logic
def start():
	print("starting")
	global condition
	if uservalue.get() == "smit" and passvalue.get() == "pass":
		condition=True

# stop button login
def stop():
	print("stopping")
	global condition
	condition=False

# welcome label
Label(root, text="Welcome", font='comicsansms 13 bold', pady=15).grid(row=0, column=0)

# form type entries
user = Label(root, text="Employee Id")
password = Label(root, text="Password")
user.grid(row=1)
password.grid(row=2)

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=1, column=1)
passentry.grid(row=2, column=1)


# Buttons 
b1 = Button(text="Start", command=start).grid()
b2 = Button(text="Stop", command=stop).grid()
b3 = Button(text = "quit", command = quit).grid()


infinite_loop()
root.mainloop()

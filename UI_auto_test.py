import pandas    as pd
import pyautogui as pauto
import time
from tkinter import *

root     = Tk()
root.title("Test 2 - Basic Classes")
numSteps = 0
steps    = []
columns  = []


class Step:

	def __init__(self, master, lab, loc, col):
		self.imageFieldLabel = Label(master, text="Image File Path: ")
		self.imageField      = Entry(master, textvariable = "")
		self.imageFieldLabel.destroy()
		self.imageField.destroy()
		self.durFieldLabel   = Label(master, text="Duration: ")
		self.durField        = Entry(master, textvariable = "")
		self.durFieldLabel.destroy()
		self.durField.destroy()
		self.typeFieldLabel  = Label(master, text="Duration: ")
		self.typeField       = Entry(master, textvariable = "")
		self.typeFieldLabel.destroy()
		self.typeField.destroy()
		self.fillFieldLabel = Label(root, text="Fill Options: ")
		self.fillFieldLabel.destroy()
		self.fillChoices    = OptionMenu(root, "", ["fake"], command = self.fillClicker)
		self.fillChoices.destroy()
		self.label     = lab
		self.id        = loc
		self.cols      = col
		self.options   = ["","Find","Click","Type","Fill"]
		self.clicked   = StringVar()
		self.clicked.set(self.options[0])
		self.choices   = OptionMenu(master, self.clicked, *self.options, command = self.clicker)
		self.choices.grid(row=loc,column=0)

	def clicker(self, event):
		if self.clicked.get() == "Find": self.setFind()
		elif self.clicked.get() == "Click": self.setClick()
		elif self.clicked.get() == "Type": self.setType()
		elif self.clicked.get() == "Fill": self.setFill()

	def setFind(self):
		if self.imageFieldLabel.winfo_exists():
			self.imageFieldLabel.destroy()
			self.imageField.destroy()
			self.windFieldLabel.destroy()
			self.windField.destroy()
		if self.durFieldLabel.winfo_exists():
			self.durFieldLabel.destroy()
			self.durField.destroy()
		if self.typeFieldLabel.winfo_exists():
			self.typeFieldLabel.destroy()
			self.typeField.destroy()
		if self.fillFieldLabel.winfo_exists():
			self.fillFieldLabel.destroy()
			self.fillChoices.destroy()
		self.imageVar        = StringVar()
		self.imageFieldLabel = Label(root, text="Image File Path: ")
		self.imageField      = Entry(root, textvariable = self.imageVar)
		self.imageFieldLabel.grid(row=self.id,column=1)
		self.imageField.grid(row=self.id,column=2)
		self.windVar         = StringVar()
		self.windFieldLabel  = Label(root, text="Search window: ")
		self.windField       = Entry(root, textvariable = self.windVar)
		self.windFieldLabel.grid(row=self.id,column=3)
		self.windField.grid(row=self.id,column=4)

	def setClick(self):
		if self.imageFieldLabel.winfo_exists():
			self.imageFieldLabel.destroy()
			self.imageField.destroy()
			self.windFieldLabel.destroy()
			self.windField.destroy()
		if self.durFieldLabel.winfo_exists():
			self.durFieldLabel.destroy()
			self.durField.destroy()
		if self.typeFieldLabel.winfo_exists():
			self.typeFieldLabel.destroy()
			self.typeField.destroy()
		if self.fillFieldLabel.winfo_exists():
			self.fillFieldLabel.destroy()
			self.fillChoices.destroy()
		self.durVar          = StringVar()
		self.durFieldLabel   = Label(root, text="Duration: ")
		self.durField        = Entry(root, textvariable = self.durVar)
		self.durFieldLabel.grid(row=self.id,column=1)
		self.durField.grid(row=self.id,column=2)

	def setType(self):
		if self.imageFieldLabel.winfo_exists():
			self.imageFieldLabel.destroy()
			self.imageField.destroy()
			self.windFieldLabel.destroy()
			self.windField.destroy()
		if self.durFieldLabel.winfo_exists():
			self.durFieldLabel.destroy()
			self.durField.destroy()
		if self.typeFieldLabel.winfo_exists():
			self.typeFieldLabel.destroy()
			self.typeField.destroy()
		if self.fillFieldLabel.winfo_exists():
			self.fillFieldLabel.destroy()
			self.fillChoices.destroy()
		self.typeVar         = StringVar()
		self.typeFieldLabel  = Label(root, text="Text: ")
		self.typeField       = Entry(root, textvariable = self.typeVar)
		self.typeFieldLabel.grid(row=self.id,column=1)
		self.typeField.grid(row=self.id,column=2)

	def fillClicker(self, event):
		print(str(self.fillClicked.get()))

	def setFill(self):
		if self.imageFieldLabel.winfo_exists():
			self.imageFieldLabel.destroy()
			self.imageField.destroy()
			self.windFieldLabel.destroy()
			self.windField.destroy()
		if self.durFieldLabel.winfo_exists():
			self.durFieldLabel.destroy()
			self.durField.destroy()
		if self.typeFieldLabel.winfo_exists():
			self.typeFieldLabel.destroy()
			self.typeField.destroy()
		if self.fillFieldLabel.winfo_exists():
			self.fillFieldLabel.destroy()
			self.fillChoices.destroy()
		self.fillFieldLabel = Label(root, text="Fill Options: ")
		self.fillOptions    = self.cols #["Filler","Filler1","Filler2","Filler3"]
		#print(self.fillOptions)
		self.fillClicked    = StringVar()
		self.fillClicked.set(self.fillOptions[0])
		self.fillChoices    = OptionMenu(root, self.fillClicked, *self.fillOptions, command = self.fillClicker)
		self.fillFieldLabel.grid(row=self.id,column=1)
		self.fillChoices.grid(row=self.id,column=2)

def submit():
	global columns
	global df
	df = pd.read_excel(xlVar.get())
	columns = df.columns.values.tolist()
	
xlVar   = StringVar()
xlLabel = Label(root, text="Excel file path: ")
xlField = Entry(root, textvariable = xlVar)
sub_btn = Button(root,text = 'Submit', command = submit)

xlLabel.grid(row=0,column=0)
xlField.grid(row=0,column=1)
sub_btn.grid(row=0,column=2)


def addStep():
	global numSteps
	global steps
	numSteps = numSteps + 1
	label    = "Step "+str(numSteps)
	addStep  = Step(root,label,numSteps+1, columns)
	steps.append(addStep)
	#print(steps)
	#for step in steps:
		#print(step.clicked.get())

newStep = Button(root, text="Add Step", command = addStep)
newStep.grid(row=1,column=0)

def find_image(im):
	x = None
	y = None
	while x == None and y == None:
		try:
			x,y = pauto.locateCenterOnScreen(im)
			return x,y
		except: time.sleep(1)

def process():
	for i in range(len(df.axes[0])):
		for step in steps:
			if step.clicked.get() == "Find":
				#print(step.imageVar.get())
				img_x, img_y = find_image(step.imageVar.get())
				pauto.moveTo(img_x, img_y)
			if step.clicked.get() == "Click": pauto.click() #step.durVar.get()
			if step.clicked.get() == "Type":
				if step.typeVar.get() == "tab": pauto.press('tab')
				else : pauto.typewrite(step.typeVar.get()) 
			if step.clicked.get() == "Fill": pauto.typewrite(df.loc[i, step.fillClicked.get()])

process = Button(root, text="Process Steps", command = process)
process.grid(row=0,column=3)

root.mainloop()








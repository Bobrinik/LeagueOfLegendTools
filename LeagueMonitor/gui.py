from Tkinter import *
import collect

root = Tk()
frame = Frame(root)
frame.pack()

searchframe = Frame(root)

searchframe.pack( side = TOP )

L1 = Label(searchframe, text="User Name:")
L1.pack( side = LEFT)
E1 = Entry(searchframe, bd =5)
E1.pack(side = LEFT)


def populate(name):

	headers=["PlayerName","WinRate","FrequentPosition","FrequentRole","History"]
	records=collect.Collector(name).loadInfo()

	counter=0
	for r in range(12):
		record_info = records[counter]
		for c in range(5):					
				
			if r == 6:
				Label(tableframe, text="Red",borderwidth=2 ).grid(row=r,column=c)
				break
			elif r == 1:
				Label(tableframe, text="Blue",borderwidth=2 ).grid(row=r,column=c)
				break
			elif r == 0:
				Label(tableframe, text=headers[c],borderwidth=2 ).grid(row=r,column=c)
			else:
				Label(tableframe, text=record_info[c],borderwidth=1 ).grid(row=r,column=c)

		if(r not in [0,1,6]):		
			counter = counter+1

def readEntry():	
	populate(E1.get())



redbutton = Button(searchframe, text="SEARCH", fg="red",command=readEntry)
redbutton.pack( side = RIGHT)




tableframe = Frame(root)
tableframe.pack( side = BOTTOM)

root.mainloop(  )

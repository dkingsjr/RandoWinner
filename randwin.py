from tkinter import *
from random import randint

root = Tk()
root.title("RandoWinner")
#root.iconbitmap("insert filepath")
root.geometry('350x350')

def pick():
	entries = ['person1', 'person2', 'person3', 'person4', 'person5']
	#convert to a set
	entries_set = set(entries)
	#convert to a list
	unique_entries = list(entries_set)
	#create a list sized variable
	our_number = len(unique_entries) - 1
	#create random number
	rando = randint(0, our_number)
	#create winner output
	winnerlabel = Label(root, text=unique_entries[rando], font="helvetica 20 bold")
	winnerlabel.grid(row=5, columnspan=3, pady=5)
  

label1 = Label(root, text="Scholarship Winner", font="helvetica 20 bold")
label1.grid(row=0, column=0, columnspan=3, pady=5)

entry = Entry(root, width=20, text='Enter Applicant')
entry.grid(row=1, column=0, columnspan=2, pady=20)

winbutton = Button(root, width=13, text="Choose Winner", font=("helvetica, 12"), command=pick)
winbutton.grid(row=2, column=1, pady=5, padx=5)

enterbutton = Button(root, width=13, text="Enter Person", font=("helvetica, 12"))
enterbutton.grid(row=2, column=0, pady=5, padx=5)

resetbutton = Button(root, width=13, text="Reset", font="helvetica 12 bold", bg="red", fg="white")
resetbutton.grid(row=3, column=0, columnspan=3, pady=5, padx=5)

label2 = Label(root, text="CONGRATULATIONS!!", font="helvetica 20 bold", fg="orange")
label2.grid(row=4, column=0, columnspan=3, pady=15)

root.mainloop()

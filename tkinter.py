from tkinter import *

top = Tk()
playlist = []

def addSong():
    playlist.append(E1.get())

L1 = Label(top, text="Playlist Generator")
L1.grid(column = 0, row= 1)


E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)


B1 = Button(text="Add to playlist", bg = "light blue", command = addSong)
B1.grid(column = 1, row = 2)

B2 = Button(text = "Export List", bg = "white", command = printList)


top.mainloop()

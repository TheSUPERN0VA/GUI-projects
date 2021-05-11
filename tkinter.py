from tkinter import *

top = Tk()
playlist = []

def addSong():
    playlist.append(E1.get())
    E1.delete(0, END)

def printList():
    print(playlist)

def exportPlaylist():    
    with open('playlist.txt', 'w') as f:
        for song in playlist:
            f.write("%s/n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "Week 1", bg= "white", command = week1)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "white")
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "white")
    B3.Main.grid(column = 0, row = 4)

def week1():
    clearWindow()

    L1 = Label(top, text="Playlist Generator")
    L1.grid(column = 0, row= 1)


    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)


    B1 = Button(text=" + ", bg = "#B4F9FF", command = addSong)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = "Export List", bg = "white", command = printList)
    B2.grid(column=1, row =1)

    B3 = Button(text="Export List", bg = "8a7e42", command = exportPlayList)
    B3.grid(column = 1, row = 3)

    Bclear = Button(text="Main Menu", bg = "white", command= mainMenu)
    Bclear.grid(column = 1, row = 4)

def week2():
    clearWindow()

    L1W2 = Label()
    L2W2 = Label()
    L3W2 = Label()

    E1W2 = Entry()
    E2W2 = Entry()

    B1W2 = Button()


    

if __name__ == "__main__":
    mainMenu()
    top.mainloop()

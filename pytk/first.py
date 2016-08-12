import Tkinter

class Application(Tkinter.Frame):
    def createWidgets(self):
        self.QUIT = Tkinter.Button(self)
        self.QUIT['text'] = 'QUIT'
        self.QUIT['fg'] = 'red'
        self.QUIT['command'] = self.quit
        self.QUIT.pack({ 'side': 'left' })

    def __init__(self, master = None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tkinter.Tk()
app = Application(master = root)
app.mainloop()
root.destroy()

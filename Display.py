import tkinter
import time

class Display(object):

    def __init__(self, house, heater):
        self._house = house
        self._heater = heater

    def create(self,master):

        master.title("Home Comforts-Control")
        tkinter.Label(master, text = self._house).pack()
        tkinter.Label(master, text = self._heater).pack()

        for r in self._house.getRooms():
            tkinter.Label(master,text = r).pack()
    
    def run(self):
        root = tkinter.Tk()
        self.create(root)
        root.after(1000,self.create(root))
        root.mainloop()
    
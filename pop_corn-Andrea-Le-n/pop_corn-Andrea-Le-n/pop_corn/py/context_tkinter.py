import tkinter as tk

#from canvas_tkinter import Canvas_Tkinter
from pop_corn.py.canvas_tkinter import Canvas_Tkinter
from pop_corn.py.buttons_tkinter import Buttons_Tkinter

class Context_Tkinter:
    def __init__(self):
        self.master=tk.Tk()
        self.mainloop=self.master.mainloop
        self.after_ms=self.master.after
    
    def canvas(self,scene,**props):
        return Canvas_Tkinter(scene,tk_master=self.master,**props)


    def buttons(self,num_bits,**props):
        return Buttons_Tkinter(num_bits,tk_master=self.master,**props)



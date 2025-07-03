#
from pop_corn.cpy.canvas_html import Canvas_HTML
from pop_corn.cpy.camera_ov7670 import Camera_ov7670
#from pop_corn.py.canvas_tkinter import Canvas_Tkinter

import time,supervisor

class Context_CircuitPython:
    def __init__(self):
        #self.master=tk.Tk()
        #self.mainloop=self.master.mainloop
        #self.after_ms=self.master.after
        self.events=[]
        self.perif={}
    
    def canvas(self,scene,**props):
        #raise ('falta por implementar')
        return Canvas_HTML(scene,self,**props)
    
    def camera_gray(self,**props):
        return Camera_ov7670()
        
    def mainloop(self):
        while True:
            for event in self.events.copy():
                delta=supervisor.ticks_ms()-event['event_ms']
                if delta > 0 or delta < -2**28:
                    self.events.remove(event)
                    event['callback']()
                
            time.sleep(0.001)
            
    def after_ms(self,ms,callback):
        self.events.append({
            'event_ms':supervisor.ticks_ms()+ms,
            'callback':callback
        })
        
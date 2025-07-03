from tkinter import Tk, Checkbutton, IntVar, Button, Label, Frame
#import tkinter as tk
#from ..matrix import Matrix

class Buttons_Tkinter:
    def __init__(self,num_bits,**props):
        self.num_bits=num_bits
        root=props['tk_master']
        # Create a Frame to hold the Checkbuttons and their labels
        frame = Frame(root)
        frame.pack()

        # Create a list to hold IntVars for each bit
        self.bits = [IntVar() for _ in range(num_bits)]
        self.checkbuttons = []

        # Create Checkbuttons and labels for each bit
        for i in range(num_bits):
            # Label for the bit (above the Checkbutton)
            Label(frame, text=f"index{i}").grid(row=0, column=i, padx=5)
            Label(frame, text=f"In_bit{num_bits - i - 1}").grid(row=1, column=i, padx=5)
            
            # Checkbutton for the bit
            chk=Checkbutton(frame, variable=self.bits[i])
            chk.grid(row=2, column=i, padx=5)
            self.checkbuttons.append(chk)
            print(chk)
        print(self.checkbuttons)

    def value(self):
        # Get the binary representation
        binary = "".join(str(bit.get()) for bit in self.bits[::-1])
        #print(f"Binary Input: {binary},{int(binary,2)}")
        return int(binary,2)
    
    def value_bin(self):
        # Get the binary representation
        binary = "".join(str(bit.get()) for bit in self.bits)
        #print(f"Binary Input: {binary},{int(binary,2)}")
        return binary
    
    def light(self, colors):
        for i, color in enumerate(colors):
            if i < len(self.checkbuttons):
                self.checkbuttons[i].config(bg=color)
        
    def light_bin(self, colors,on='gray35',off='gray65'):
        for i, color in enumerate(colors):
            if i < len(self.checkbuttons):
                self.checkbuttons[i].config(bg=on if color else off )
        
        
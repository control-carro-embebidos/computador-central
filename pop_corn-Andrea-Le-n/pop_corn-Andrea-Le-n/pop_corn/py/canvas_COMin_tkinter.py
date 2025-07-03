import tkinter as tk
#from ..Matrix import Matrix
from Canvas_Tkinter import Canvas_Tkinter


if __name__ == "__main__":

    import serial

    import ast
    
    canvas=None
    master=tk.Tk()
    
    def parse_function_string(s ):
        global canvas
        print('s','¿'+s+'?')
        func_name=s[:4]
        if func_name=='__in':
            params_list = (s[s.find('(')+1:s.find(')')]).split(',')
            
            params = {}
    
            # Extract and evaluate each parameter value
            for param in params_list:
                key, value = param.split('=')
                key = key.strip()
                value = value.strip()
                params[key] = ast.literal_eval(value)
            
            params['tk_master']=master
            # Call the print_constructor_call method with the extracted arguments
            print('-ini-',params)
            canvas=Canvas_Tkinter(**params)
            print('canvas',canvas)
            return 0
        elif canvas==None:
            return -1
        elif func_name=='dele':
            print('delete')
            return canvas.delete()
            
        elif func_name in ['oval','rect','line']:
            
            # Extract the list and dictionary part of the string
            list_part = s[s.find('['):s.find(']')+1]
            dict_part = s[s.find('{'):s.find('}')+1]
            
            # Convert the string representations to Python objects
            coordinates = ast.literal_eval(list_part)
            params = ast.literal_eval(dict_part)
            
            # Call the appropriate function with the extracted arguments
            if func_name == 'oval':
                print('oval')
                return canvas.oval(Matrix(2,2,coordinates), **params)
            elif func_name == 'rect':
                return canvas.rectangle(coordinates, **params)
            elif func_name == 'line':
                return canvas.line(coordinates, **params)
        else:
            print(f"Unknown function name: ¿{s}?")



    port = input("port: (like COM11)")
    if port=="":
        port="COM11"

    ser = serial.Serial(
        port=port,
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
    )
    ser.write(b'\r\n')  
    ser.write(b'\r\n')
    buffer=[]
    #while True:
    def repetir_com():
        global buffer
        master.after(50,repetir_com)
        n=ser.in_waiting
        rx_uart = ser.read(n).decode()
        if rx_uart:
            print('rx',rx_uart,len(buffer))
            buffer += rx_uart.splitlines(True)
        if len(buffer):       
            tx_uart = parse_function_string(buffer.pop(0))
            print('tx',tx_uart)
            #tx_uart += '\r\n'
            #ser.write(tx_uart.encode('ascii'))  
            
    repetir_com() 
    master.mainloop()    



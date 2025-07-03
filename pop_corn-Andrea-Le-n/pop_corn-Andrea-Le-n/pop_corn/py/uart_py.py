import serial

Class Uart_py: 
    def __init__(self, 
                port='COM11',
                baudrate=115200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE):##,**kwargs):
     
        self.uart= serial.Serial(
                port=port,
                baudrate=baudrate,
                bytesize=bytesize,
                parity=parity,
                stopbits=stopbits,
                                )
                                
        self.prop={
                'port'=port,
                'baudrate'=baudrate,
                'bytesize'=bytesize,
                'parity'=parity,
                'stopbits'=stopbits,        
        }#+  kwargs
    
    
        def readinto(self, buf_r):
            return self.uart.readino(buf_r)
        
        def write(self, buf_w):
            return self.uart.write(buf_w)
            
            
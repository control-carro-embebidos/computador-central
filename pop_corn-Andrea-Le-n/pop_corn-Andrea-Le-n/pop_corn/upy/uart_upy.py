from machine import UART,Pin

Class Uart_upy: 
    def __init__(self, 
                port=None,
                baudrate=115200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                buf_r=None,
                buf_w=None
                ):##,**kwargs):
        if buf_w==None:
            buf_w=bytearray(8)
        if buf_r==None:
            buf_r=bytearray(8)
        
       #try:
        #from machine import UART,Pin
        if port==None:
            port=(Pin(5),Pin(4),1)# rx,tx,id
        uart = UART(port[2],#id
                    baudrate=9600,
                    bits=8,
                    parity=None,
                    stop=1,
                    rx=port[0],
                    tx=port[1])
       # except:
        # import board
        # import busio
        # import digitalio
        # if port == Noone:
            # port=(board.GP4, board.GP5)
        # uart = busio.UART(*port,
                          # baudrate=9600,
                          # bits=8,
                          # parity=None,
                          # stop=1)
                                
        self.prop={
                'port':port,
                'baudrate':baudrate,
                'bytesize':bytesize,
                'parity':parity,
                'stopbits':stopbits,      
                'buf_r':buf_r,
                'buf_w':buf_w
                }#+  kwargs
    
        def readinto(self, buf_r):
            return self.uart.readino(buf_r)
            
        
        def write(self, buf_w):
            return self.uart.write(buf_w)
    
            

import digitalio
import busio
import board
from adafruit_ov7670 import (  # pylint: disable=unused-import
    OV7670,
    OV7670_SIZE_DIV16,
    OV7670_COLOR_YUV,
    OV7670_TEST_PATTERN_COLOR_BAR_FADE,
)


class Camera_ov7670:
    def __init__(self,**props):    
        # # Supported color formats
        # OV7670_COLOR_RGB = 0
        # """RGB565 big-endian"""
        # OV7670_COLOR_YUV = 1
        # """YUV/YCbCr 422 big-endian"""
        # 
        # # Supported sizes (VGA division factor) for OV7670_set_size()
        # OV7670_SIZE_DIV1 = 0
        # """640 x 480"""
        # OV7670_SIZE_DIV2 = 1
        # """320 x 240"""
        # OV7670_SIZE_DIV4 = 2
        # """160 x 120"""
        # OV7670_SIZE_DIV8 = 3
        # """80 x 60"""
        # OV7670_SIZE_DIV16 = 4
        # """40 x 30"""

        # Ensure the camera is shut down, so that it releases the SDA/SCL lines,
        # then create the configuration I2C bus

        #with digitalio.DigitalInOut(board.D39) as shutdown:
        #    shutdown.switch_to_output(True)
        #    time.sleep(0.001)
        props={
            'scl':board.GP21,
            'sda':board.GP20,
            'data_pins':[
                board.GP0,
                board.GP1,
                board.GP2,
                board.GP3,
                board.GP4,
                board.GP5,
                board.GP6,
                board.GP7,
            ],
            'clock':board.GP8,
            'vsync':board.GP13,
            'href':board.GP12,
            'mclk':board.GP9,
            'shutdown':board.GP15,
            'reset':board.GP14,
            'cam_size' : OV7670_SIZE_DIV16,
            'cam_colorspace': OV7670_COLOR_YUV,
            'cam_flip_y' : True,
            }|props
        cam_bus = busio.I2C(props['scl'],props['sda'])

        self.cam = OV7670(
            cam_bus,
            data_pins=props['data_pins'],
            clock=props['clock'],
            vsync=props['vsync'],
            href=props['href'],
            mclk=props['mclk'],
            shutdown=props['shutdown'],
            reset=props['reset'],
        )
        self.cam.size = props['cam_size']
        self.cam.colorspace = props['cam_colorspace']
        self.cam.flip_y = props['cam_flip_y']

    #    print(cam.width, cam.height)

        self.buf_in = bytearray(2* self.cam.width * self.cam.height)
        #self.buf_out = bytearray( self.cam.width * self.cam.height)
    #    print('##################################')
    #    print(buf)

        
    def capture_gray(self,buf=None):
        if buf==None:
            buf=self.buf_in
        self.cam.capture(buf)
#         print('##################################')
#         print(len(buf))
#         print('##################################')
#         print(len(list(buf)))


#         chars = b" .:-=+*#%@"

        width = self.cam.width
        row = bytearray(width)
        #while True:

            #cam.capture(buf)
#         for j in range(self.cam.height):
#             for i in range(width):
#                 self.buf_out[width * j + i]=row[i ] = buf[2*(width * j + i)]
#             print(row)
        self.buf_out=bytearray([data for i,data in enumerate(buf) if i%2==0])
        return self.buf_out
#                print(row)
#            print()
#            time.sleep(2)

# Example usage
if __name__ == "__main__":
    camera=Camera_gray_ov7670()
    print(camera.capture())
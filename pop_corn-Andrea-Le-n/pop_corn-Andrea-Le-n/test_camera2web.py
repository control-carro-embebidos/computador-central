# This program sets up a web server that streams the camera feed to an HTML page.
# You need to configure the network name (SSID) and password.
# Ensure the client device is connected to the same network.
# Access the camera feed via the IP address displayed after 'IP address: PicoW'.

import array


from pop_corn.matrix import Matrix, Vec
from pop_corn.scene import Scene
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.cpy.context_circuitpython import Context_CircuitPython
    




if __name__ == "__main__":
    
    t_anim = 1000


    ctx=Context_CircuitPython()
    scene = MainScene()

    canvas = ctx.canvas(scene)
    canvas.oval(Matrix(2,2,[10, 10, 5, 3]), value=255)
    print(canvas.matrix)
    
    camera= ctx.camera_gray()

    def anim_loop():
        ctx.after_ms(t_anim,anim_loop)
        print('.',end='')
        canvas.matrix.data=array.array('f',list(camera.capture_gray()))

  
    anim_loop() 
    ctx.mainloop()
    
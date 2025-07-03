from pop_corn.matrix import Matrix, Vec
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.py.context_tkinter import Context_Tkinter as Context


if __name__ == "__main__":
    
    t_anim = 1000

    ctx=Context()
    scene = MainScene()#bg='img/UD_@8.xbm', foreground="white", background="black")

    disc0 = Disc(scene)
    disc0.set_pos(-50,0)
    print('0',disc0)

    
    disc1 = Disc(scene)
    #disc1.set_pos(-50,0)
    print('1',disc1)

    disc2 = Disc(scene)
    disc2.set_pos(50,0)
    print('2',disc2)

    state=disc0
    state.color='blue'
    next_state=state
    next_out={}
    
    in_bits=ctx.buttons(4)
    canvas = ctx.canvas(scene)
    out_bits=ctx.buttons(5)
    
    

    def anim_loop():
        global state,next_state,next_out
        ctx.after_ms(t_anim,anim_loop)
        scene.refresh()
        binary=in_bits.value_bin()
        canvas.debug(f"Bin:{binary}, Int:{int(binary,2)}")
        #binary = f"{n:0{32}b}"
        print('1',binary,state,type(binary[0]))
        if state==disc0:
            print('disc0',binary[0])
            if binary[0] == '1':
                next_state=disc1
                next_out[0]='0'
                
        elif state==disc1:
            print('disc1')
            if binary[0] == '1':
                next_state=disc2
                next_out[0]='0'
                
        elif state==disc2:
            print('disc2')
            if binary[0] == '1':
                next_state=disc0
                next_out[0]='1'
                


        state.color="green"
        state=next_state
        state.color="blue"
        
        
        #bin_out = out_bits.value_bin(None)#f"{out_bits.value(None):0{self.num_bits}b}"
        #print('bin_out',bin_out,type(bin_out))
        out_bits.light_bin(next_out)
        #for key, valu in next_out.items():
        #    bin_out[key]=valu
        
        #out_bits.value_bin(bin_out)
        print('2',binary,state,next_out)

        next_out={}
  
    anim_loop() 
    ctx.mainloop()
    



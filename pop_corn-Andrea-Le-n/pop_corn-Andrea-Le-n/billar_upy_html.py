from pop_corn.matrix import Matrix, Vec
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.upy_html.context_upy_html import Context_upy_html as Context


if __name__ == "__main__":
    
    t_anim = 500

    ctx=Context()
    scene = MainScene()#bg='img/UD_@8.xbm', foreground="white", background="black")
    disc0 = Disc(scene)
    
    disc1 = Disc(scene)
    disc1.r=10
    disc1.color='blue'
    disc1.set_pos(-50,0)
    disc1.set_vel(Vec(5,0.5))

    canvas = ctx.canvas(scene)

    def anim_loop():
        ctx.after_ms(t_anim,anim_loop)
        scene.refresh()
  
    anim_loop() 
    ctx.mainloop()
    

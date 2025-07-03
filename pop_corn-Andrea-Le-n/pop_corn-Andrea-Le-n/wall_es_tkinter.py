from pop_corn.matrix import Matrix, Vec
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.pub_sub import PubSub
from pop_corn.py.context_tkinter import Context_Tkinter as Context
from wall_e.wall_e import Wall_e
from wall_e.garbage import Garbage
import numpy as np
import math

class Host(PubSub):
    def __init__(self,zones_num,debug=False):
        super().__init__()
        self.zones_num=zones_num
        #self.pubsub = PubSub()
        pass
            #Amarillo: (70,-250)->()
        #Rojo: (200,-70) -> (200,30)
        #Azul: (-200,-100) 
        #Verde: (-70,-270)
        #Black1: (180,-200) -> (-20,-130)
        #Black2: (-190,-210)

#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,200,30,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-20,-130,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-110,-50,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-140,-20,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-120,60,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,0,110,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-50,110,0]]})
        
    
    
    def Bezier_x(self, coor_ix, coor_fx,n):
        ptos_x = []
        pc_x = 0
        if coor_ix == 200:
           pc_x = 180
        elif coor_ix == -70:
           pc_x = -190

        dist_x = []
        
        t = np.arange(0, 1.1, 0.1)
        
        for t_aux in t:
           Pto_x = coor_ix*(1-t_aux)**(n)+n*(pc_x)*(1-t_aux)*t_aux + coor_fx*(t_aux)**n
           ptos_x.append(Pto_x)
        
    
        for i in range(len(ptos_x) - 1):
            valor_actual = ptos_x[i]
            suma = ptos_x[i+1] - ptos_x[i]
            dist_x.append(suma)
        return dist_x
        #coorf_x = coor_fx - coor_ix
        #Pto_x = coor_ix1*(1-t) + coor_ix2*t**2
    def Bezier_y(self, coor_iy, coor_fy,n):
        ptos_y = []
        dist_y = []
        pc_y = 0
        if coor_iy == -70:
           pc_y = -200
        elif coor_iy == -270:
           pc_y = -210
    
    
        t = np.arange(0, 1.1, 0.1)
        

        for t_aux in t:
           Pto_y = coor_iy*(1-t_aux)**(n)+n*(pc_y)*(1-t_aux)*t_aux + coor_fy*(t_aux)**n
           ptos_y.append(Pto_y)
        
        for i in range(len(ptos_y) - 1):
            valor_actual = ptos_y[i]
            suma = ptos_y[i+1] - ptos_y[i]
            dist_y.append(suma)
        return dist_y       

    
    
    def angles(self,coor_x,coor_y):
        
        angle = 180
        
        if coor_x > 0 and coor_y > 0:
           angle = np.arctan2(coor_x, coor_y)
           
        elif coor_x > 0 and coor_y < 0:
             angle = 2*(np.pi) - np.arctan2(coor_x, coor_y) 
        
        elif coor_x < 0 and coor_y > 0:
             angle = np.pi - np.arctan2(coor_x, coor_y)
        
        elif coor_x < 0 and coor_y < 0:
             angle = -np.pi/3
             #angle = np.pi + np.arctan2(coor_x, coor_y)
# 
# 
        return angle
     
#     def start(self):
#         for i in range(self.zones_num[0]):
#             for j in range(self.zones_num[1]):
#                 name=f"Walle_{i}_{j}/wheelVels"
#                 #self.publish(name, {"steering_angle_deg":20*i+5*j,"speed_cm_s":2, "duration_seg":30})
#         #self.publish("All_Wall_es", {"steering_angle_deg":0,"speed_cm_s":20, "duration_seg":2})      
# #         self.publish("All_Wall_es/on_move", #{"value": "10"})
# #         {#"arm_ds_deg**3":[[3,10,10,10],[5,12,10,10],[10,14,10,10],[15,20,10,10]],
# #                        "rel_posit_ds_frontmm_rightmm_angledeg":[[3,10,10,0],[3,12,10,0],[3,14,10,45],[3,20,10,45]],
# #          #              "catch_ds_byte":[[0,0],[10,255],[15,0]]
# #             })
# #         self.publish("Walle_0_0/on_move", #{"value": "10"})
# #         {"rel_posit_ds_frontmm_rightmm_angledeg":[[2,0,11,15],[2,12,10,30],[2,14,10,45],[2,20,10,60]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[9,self.Move_walls_x(200),self.Move_walls_y(-70),-90]]})
# 
    def start(self):

        for i in range(self.zones_num[0]):
            for j in range(self.zones_num[1]):
                name=f"Walle_{i}_{j}/wheelVels"
                
        coor = self.Bezier_x(0, 200,1)
        coor_y = self.Bezier_y(-100,-70,1)

        for i in range(len(coor)):
            self.publish("Walle_0_0/on_move", #{"value": "10"})
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,coor[i],coor_y[i]
                                                         ,self.angles(coor[i],
                                                                      coor_y[i])]]})

        
        self.publish("Walle_0_0/on_move",
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,0,0,0]]})

        coor1 = self.Bezier_x(200, 70,2)
        coor_1y = self.Bezier_y(-70,-250,2)
        
        for i in range(len(coor1)):
            self.publish("Walle_0_0/on_move", #{"value": "10"})
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,coor1[i],coor_1y[i]
                                                         ,self.angles(coor1[i],
                                                                      coor_1y[i])]]})
            
        
        self.publish("Walle_0_0/on_move",
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,0,0,0]]})
        
        coor2 = self.Bezier_x(70, -70,1)
        coor_2y = self.Bezier_y(-250,-270,1)        
        
        for i in range(len(coor2)):
            self.publish("Walle_0_0/on_move", #{"value": "10"})
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,coor2[i],coor_2y[i]
                                                         ,self.angles(coor2[i],
                                                                      coor_2y[i])]]})
          
        
        self.publish("Walle_0_0/on_move",
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,0,0,0]]})
        
        coor3 = self.Bezier_x(-70, -200,2)
        coor_3y = self.Bezier_y(-270,-100,2)
        
        for i in range(len(coor3)):
            self.publish("Walle_0_0/on_move", #{"value": "10"})
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,coor3[i],coor_3y[i]
                                                         ,self.angles(coor3[i],
                                                                      coor_3y[i])]]})
            
            
        
        self.publish("Walle_0_0/on_move",
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,0,0,0]]})
        self.publish("Walle_0_0/on_move",
              {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-70,0,0]]})


#        self.publish("Walle_0_0/on_move", #{"value": "10"})
        #{"rel_posit_ds_frontmm_rightmm_angledeg":[[9,-200,70,-90]]})
       # self.publish("Walle_0_0/on_move", #{"value": "10"})
        #{"rel_posit_ds_frontmm_rightmm_angledeg":[[9,200-30,30,0],
        #[9,40,67,34]]})
        #{"rel_posit_ds_frontmm_rightmm_angledeg":[[9,200-30,70,0],]})
#                      
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,self.Bezier_x(0,200-10,t_aux),
#                                                    self.Bezier_y(0,-70,t_aux),self.angles(self.Bezier_x(0,200-30,t_aux),self.Bezier_y(0,-70,t_aux))]
#                                                    for t_aux in t
#         ]})
#         
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#            {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,self.Bezier_x(200-10,70,t_aux),
#                                                       self.Bezier_y(-70,-250,t_aux),self.angles(self.Bezier_2x(0,200-30,t_aux),self.Bezier_2y(0,-70,t_aux))]
#                                                       for t_aux in t
#         ]})
# #          
#      

#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,200,30,0]]})
        #self.publish("Walle_0_0/on_move", #{"value": "10"})
        #{"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-20,-130,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-130,-180,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-140,-20,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-120,60,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,0,110,0]]})
#         self.publish("Walle_0_0/on_move", #{"value": "10"})
#         {"rel_posit_ds_frontmm_rightmm_angledeg":[[5,-50,110,0]]})
        
        
    

    def animate(self):
        pass
    
    def get_name(self):
        return "Host"

if __name__ == "__main__":
    
    t_anim = 100 #ms
    zones_num=(1,2)
    zones_size=(400,200)
    debug=False#True
    
    host = Host(zones_num,debug)
    ctx=Context()
    scene = MainScene()#bg='img/UD_@8.xbm', foreground="white", background="black")
    disc0 = Disc(scene)
    Garbage(scene,"red",200,-70)
    Garbage(scene,"blue",-200,-100)
    #Garbage(scene,"black", 180,-200)
    #Garbage(scene,"black", -190,-210)
    Garbage(scene, "yellow", 70,-250)
    Garbage(scene, "light green",-70,-270)
    
    wall_es=[]
    for i in range(zones_num[0]):
        list_tmp=[]
        for j in range(zones_num[1]):
            disc_tmp=Wall_e(scene,i,j,host,debug)
            name=disc_tmp.get_name()
            #disc_tmp.name=f"Walle_{i}_{j}"
            #disc1.color='blue'
            
            disc_tmp.set_pos(int((i-zones_num[0]/2 +0.5)*zones_size[0]),int((j-zones_num[1]/2+0.5)*zones_size[1]))
            #disc1.set_vel(Vec(5,0.5))
            #host.subscribe(disc_tmp.name+" All_Wall_es", disc_tmp, "Command")
            list_tmp.append(list_tmp)
            #host.publish(disc_tmp.name, {"steering_angle_deg":20*i+5*j,"speed_cm_s":15, "duration_seg":5})
            
            
    
        wall_es.append(list_tmp)
    
    #host.publish("All_Wall_es", {"steering_angle_deg":0,"speed_cm_s":20, "duration_seg":2})
        
    canvas = ctx.canvas(scene,height=zones_num[1]*zones_size[1],width=zones_num[0]*zones_size[0])

    def anim_loop():
        #global debug
        if debug:
            rta=input("Debug Mode, Press ENTER")
        #    if "off"==rta:
        #        debug=False
        ctx.after_ms(t_anim,anim_loop)
        scene.refresh()
        host.animate()
  
    host.start()
    anim_loop() 
    ctx.mainloop()
    

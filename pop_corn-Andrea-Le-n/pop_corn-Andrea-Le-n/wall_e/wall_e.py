import math
import time
from pop_corn.matrix import Matrix, Vec
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.uqueue import uQueue
from pop_corn.py.context_tkinter import Context_Tkinter as Context
from pop_corn.lib import copy



class Wall_e(Disc):
    def __init__(self,scene,i,j,host,debug=False):
        self.debug=debug
        self.host=host
        self.i,self.j=i,j
        super().__init__(scene)
        self.steering_angle_degrees=1
        self.wheelbase=200
        self._t_circle=0
        self.set_speed(5)
        self.poligons=[
            {"points":Matrix(4,2,[3,5, 3,15, 18,15, 18,5]),"options":{}},
            {"points":Matrix(4,2,[-3,5, -3,15, -18,15, -18,5]),"options":{}},
            {"points":Matrix(4,2,[-3,-5, -3,-15, -18,-15, -18,-5]),"options":{}},
            {"points":Matrix(4,2,[3,-5, 3,-15, 18,-15, 18,-5]),"options":{}},
            {"points":Matrix(8,2,[7,-2, 20,-2, 20,-5, 30,-5, 30,5, 20,5, 20,2, 7,2]),"options":{"fill":"yellow"}},
                      ]
        host.subscribe(self.get_name()+"/wheelVels All_Wall_es/wheelVels", self, "wheelVels")
        host.subscribe(self.get_name()+"/on_move All_Wall_es/on_move", self, "on_move")


        self.queues = {}  # callback_name -> Queue()
        #self.ps=pubsub
        self.k_max_mag = 10
        self.k_mag =self.k_max_mag
        self.k_ferromag = 0
        self.move_wall_e_conf={"arm_m":[1,1,1],"arm_b":[0,0,0],"wheels_lr_m":[1,1],"wheels_lr_b":[0,0]}
        self.move_car_data={}
        #self.move_arm_time_stamp=None
        self._pos=Vec(0,0)
        self.anim_data={}
        self.ticks=0

        # Subscribe to each topic using provided PubSub

#     def ensure_queue(self, callback_name):
#         if callback_name not in self.queues:
#             self.queues[callback_name] = uQueue(callback_name)

    def published(self, data):
        data=copy.deepcopy(data)
        #print("Who published",self.get_name(),data)
        callback_name = data.get("callback_name")
        control= data.get("control","appendlast")
        if callback_name is None:
            return
        #self.ensure_queue(callback_name)
        if callback_name not in self.queues:
            self.queues[callback_name] = uQueue(callback_name)
        if control=="appendlast":
            self.queues[callback_name].appendlast(data)
        if control=="appendfirst":
            self.queues[callback_name].appendfirst(data)
        if control=="clear_appendfirst":
            self.queues[callback_name].clear()
            self.queues[callback_name].appendfirst(data)
        self.print("Who published",self.get_name(), self.queues[callback_name]._queue)

    def process(self, callback_name,t):
        queue = self.queues.get(callback_name)
        if queue:
            #while len(queue):
                msg = queue.popfirst()
                #self.print("process",f"{self.get_name()}:{callback_name} received ->", msg)
                if callback_name=="on_move":
                    self.move_wall_e_ini(msg['data'])
        else:
            pass
            self.print("process",f"{self.get_name()}:{callback_name} No_received")


    def move_wall_e_ini(self,movements):
        #wall_e movemen is a dic of list of list, first item is time in ds relative to the lastime of the same key
        #movements={"arm_ds_deg**3":[[3,10,10,10],[5,12,10,10],[10,14,10,10],[15,20,10,10]],
        #           "rel_posit_ds_front_right_mm":[[3,10,10],[5,12,10],[10,14,10],[15,20,10]],
        #           "catch_ds_byte":[[0,0],[10,255],[15,0]]}
        
        for key in movements:
            if key in self.move_car_data:
                self.move_car_data[key]+=copy.deepcopy(movements[key])
            else:
                self.move_car_data[key]=copy.deepcopy(movements[key])
            #print("move_wall_e_ini",key,self.move_car_data[key])
            self.anim_data[key+"_time_stamp_ds"]=self.ticks#time.time_ns()//10**8
        self.print("move_wall_e_ini self.anim_data",self.anim_data,self.move_car_data)
        
        
        
    def move_wall_e_anim(self,t):
        self.ticks+=t
        #key="rel_posit_ds_distance_angledeg"
        key="rel_posit_ds_frontmm_rightmm_angledeg"
        if key in self.move_car_data:
            if len(self.move_car_data[key])>0:
                ds=self.move_car_data[key][0][0]
                #delta_ticks=time.time_ns()//10**8
                self.print("move_wall_e_anim self.anim_data",self.anim_data,self.move_car_data,self.ticks)
                if (self.anim_data[key+"_time_stamp_ds"]+ds)<= self.ticks:
                    ds,front,right,angl=self.move_car_data[key].pop(0)
                    self.anim_data[key+"_time_stamp_ds"]=self.ticks
                    self.add_pos(Vec(front,right))
                    self.add_angle(angl*math.pi/180)
            else:
                pass
                self.print("wall_e move_wall_e_anim: Hay que frenar")
                



#    def send(self,dest,data):
#        pass
    
    def recive(self,dest,data):
        pass
        
    

    def get_name(self):
        return f"Walle_{self.i}_{self.j}"

#     def published(self, data=None):
#         print("Who published",self.get_name(),data)
#         if data["callback_name"]=="Command":
#             if "steering_angle_deg" in data["data"]:
#                 self.steering_angle_degrees=data["data"]["steering_angle_deg"]
#                 #print("steering_angle_degrees",data["data"]["steering_angle_deg"],self.steering_angle_degrees)
#             if "speed_cm_s" in data["data"]:
#                 self.set_speed(data["data"]["speed_cm_s"])
#                 #print("speed_cm_s",data["data"]["speed_cm_s"],self.get_speed())
#             if "duration_seg" in data["data"]:
#                 self._t_circle=data["data"]["duration_seg"]
#                 #print("duration_seg",data["data"]["duration_seg"],self._t_circle)        
        
    @staticmethod
    def default_control(self,t):
        self.process("on_move",t)
        self.move_wall_e_anim(t)
        
    def print(self,*args):
        if self.debug:
            print(*args,self.get_name(),self.ticks)
        
        
#         #print("wall_w t",self.i,self.j,self.steering_angle_degrees)
#         
#         if self._t_circle>0:
#         
#             v=self.get_speed()
#             # Actualización del ángulo del carro
#             self.add_angle((v / self.wheelbase) * math.tan(self.steering_angle_degrees*math.pi/180)*t)
# 
#             # Desplazamiento en el sistema global
#             theta = self._angle  # orientación actual del carro
#             dx = v * math.cos(theta) * t
#             dy = v * math.sin(theta) * t
# 
#             desp = Matrix(1,2,[dx, dy])
#             self.add_pos(desp)
#             self._t_circle-=t
#             #print("wall_w t",t)


# if __name__ == "__main__":
#     

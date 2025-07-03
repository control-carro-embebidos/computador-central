# cambios a realizar.
#     data es bytearray
#     Se anexa una string de 4 caracters con el formato
#     se debe hacer un buffer o lista o diccionarion para almacenar published
#     debe permitir adicionar al principio o al final o borrar la lista
from pop_corn.uqueue import uQueue
from pop_corn.matrix import Matrix, Vec
#from uqueue import uQueue
#from matrix import Matrix, Vec
import time


class PubSub:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topics, who, callback_name):
        self.log("subscribe:"+str(topics)+" "+str( who)+" "+str( callback_name))
        for  topic in topics.split():
            if topic not in self.topics:
                self.topics[topic] = []
            self.topics[topic].append({"who":who,"callback_name":callback_name})

#     def unsubscribe(self, topic, who, callback_name):
#         if topic in self.topics:
#             try:
#                 self.topics[topic].remove(callback)
#                 if not self.topics[topic]:
#                     del self.topics[topic]
#             except ValueError:
#                 pass  # Callback not found

    def publish(self, topics, data=None):
        self.log("publish:"+str(topics)+" "+str( data))
        for  topic in topics.split():
            if topic in self.topics:
                for info in self.topics[topic]:
                    info["who"].published(info|{"data":data,"topic":topic, "who":self.get_name()})
            
    def log(self, string):
        print(string)
        
    def get_name(self):
        return "PubSub"



        
# class Who:
#     def __init__(self,name):
#         self.name=name
#         
#     def published(self, data=None):
#         print("Who published",self.name,data)


class Who:
    def __init__(self, name, pubsub, subscriptions):
        self.name = name
        self.queues = {}  # callback_name -> Queue()
        #self.ps=pubsub
        self.move_wall_e_conf={"arm_m":[1,1,1],"arm_b":[0,0,0],"wheels_lr_m":[1,1],"wheels_lr_b":[0,0]}
        self.move_car_data={}
        #self.move_arm_time_stamp=None
        self._pos=Vec(0,0)
        self.anim_data={}

        # Subscribe to each topic using provided PubSub
        for topic, callback_name in subscriptions:
            self.ensure_queue(callback_name)
            pubsub.subscribe(topic, self, callback_name)

    def ensure_queue(self, callback_name):
        if callback_name not in self.queues:
            self.queues[callback_name] = uQueue(callback_name)

    def published(self, data):
        callback_name = data.get("callback_name")
        control= data.get("control","appendlast")
        if callback_name is None:
            return
        self.ensure_queue(callback_name)
        if control=="appendlast":
            self.queues[callback_name].appendlast(data)
        if control=="appendfirst":
            self.queues[callback_name].appendfirst(data)
        if control=="clear_appendfirst":
            self.queues[callback_name].clear()
            self.queues[callback_name].appendfirst(data)

    def process(self, callback_name):
        queue = self.queues.get(callback_name)
        if queue:
            #while len(queue):
                msg = queue.popfirst()
                print(f"{self.name}:{callback_name} received ->", msg)
                if callback_name=="on_move":
                    self.move_wall_e_ini(msg['data'])
        else:
            print(f"{self.name}:{callback_name} No_received")


    def move_wall_e_ini(self,movements):
        #wall_e movemen is a dic of list of list, first item is time in ds relative to the lastime of the same key
        #movements={"arm_ds_deg**3":[[3,10,10,10],[5,12,10,10],[10,14,10,10],[15,20,10,10]],
        #           "rel_posit_ds_front_right_mm":[[3,10,10],[5,12,10],[10,14,10],[15,20,10]],
        #           "catch_ds_byte":[[0,0],[10,255],[15,0]]}
        
        for key in movements:
            if key in self.move_car_data:
                self.move_car_data[key]+=movements[key]
            else:
                self.move_car_data[key]=movements[key]
            print("move_wall_e_ini",key,self.move_car_data[key])
        self.anim_data[key+"_time_stamp_ds"]=time.time_ns()//100000000
        
        
        
    def move_wall_e_anim(self):
        key="rel_posit_ds_front_right_mm"        
 
            
        if key in self.move_car_data:
            ds,font,right=self.move_car_data["rel_posit_ds_front_right_mm"].pop(0)
            ticks=time.time_ns()//100000000
            if (self.anim_data[key+"_time_stamp_ds"]+ds)>= ticks:
                self.anim_data[key+"_time_stamp_ds"]=ticks
                self.add_pos(Vec(front,right))
                 


    def add_pos(self,pos):
        self._pos  = self._pos +pos
                
            
            
        



if __name__ == "__main__":




    ps = PubSub()

    Host = Who(
        name="Host",
        pubsub=ps,
        subscriptions=[
            ("all_dev/frame", "on_frame"),
            ("all_dev/alert", "on_alert")
        ]
    )
    deviceA = Who(
        name="DeviceA",
        pubsub=ps,
        subscriptions=[
            ("all_dev/arm devA/arm", "on_arm"),
            ("all_dev/move devA/move", "on_move")
        ]
    )
    deviceB = Who(
        name="DeviceB",
        pubsub=ps,
        subscriptions=[
            ("all_dev/arm devB/arm", "on_arm"),
            ("all_dev/move devB/move", "on_move")
        ]
    )

    Host.ps.publish("devA/arm", {"value": 23})
    Host.ps.publish("all_dev/move", #{"value": "10"})
    {"arm_ds_deg**3":[[3,10,10,10],[5,12,10,10],[10,14,10,10],[15,20,10,10]],
                   "rel_posit_ds_front_right_mm":[[3,10,10],[5,12,10],[10,14,10],[15,20,10]],
                   "catch_ds_byte":[[0,0],[10,255],[15,0]]})
    Host.ps.publish("devB/move", #{"value": "10"})
    {"arm_ds_deg**3":[[3,10,10,10],[5,12,10,10],[10,14,10,10],[15,20,10,10]],
                   "rel_posit_ds_front_right_mm":[[3,10,10],[5,12,10],[10,14,10],[15,20,10]],
                   "catch_ds_byte":[[0,0],[10,255],[15,0]]})

    deviceA.process("on_arm")
    deviceB.process("on_arm")
    deviceA.process("on_move")
    deviceB.process("on_move")
    deviceA.process("on_arm")
    deviceB.process("on_arm")
    deviceA.process("on_move")
    deviceB.process("on_move")
    deviceA.process("on_arm")
    deviceB.process("on_arm")
    deviceA.process("on_move")
    deviceB.process("on_move")

# 
# 
#     # Create PubSub instance
#     pubsub = PubSub()
# 
# 
# 
# 
# ###############################################
#     who1=Who(1)
# #     In who1 ->
# #     def temperature_handler(data):
# #         print("Temperature update:", data)
#     pubsub.subscribe("temperature cool", who1, "temperature_handler")
# ###############################################
#     who2=Who(2)
# #     In who2 ->
# #     def humidity_handler(data):
# #         print("Humidity update:", data)
#     pubsub.subscribe("humidity rain",who2 , "humidity_handler")
# ###############################################
#     
#     # Publish some data
#     pubsub.publish("temperature cool", 25.6)
#     pubsub.publish("rain", 65)
#     pubsub.publish("humidity", 60)

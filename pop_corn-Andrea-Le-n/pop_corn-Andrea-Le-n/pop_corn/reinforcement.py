from pop_corn.perceptron import Perceptron
from pop_corn.matrix import Matrix, Vec
# from Matrix import Matrix
# from Perceptron import Perceptron
# import array
# import random

class Reinforcement:
    def __init__(self,n_in, n_out, list_outs,f_error):
        """
        n_in, n_out : number of inputs and outputs
        list_outs : a Matrix of spected outputs. each row is one output
        f_error : input:Matrix,output:Matrix -> realnumber that represents the error of that input

        """
        self.n_in = n_in
        self.n_out = n_out
        self.list_outs = list_outs
        self.f_error = f_error
        self.control = Perceptron( n_in, n_out)
        self.model = Perceptron(n_in + n_out, n_in)
        self.input_ant =None
        self.output_ant =None



    def control_predict(self, input_):
        return self.control.predict(input_)

    def model_predict(self, input_, output):
        return self.model.predict(input_ & output  )

    def control_train(self, input_act , output_act, learning_rate=0.1):
        self.control.train(input_act, output_act, learning_rate=learning_rate)

    def model_train(self, input_act, output_act, learning_rate=0.1):
        if self.input_ant != None and self.output_ant != None:
            self.model.train(self.input_ant & self.output_ant , input_act, learning_rate=learning_rate)
        self.input_ant = input_act
        self.output_ant = output_act

    def improve_control(self, input_ant=None, learning_rate=0.01):
        if input_ant == None:
            input_ant = self.input_ant
        out_selected=None
        min_error=None
        for i in range(self.list_outs.m):
          out_i=self.list_outs[i:i+1,:]
          in_predic = self.model.predict(input_ant & out_i)
          error_pred = self.f_error(in_predic,out_i.tolist())
          if  (None == min_error) or (error_pred < min_error):
              min_error = error_pred
              out_selected= out_i
        self.control.train(input_ant,out_selected, learning_rate=learning_rate)        

    def train_both(self, input_act , output_act, learning_rate=0.1 ):
        self.control_train(input_act, output_act, learning_rate=learning_rate)
        self.model_train(input_act, output_act, learning_rate=learning_rate)
 
    def predict_improve_train(self, input_act, learning_rate=0.01 ):
        output_act = self.control_predict(input_act)
        self.model_train(input_act , output_act, learning_rate=learning_rate)
        self.improve_control( learning_rate=learning_rate)
        return output_act 
# #    def control_predict_improve(self,in) 
# 
# 
# 
# 
#     output =self.control.predict(input_)
#     
#     self.train(self.input_old,self.output_old,input_,output)
# 
#     self.input_old=input_
#     self.output_old=output
#     return pred
#      
#   
#   def train(self , input_old ,  output_old , input_ , output):
#       model.train(input_old | output_old,input_)
#           
# # Example usage
# if __name__ == "__main__":
#     from Car import Car
#     from Speedway import Speedway
#     import tkinter as tk
# 
# 
#     master = tk.Tk()
#     
#     perceptron = Perceptron(name_or_input_size=7, output_size=2)    
#     
#     train=True
#     #repeat=True
#     
#     speedway = Speedway(master)
#     car = Car()
#     speedway.add_car(car)
# 
# 
#     def enter(event):
#         global train
#         train=not(train)
#         print('train: ',train)
#         perceptron.save_file("car.txt")
#         
#     def load(event):
#         global perceptron
#         perceptron = Perceptron("car.txt") 
#         print('load: ',load)
#        
# 
#     master.bind("<Return>", enter)
#     master.bind("<space>", load)
# 
#     def train_control():
#         global cont_train,train
#       #if repeat:
#        
#         floor_colors = Matrix(1,7,speedway.read_floor_color_gray(car.get_sensors_coord()))
#         if train:
#             master.after(30,train_control)
#             maxval=0
#             index_maxval=11
#             for i in range(7):
#                 if floor_colors[0,i]>maxval:
#                     maxval=floor_colors[0,i]
#                     index_maxval=i-4
#             car.v_i=5 - index_maxval/3
#             car.v_d=5 + index_maxval/3
#             motors_vel= Matrix(1,2,[car.v_i,car.v_d])
# 
#             cont_train +=1
#             if cont_train%100==0:
#                 print(cont_train,perceptron.predict(floor_colors*(1/255))*5-motors_vel)
#             if cont_train==10000:
#                 train=False
# 
#             perceptron.train(floor_colors*(1/255), motors_vel*(1/5))
#         else:
#             master.after(10,train_control)
#             prediction=perceptron.predict(floor_colors*(1/255))*5
#             car.v_i = prediction[0,0]
#             car.v_d = prediction[0,1]
#             #print('predic', prediction)
#                 
#     cont_train =0
#     speedway.anim()
#     train_control()
#     master.mainloop()
# 
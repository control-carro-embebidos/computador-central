#import tkinter as tk
from ..matrix import Matrix

class Canvas_upy_html:
    
    
# llamar en el constructoer    
#server.add_gadget(gadget_dic):
#     gadgets=gadgets|gadget_dic
#
#llamar para poner shapes
# server. add_shape(shape):
#     json2send=sjon2send|shape

    
    def __init__(self,scene,**props):#transf=None,height=900,width=1800,tk_master=None,grid=10 ):
        #self.canvas_width = cols
        #self.canvas_height = rows
        
        self.scene=scene
        self.context=props['context']
        scene.subscribe_canvas(self)
        props={'height':300,'width':300} | props
        self.props=props
        m,n=props['height'],props['width']
        
        

        if 'transf' not in props:
            px_cm=100/150#min(m,n)/50
            transf=Matrix(3,3,
                               [px_cm,0,0,
                                0,px_cm,0,
                                n/2,m/2,1],has_tail=True)
            props['transf']=transf
        self.transf=props['transf']

        self.canvas_index=self.context.add_gadget({
        "type": "canvas",
        "canvasWidth": n,
        "canvasHeight": m
      })


#         self.canvas = tk.Canvas(props['tk_master'],height=m,width=n,bg='blue')#, **subset)
#         self.canvas.pack()
# 
#         xy=Matrix(m*n,2,
#                   [k
#                   for i in range(m)
#                   for j in range(n)
#                   for k in (i,j)])
# #                   [(lambda k:i if k==0 else j if k==1 else 0)(k)
# #                               for i in range(m)
# #                               for j in range(n)
# #                               for k in range(3)])
#         xy=xy@(self.transf.inv())
#         xbm_image=self.xmb_format(Matrix(m,n,self.scene.get_background_at(xy)))
#         bitmap = tk.BitmapImage(data=xbm_image, foreground="white", background="black")
#         #bitmap = tk.BitmapImage(data=xbm_image, background="white", foreground="black")
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=bitmap)
#         self.canvas.image = bitmap
#         self.debug_id=self.canvas.create_text(n/2,10,text='0')
#         
    
    def oval(self, vertex,**options)->int:
        #print(vertex@self.transf)
        points=vertex@self.transf
        oval_dic={
                "gadget_index":self.canvas_index,
                "canvas_fillStyle": "blue",
                "canvas_shape": "ellipse",
                "canvas_elli_x": int(points[0]),
                "canvas_elli_y": int(points[1]),
                "canvas_elli_rw": int((points[2]-points[0])/2),
                "canvas_elli_rh": int((points[3]-points[1])/2),
                "canvas_elli_angini_deg": 0,
                "canvas_elli_angfin_deg": 360,
            }
        self.context.add_shape(oval_dic)
#         self.canvas_index=self.context.add_gadget({
#         "type": "canvas",
#         "canvasWidth": n,
#         "canvasHeight": m
#       })
        #return self.canvas.create_oval(vertex@self.transf,**options)
        
    def delete(self,tag):
        oval_dic={
                "gadget_index":self.canvas_index,
                #"canvas_fillStyle": "blue",
                "canvas_shape": "reset",
            }
        self.context.add_shape(oval_dic)

        #pass#self.canvas.delete(tag)
#     def rect(self, vertex,**options)->int:
#         return self.canvas.create_rectangle(vertex@self.transf,**options)
#         
# 
#     def text(self, vertex,**options)->int:
#         return self.canvas.create_text(vertex[0:1,:]@self.transf,**options)
# 
#     def debug(self, text)->int:
#         return self.canvas.itemconfig(self.debug_id,text=text)
# 
#     def	line(self, vertex,**options)->int:
#         return self.canvas.create_line(vertex@self.transf,**options)
#     
#     def	poly(self, vertex,**options)->int:
#         return self.canvas.create_polygon(vertex@self.transf,**options)
#     
#     #def coords(self, id_shape, list_vertex):
#     #    self.canvas.coords(id_shape, list_vertex@self.transf)
#             
# 
#     def draw_grid(self, width, height, interval,color):
#         # Dibujar líneas verticales
#         wh=Vec(width,height)@self.transf
#         width=wh[0]
#         height=wh[1]
#         for x in range(0, width, interval):
#             self.create_line(x, 0, x, height, fill=color, dash=(2, 2))
#         # Dibujar líneas horizontales
#         for y in range(0, height, interval):
#             self.create_line(0, y, width, y, fill=color, dash=(2, 2))
# 
# 
# #     def refresh(self, scene):
# #         tag="disc"
# #         self.delete(tag)
# #         for disc in scene.discs:
# #             disc.draw(self,tag=tag)
#     
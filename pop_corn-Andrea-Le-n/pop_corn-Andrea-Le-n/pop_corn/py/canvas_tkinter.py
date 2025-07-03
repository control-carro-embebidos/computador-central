import tkinter as tk
from ..matrix import Matrix

class Canvas_Tkinter:
    def __init__(self,scene,**props):#transf=None,height=900,width=1800,tk_master=None,grid=10 ):
        #self.canvas_width = cols
        #self.canvas_height = rows
        
        self.scene=scene
        scene.subscribe_canvas(self)
        props={'height':300,'width':300} | props
        self.props=props
        m,n=props['height'],props['width']
        if 'tk_master' not in props: 
            props['tk_master'] = tk.Tk()
        self.canvas = tk.Canvas(props['tk_master'],height=m,width=n,bg='white')#, **subset)
        self.canvas.pack()

        if 'transf' not in props:
            px_cm=100/150#min(m,n)/50
            transf=Matrix(3,3,
                               [px_cm,0,0,
                                0,px_cm,0,
                                n/2,m/2,1],has_tail=True)
            props['transf']=transf
        self.transf=props['transf']
        #print('tkinter_init',self.transf)
        if self.scene.get_background_at != None:
            xy=Matrix(m*n,2,
                      [k
                                  for i in range(m)
                                  for j in range(n)
                                  for k in (i,j)])
    #                   [(lambda k:i if k==0 else j if k==1 else 0)(k)
    #                               for i in range(m)
    #                               for j in range(n)
    #                               for k in range(3)])
            xy=xy@(self.transf.inv())
            xbm_image=self.xmb_format(Matrix(m,n,self.scene.get_background_at(xy)))
            bitmap = tk.BitmapImage(data=xbm_image, foreground="white", background="black")
            #bitmap = tk.BitmapImage(data=xbm_image, background="white", foreground="black")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=bitmap)
            self.canvas.image = bitmap
        self.debug_id=self.canvas.create_text(n/2,10,text='0')
        
    def xmb_format(self,matrix, threshold=128):
        height = matrix.m
        width = matrix.n
        
        xbm_data = []
        xbm_data.append(f'#define image_width {width}')
        xbm_data.append(f'#define image_height {height}')
        xbm_data.append('static char image_bits[] = {')
        
        for y in range(height):
            row_data = []
            for x in range(0, width, 8):
                byte = 0
                for bit in range(8):
                    if x + bit < width:
                        if matrix[y,x + bit] >= threshold:
                            byte |= (1 << bit)
                row_data.append(f'0x{byte:02x}')
            xbm_data.append('    ' + ', '.join(row_data) + ',')
        xbm_data[-1] = xbm_data[-1].rstrip(',')  # Remove trailing comma from the last row
        xbm_data.append('};')
        return '\n'.join(xbm_data)
    
    def oval(self, vertex,**options)->int:
        return self.canvas.create_oval(vertex@self.transf,**options)
        
    def rect(self, vertex,**options)->int:
        return self.canvas.create_rectangle(vertex@self.transf,**options)
        

    def text(self, vertex,**options)->int:
        return self.canvas.create_text(vertex[0:1,:]@self.transf,**options)

    def debug(self, text)->int:
        return self.canvas.itemconfig(self.debug_id,text=text)

    def	line(self, vertex,**options)->int:
        return self.canvas.create_line(vertex@self.transf,**options)
    
    def	poly(self, vertex,**options)->int:
        #print('tkinter_poly',type(vertex),type(self.transf))
        return self.canvas.create_polygon(vertex@self.transf,**options)
    
    #def coords(self, id_shape, list_vertex):
    #    self.canvas.coords(id_shape, list_vertex@self.transf)
            

    def draw_grid(self, width, height, interval,color):
        # Dibujar líneas verticales
        wh=Vec(width,height)@self.transf
        width=wh[0]
        height=wh[1]
        for x in range(0, width, interval):
            self.create_line(x, 0, x, height, fill=color, dash=(2, 2))
        # Dibujar líneas horizontales
        for y in range(0, height, interval):
            self.create_line(0, y, width, y, fill=color, dash=(2, 2))

    def delete(self,tag):
        self.canvas.delete(tag)

#     def refresh(self, scene):
#         tag="disc"
#         self.delete(tag)
#         for disc in scene.discs:
#             disc.draw(self,tag=tag)
    
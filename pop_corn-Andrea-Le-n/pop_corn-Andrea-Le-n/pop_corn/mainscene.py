from pop_corn.scene import Scene
from pop_corn.matrix import Matrix, Vec
from pop_corn.forces import collision, viscosity,magnetic


class MainScene(Scene):
#     def __init__(self,**props):
#         super().__init__(**props)
#         #self.poligons=[]
#         #self._pos
#         #self._angle
        
        
    def __init__(self,**props):
        self.subscribers_canvas=[]
        self._bg={
            'xy0':(-200,-200),
            'xy1':(200,200),
            'data_grayscale':None, #Matrix(20,10),
            'gray':255,
            'transf':None#self.get_bg_transf()
        }|props
        if self._bg['data_grayscale']==None:
            self.get_background_at=None
        else:
            self.get_background_at=self.fun_bg
        super().__init__(**props)
        self.forces += [collision, viscosity,magnetic]
        
    def get_bg_transf(self):
       x0,y0=self._bg['xy0']
       x1,y1=self._bg['xy1']
       m_data=self._bg['data_grayscale']
       return Matrix(3,3,[m_data.m/abs(x1-x0),0,0,
                          0,m_data.n/abs(y1-y0),0,
                          -x0*m_data.m/abs(x1-x0),-y0*m_data.n/abs(y1-y0),1])
#        return Matrix(3,3,[m_data.m/abs(x1-x0),0,0,
#                           0,m_data.n/abs(y1-y0),0,
#                           0,0,1])
        
    def fun_bg(self,xy):
        m_data=self._bg['data_grayscale']
        if m_data:
            if self._bg['transf'] == None:
                self._bg['transf'] = self.get_bg_transf()
            ij = xy @ (self._bg['transf'])
            list_grays=[]
            for rengl in range(ij.m):
                
                i,j = int(ij[rengl,0]), int(ij[rengl,1])
                if 0<i<m_data.m and 0<j<m_data.n: 
                    list_grays.append( m_data[i,j])
                else:
                    list_grays.append( self._bg['gray'])
            return list_grays
        else:
            return [self._bg['gray']]*xy.m


    def subscribe_canvas(self, canvas):
        if canvas not in self.subscribers_canvas:
            self.subscribers_canvas.append(canvas)

#    @staticmethod
#    def magnetic(disc):
#             dx=(disc.get_pos()[0]%disc.d_magne)-disc.d_magne/2
#             dy=(disc.get_pos()[1]%disc.d_magne)-disc.d_magne/2
#             dif=Vec(dx,dy)#Matrix(1,3,[dx,dy,1])
#             dist=dif.norm()
#             if dist==0:
#                 dist=disc.d_magne/1000
#             f_mag=(disc.k_magne/dist**3)*dif
#             return f_mag
#        return Vec(0,0)


#     def forces(self):
# 
#         n=len(self.discs)
#         for i in range(n):
#            for j in range(i):
#                 disc_i = self.discs[i] 
#                 disc_j = self.discs[j]
#                 #if disc_i.isparent(disc_j) or disk_j()
#                 dist=(disc_i.get_pos() - disc_j.get_pos()).norm()
#                 if dist<(disc_i.r+disc_j.r) :
#                     if dist<(disc_i.r+disc_j.r)/100:
#                         dist=(disc_i.r+disc_j.r)/100
#                     f_dir_ji=(disc_i.get_pos() - disc_j.get_pos())*(1/dist)
#                     dist=min(dist,disc_i.r,disc_j.r)
#                     k_elast=(disc_i.k_elast + disc_j.k_elast)/2
#                     f_ji=k_elast*dist*f_dir_ji
#                     disc_i.add_force(f_ji) #colition
#                     disc_j.add_force((-1)*f_ji) #colition
# 
#         for disc in self.discs:
#             #f_mag=self.magnetic(disc)
#             #disc.add_force(f_mag) #Magnetic Force floor
#             
#             #Parent attractor
# 
#             disc.add_force(-disc.k_frict*disc.get_vel())  # friction

    def refresh(self):
        self.calc_forces()
        for disc in self.discs:
            #print('.',end='')
            disc.refresh(1)            
        for canvas in self.subscribers_canvas:
            #print('#',end='')
            canvas.delete("disc")
            for disc in self.discs:
                #canvas.delete(disc.tag_disc)
                disc.draw(canvas)
        #self.calc_updates() 
    
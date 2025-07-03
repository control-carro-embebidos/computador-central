from pop_corn.matrix import Matrix, Vec

class Scene:
    def __init__(self,**props):
        self.discs=[]
        self.props=props
        self.parent=None
        self.forces=[]
        #self.updates=[]
    
   
    def add_disc(self,disc):
            self.discs.append(disc)
            #print(self.discs)
            
#     def scan_names(self,distance)
#         for disc

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
        
        
        
    def calc_forces(self):
        for force in self.forces:
            force(self)

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

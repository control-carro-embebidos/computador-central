#from ..Matrix import Matrix

class Canvas_print:
    def __init__(self,transf=None,rows=900,cols=1800,tk_master=None,grid=10 ):
        if input("Canvas_print\n")== 'exit':exit
        print(f"__init__( transf={transf}, rows={rows}, cols={cols}, tk_master={tk_master}, grid={grid})")
    
    def oval(self, vertex,**options)->int:
        print(f"oval( {vertex},{options})")
        return input()
        
    def rect(self, vertex,**options)->int:
        return input(f"rect( {vertex},{options})")
        
    def text(self, vertex,**options)->int:
        return input(f"text( {vertex},{options})")
 
    def	line(self, vertex,**options)->int:
        return input(f"line( {vertex},{options})")
    
            

    def delete(self):
        print("delete()")

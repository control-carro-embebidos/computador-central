#Change by Canvas_bytesbuffer

from pop_corn.matrix import Matrix, Vec


class Canvas_Matrix:
    def __init__(self,scene, matrix=None,width=None,height=None):
        self.scene=scene
        scene.subscribe_canvas(self)
        if matrix!=None:
            self.matrix = matrix
        elif width==None and height==None:
            self.matrix=Matrix(30,40)
        elif width==None:
            self.matrix=Matrix(height,height)
        elif height==None:
            self.matrix=Matrix(width,width)
        else:
            self.matrix=Matrix(width,height)

        #self.width = matrix.m
        #self.height = matrix.n
            

    def oval(self, vertex, value=255, **options):
        x1,y1,x2,y2=vertex.tolist()
        x_center, y_center, x_radius, y_radius=(x1+x2)/2,(y1+y2)/2,abs(x1-x2)/2,abs(y1-y2)/2
        for i in range(self.matrix.m):
            for j in range(self.matrix.n):
                if (((i - x_center) ** 2) / (x_radius ** 2) + ((j - y_center) ** 2) / (y_radius ** 2)) <= 1:
                    self.matrix[i, j] = value

    def rect(self, vertex, value=255, **options):
        x1,y1,x2,y2=vertex.tolist()
        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                if 0 <= i < self.matrix.m and 0 <= j < self.matrix.n:
                    self.matrix[i, j] = value

    def line(self,vertex, value=255, **options):
        x1,y1,x2,y2=vertex.tolist()
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1

        if dx > dy:
            err = dx / 2.0
            while x != x2:
                if 0 <= x < self.matrix.m and 0 <= y < self.matrix.n:
                    self.matrix[x, y] = value
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y2:
                if 0 <= x < self.matrix.m and 0 <= y < self.matrix.n:
                    self.matrix[x, y] = value
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        if 0 <= x2 < self.matrix.m and 0 <= y2 < self.matrix.n:
            self.matrix[x2, y2] = value

    def text(self,vertex,text,**options):
        pass

    def debug(self,text,**options):
        pass
    
    def poly(self, vertex,**options)->int:
         pass
    
    def delete(self,tag):
        pass

# Example usage
# m = Matrix(20, 20)
# canvas = Canvas_Matrix(m)
# canvas.draw_oval(10, 10, 5, 3)
# canvas.draw_rectangle(3, 3, 7, 7)
# canvas.draw_line(0, 0, 19, 19)
# print(canvas.matrix)

class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self):
        return(f"(x={self.x},y={self.y})")
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
v1 = Vector(2,5)
print(v1)

v2 = Vector(3,7)
print(v2)

v3 = v1+ v2
print(v3)
print("sześciokąt:")
class sześcian:
    def __init__(self,_a) -> None:
        self.a = _a
        self.Pc = 6*_a**2
        self.V = _a**3
    def inf(self):
        print(f"Pc= {self.Pc}")
        print(f"V = {self.V}") 
        
k1 = sześcian(5)
k1.inf()
print("ostosłup czworokątny:")

class ostrosłup_czworokątny:
    def __init__(self,_a,_h) -> None:
        self.a = _a
        self.h = _h
        self.Pc = _a**2 + 2*_a*_h
        self.V  = int(1/3*_a**2*_h)

    def inf(self):
        print(f"Pc= {self.Pc}")
        print(f"V = {self.V}")           
              
o1 = ostrosłup_czworokątny(3,8)
o1.inf()
print("graniastosłup czworokątny:")

class graniastosłup_czworokątny:
    def __init__(self,_a,_b,_h) -> None:
        self.a = _a
        self.h = _h
        self.b = _b
        self.Pc = 2*_a*_h * 2*_a*_b * 2*_a*_b 
        self.V  = int(_a*_b*_h)

    def inf(self):
        print(f"Pc= {self.Pc}")
        print(f"V = {self.V}")           
              
g1 = ostrosłup_czworokątny(13,6)
g1.inf()


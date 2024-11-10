class Caja:
    
    def __init__(self, id=0, cola=0, tiempoUso=0, tiempoLibre=0, tiempoActual=0):
        self.id = id
        self.cola = cola
        self.tiempoUso = tiempoUso
        self.tiempoLibre = tiempoLibre
        self.tiempoActual = tiempoActual
        
    def setTiempoActual(self, tiempoActual):
        self.tiempoActual = tiempoActual

    def getTiempoActual(self):
        return self.tiempoActual

    def setTiempoUso(self, tiempoUso):
        self.tiempoUso = tiempoUso 

    def getTiempoUso(self):
        return self.tiempoUso
    
    def setTiempoLibre(self, tiempoLibre):
        self.tiempoLibre = tiempoLibre 

    def getTiempoLibre(self):
        return self.tiempoLibre
    
    def getCola(self):
        return self.cola
    
    def setCola(self, cola):
        self.cola = cola

    def getId(self):
        return self.id 

    def setId(self, id):
        self.id = id

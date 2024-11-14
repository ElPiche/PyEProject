class Caja:
    
    def __init__(self, id=0, cola=0, tiempoUso=0, tiempoLibre=0, tiempoActual=0, listaTiempoUso=None, listaTiempoActual=None):
        self.id = id
        self.cola = cola
        self.tiempoUso = tiempoUso
        self.tiempoLibre = tiempoLibre
        self.tiempoActual = tiempoActual
        self.listaTiempoUso =  listaTiempoUso if listaTiempoUso is not None else []
        self.listaTiempoActual = listaTiempoActual if listaTiempoActual is not None else []
    
    def setListaTiempoActual(self, listaTiempoActual):
        self.listaTiempoActual = listaTiempoActual

    def getListaTiempoActual(self):
        return self.listaTiempoActual
    
    def setListaTiempoUso(self, listaTiempoUso):
        self.listaTiempoUso = listaTiempoUso

    def getListaTiempoUso(self):
        return self.listaTiempoUso
        
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

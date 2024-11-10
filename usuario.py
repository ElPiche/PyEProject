class User:
     
    def __init__(self, tiempoEspera, tiempoCaja, tiempoLlegada, productos):
        self.tiempoEspera = tiempoEspera
        self.tiempoCaja = tiempoCaja
        self.tiempoLlegada = tiempoLlegada
        self.productos = productos

    def __init__(self):
        pass  # Esto indica que el constructor no hace nada específico
    
    def setTiempoEspera(self, tiempoEspera):
        self.tiempoEspera = tiempoEspera

    def getTiempoEspera(self):
        return self.tiempoEspera
    
    def setProductos(self, productos):
        self.productos = productos

    def getProductos(self):
        return self.productos
    
    def setTiempoLlegada(self, tiempoLlegada):
        self.tiempoLlegada = tiempoLlegada

    def getTiempoLlegada(self):
        return self.tiempoLlegada
    
    def setTiempoCaja(self, tiempoCaja):
        self.tiempoCaja = tiempoCaja

    def getTiempoCaja(self):
        return self.tiempoCaja


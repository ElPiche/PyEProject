class User:
     
    def __init__(self, tiempoEspera, tiempoCaja, tiempoLlegada, productos):
        self.tiempoEspera = tiempoEspera
        self.tiempoCaja = tiempoCaja
        self.tiempoLlegada = tiempoLlegada
        self.productos = productos

    def __init__(self):
        pass  # Esto indica que el constructor no hace nada específico
    
    def set_tiempoEspera(self, tiempoEspera):
        self.tiempoEspera = tiempoEspera

    def get_tiempoEspera(self):
        return self.tiempoEspera
    
    def set_Productos(self, productos):
        self.productos = productos

    def get_Productos(self):
        return self.productos
    
    def set_tiempoLlegada(self, tiempoLlegada):
        self.tiempoLlegada = tiempoLlegada

    def get_tiempoLlegada(self):
        return self.tiempoLlegada
    
    def set_tiempoCaja(self, tiempoCaja):
        self.tiempoCaja = tiempoCaja

    def get_tiempoCaja(self):
        return self.tiempoCaja


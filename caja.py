class Caja:
    
    def __init__(self, libre, tiempoUso, tiempoLibre, cola):
        self.libre = libre
        self.tiempoUso = tiempoUso
        self.tiempoLibre = tiempoLibre
        self.cola = cola
    
    def __init__(self):
        pass  # Esto indica que el constructor no hace nada específico

    def set_libre(self, libre):
        self.libre = libre 

    def get_libre(self):
        return self.libre
    
    def set_tiempoUso(self, tiempoUso):
        self.tiempoUso = tiempoUso 

    def get_tiempoUso(self):
        return self.tiempoUso
    
    def set_tiempoLibre(self, tiempoLibre):
        self.tiempoLibre = tiempoLibre 

    def get_tiempoLibre(self):
        return self.tiempoLibre
    
    def set_cola(self, cola):
        self.cola = cola

    def get_cola(self):
        return self.cola

import matplotlib.pyplot as plt 
import numpy as np 
import scipy.stats as ss

from usuario import User
from caja import Caja

#import timeit

#Instalar librerias:
#pip install matplotlib
#pip install matplotlib pandas numpy Este comando de aca deberia instalar 3 librerias.
#pip install SciPy

# Show the figure.

#Probabilidad del pago, utilizando una variable de Bernolli
#1(exito) paga en efectivo y consume 2 minutos (120 segundos)
#caso contrario paga con otro metodo consumiendo 70 segundos.
def pagoProb(p):
    bernoulliResult = ss.bernoulli(p)
    result = bernoulliResult.rvs()
    
    if result == 1:
        return 120
    else:
        return 70

#Obtener cantidad de productos al azar utilizando distribucion normal
def productos(media, varianza):
    while True:
        cantidadProductos = int(ss.norm(media, varianza).rvs())
        cantidadProductos = abs(cantidadProductos)  # Asegurarse de que sea positivo
        if cantidadProductos != 0:
            return cantidadProductos

#Asignar a un conjunto de clientes un tiempo de llegada utilizando
#Distribucion de poisson, el primer cliente siempre llega en tiempo 0.
def tiempoLlegada(media, nroClientes):
    llegadas = np.random.poisson(media, nroClientes-1)
    llegadas = np.insert(llegadas, 0, 0)
    return abs(llegadas)


def main():

    cant_usuarios = 6
    usuarios = []

    cajas = 3
    cajaArray = []

    p = 0.4
    media = 5 #mu
    varianza = 3 #sigma
    llegadas = tiempoLlegada(3,100)

    metodoEleccion = 2 #0 para fila unica y 1 para fila x caja

    #Al usuario se le asigna un tiempo de llegada basado en la distribucion poisson
    #Y se le asignan productos basado en la distribucion normal
    for i in range (0, cant_usuarios):
        usuarios.append(User())
        usuarios[i].setTiempoLlegada(llegadas[i] * 60)
        usuarios[i].setProductos(productos(media, varianza) * 60)
        usuarios[i].setTiempoEspera(0)
    
    #Se crean las cajas y se colocan en libre (Para el metodo de fila unica)
    for i in range (0, cajas):
        cajaArray.append(Caja())
        cajaArray[i].setId(i)
        cajaArray[i].setTiempoActual(0)
        cajaArray[i].setTiempoUso(0)
        cajaArray[i].setTiempoLibre(0)

    if(metodoEleccion == 0):
        for user in usuarios:
            print("\nMetodo de fila unica")
            
            #Obtener la caja con menor tiempo de espera
            caja = min(cajaArray, key=lambda caja: caja.getTiempoActual())
            menorTiempoOcupacion = caja.getTiempoActual()
            
            #Se obtiene el menor tiempoActual de la caja, es decir la caja en la que el usuario esperará menos 
            #para asignarlo a la misma
            if((user.getTiempoLlegada() - menorTiempoOcupacion) < 0):
                user.setTiempoEspera(abs(user.getTiempoLlegada() - menorTiempoOcupacion))
                metodoPago = pagoProb(p)
                caja.setTiempoUso(caja.getTiempoUso() + (user.getProductos()+ metodoPago))
                caja.setTiempoActual(user.getProductos()+ metodoPago)
        
            else:
                caja.setTiempoLibre(caja.getTiempoLibre() + (user.getTiempoLlegada() - menorTiempoOcupacion))
                user.setTiempoEspera(0)
                metodoPago = pagoProb(p)
                caja.setTiempoUso(caja.getTiempoUso() + (user.getProductos()+ metodoPago))
                caja.setTiempoActual(user.getProductos()+ metodoPago)
                                            
    else:
        print("\nMetodo de filas en cajas")
        
        for user in usuarios:
            #Obtener la fila mas pequeña de las cajas
            caja = min(cajaArray, key=lambda caja: caja.getCola())
            caja.setCola(caja.getCola() + 1)
            menorTiempoOcupacion = caja.getTiempoActual()
            
            if((user.getTiempoLlegada() - menorTiempoOcupacion) < 0):
                user.setTiempoEspera(abs(user.getTiempoLlegada() - menorTiempoOcupacion))
                metodoPago = pagoProb(p)
                caja.setTiempoUso(caja.getTiempoUso() + (user.getProductos()+ metodoPago))
                caja.setTiempoActual(user.getProductos()+ metodoPago)
        
            else:
                caja.setTiempoLibre(caja.getTiempoLibre() + (user.getTiempoLlegada() - menorTiempoOcupacion))
                user.setTiempoEspera(0)
                metodoPago = pagoProb(p)
                caja.setTiempoUso(caja.getTiempoUso() + (user.getProductos()+ metodoPago))
                caja.setTiempoActual(user.getProductos()+ metodoPago)
                
            print("\nCaja: " + str(caja.getId()))
            print("Personas en la caja: " + str(caja.getCola()))
            print("Tiempo Ocupacion: " + str(menorTiempoOcupacion)) 
            print("Metodo pago: " + str(metodoPago)+ " segundos")
            print("Tiempo de uso: " + str(caja.getTiempoUso())+ " segundos")
            print("Tiempo Actual: " + str(caja.getTiempoActual())+ " segundos")
            print("Tiempo Libre: " + str(caja.getTiempoLibre())+ " segundos") 
            
            print("\nCantidad de productos: " + str(user.getProductos()))
            print("Tiempo llegada del usuario " + str(user.getTiempoLlegada()))
            print("Tiempo de espera del usuario: " + str(user.getTiempoEspera()))


                
"""
    for caja in cajaArray:
        print("\nCaja: " + str(caja.getId()))
        print("Tiempo de uso: " + str(caja.getTiempoUso())+ " segundos")
        print("Tiempo Actual: " + str(caja.getTiempoActual())+ " segundos")
        print("Tiempo Libre: " + str(caja.getTiempoLibre())+ " segundos")        
            
    for usuario in usuarios:
        print("\nCantidad de productos: " + str(usuario.getProductos()))
        print("Tiempo llegada del usuario " + str(usuario.getTiempoLlegada()))
        print("Tiempo de espera del usuario: " + str(usuario.getTiempoEspera()))



    #Grafica tiempo de uso cajas.

    #Grafica tiempo de espera de cada cliente en la fila antes de ser atendido

    print("Datos a presentar:")
    #Presentar valores, valor medio y desviacion estandar para el tiempo de uso de cada una de las cajas.
    print("Valor medio y desviacion estandar para el tiempo de uso de cada una de las cajas:\n")

    #Presentar valores, valor medio y desviacion estandar para el tiempo de espera en la fila
    #de cada cliente en la fila antes de ser atendido

    print("Valor medio y desviacion estandar para el tiempo de espera en la fila de cada cliente en la fila antes de ser atendido. \n")
    
    print("Valor medio: " + "\n Desviación estandar: ")

    #Tiempo libre de cada caja.

    print("Tiempos en los que las cajas estuvieron libres:\n")
    print("Caja: Nº" + ", tiempo libre:")


   # fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    #ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
   # plt.show()
     
"""

if __name__ == "__main__":
    main()
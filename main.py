import matplotlib.pyplot as plt 
import numpy as np 

import scipy.stats as ss

from usuario import User
from caja import Caja

#import timeit

#Instalar librerias:
#pip install matplotlib
#pip install matplotlib pandas numpy Este comando de aca deberia instalar 3 librerias.

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
def productos(mu, sigma):
    cantidad_productos = int(ss.norm(mu, sigma).rvs())
    return cantidad_productos

#Asignar a un conjunto de clientes un tiempo de llegada utilizando
#Distribucion de poisson, el primer cliente siempre llega en tiempo 0.
def tiempoLlegada(mu, n_clientes):
    llegadas = np.random.poisson(mu, n_clientes-1)
    llegadas = np.insert(llegadas, 0, 0)
    return llegadas



def main():

    # tipoPago = pagoProb(0.4)

    users = 100
    user = []
    p = 0.4
    cajas = 5
    cajaArray = []

    mu = 5
    sigma = 3

    llegadas = tiempoLlegada(3,100)

    #Al usuario se le asigna un tiempo de llegada basado en la distribucion poisson
    #Y se le asignan productos basado en la distribucion normal
    for i in range (0,users):
        user.append(User())
        user[i].set_tiempoLlegada(llegadas[i])
        user[i].set_Productos(productos(mu, sigma))
    
    for i in range (0, cajas):
        cajaArray.append(Caja())
        cajaArray[i].set_libre("true")

    
    print("\nTiempo llegada pos 3")
    print(user[3].get_tiempoLlegada())
    print(user[3].get_Productos())

   # fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    #ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
   # plt.show()  


if __name__ == "__main__":
    main()
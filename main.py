import matplotlib.pyplot as plt 
import numpy as np 
import scipy.stats as ss
import random

from usuario import User
from caja import Caja

#Instalar librerias:
#pip install matplotlib
#pip install matplotlib pandas numpy Este comando de aca deberia instalar 3 librerias.
#pip install SciPy



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

    cant_usuarios = 15
    usuarios = []

    cajas = 3
    cajaArray = []

    p = 0.4
    media = 5 #mu
    varianza = 3 #sigma
    llegadas = tiempoLlegada(media,cant_usuarios)

    metodoEleccion = 1 #0 para fila unica y cualquier numero para fila x caja

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
        cajaArray[i].setId(i+1)


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
                caja.getListaTiempoUso().append(user.getProductos()+ metodoPago)

            else:
                caja.setTiempoLibre(caja.getTiempoLibre() + (user.getTiempoLlegada() - menorTiempoOcupacion))
                user.setTiempoEspera(0)
                metodoPago = pagoProb(p)
                caja.setTiempoUso(caja.getTiempoUso() + (user.getProductos()+ metodoPago))
                caja.setTiempoActual(user.getProductos()+ metodoPago)
                caja.getListaTiempoUso().append(user.getProductos()+ metodoPago)

    else:
        
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
                caja.getListaTiempoUso().append(user.getProductos()+ metodoPago)
        
            else:
                caja.setTiempoLibre(caja.getTiempoLibre() + (user.getTiempoLlegada() - menorTiempoOcupacion))
                user.setTiempoEspera(0)
                metodoPago = pagoProb(p)
                caja.setTiempoUso(caja.getTiempoUso() + (user.getProductos()+ metodoPago))
                caja.setTiempoActual(user.getProductos()+ metodoPago)
                caja.getListaTiempoUso().append(user.getProductos()+ metodoPago)
 
    # 1. Grafica tiempo de uso cajas.
    graficarCajas(cajaArray)
    
    # 2. Grafica tiempo de espera de cada cliente en la fila antes de ser atendido
    graficarUsuarios(usuarios)
    
    # 3 y 5. Presentar valores, valor medio y desviacion estandar para el tiempo de uso de cada una de las cajas.    
    print("Valor medio, desviacion estandar para el tiempo de uso de cada una de las cajas y tiempo libre:\n")
    for caja in cajaArray:
        media = np.mean(caja.getListaTiempoUso())
        desviacion = round(np.std(caja.getListaTiempoUso()), 4) 
        print("Caja Nº: " + str(caja.getId()))
        print("Valor medio: " + str(media))
        print("Desviacion estandar: " +  str(desviacion))
        print("Tiempo total libre de la caja: " + str(caja.getTiempoLibre()) + "\n")
    
    
    # 4. Presentar valores, valor medio y desviacion estandar para el tiempo de espera en la fila
    #de cada cliente en la fila antes de ser atendido
    
    print("\nValor medio y desviacion estandar para el tiempo de espera en la fila de cada cliente en la fila antes de ser atendido. ")
    tiempos_espera = [user.getTiempoEspera() for user in usuarios]
    media_espera = np.mean(tiempos_espera)
    desviacion_espera = round(np.std(tiempos_espera), 4)
    print("Valor medio: " + str(media_espera))
    print("Desviación estandar: " + str(desviacion_espera) + "\n")

     

    
def graficarCajas(cajaArray):
    tiemposCajas = []
      
    for caja in cajaArray:
        tiemposCajas.append(caja.getTiempoUso())
         
    etiquetas = [f"Caja {i+1}" for i in range(len(cajaArray))]      

    colores = ['blue', 'lightgreen', 'skyblue', 'purple', 'green']
    #seleccion = random.choices(colores)
    plt.figure(figsize=(8,6))
    plt.bar(etiquetas, tiemposCajas, color=colores[:len(etiquetas)], width=0.5)   
    plt.ylabel("Tiempo de uso de cajas (segundos)")
    plt.title("Grafica tiempo de uso de las cajas")
    plt.show()
   
def graficarUsuarios(usuarios):
    tiemposEspera = []
    for user in usuarios:
        tiemposEspera.append(user.getTiempoEspera())    
    
    etiquetas = [f"Usuario {i+1}" for i in range(len(usuarios))]      

    colores = ['blue', 'lightgreen', 'skyblue', 'purple', 'green']
    seleccion = random.choices(colores)
    plt.figure(figsize=(10,8))
    plt.bar(etiquetas, tiemposEspera, color=seleccion, width=0.5)   
    plt.ylabel("Tiempo de espera clientes en (segundos)")
    plt.title("Grafica tiempo de espera de los clientes")
    plt.xticks(rotation=90)
    plt.show()
    
    


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 08:29:31 2021

@author: Clara Roig
"""

import fileparse   #utiliza el módulo fileparse de este mismo repositorio


#definimos la función para crear una lista con la mercadería del camión
#que contiene diccionarios que especifican nombre, cantidad de cajones y precio por cajón

def leer_camion (nombre_archivo1):
    
    with open(nombre_archivo1) as file:
        contenido = fileparse.parse_csv(file, select = ['nombre', 'cajones', 'precio'], types = [str, float, float])
                 
    return contenido





#definimos una función para leer los datos de los precios de venta
#creando un diccionario que especifica nombre y precio


def leer_precios(nombre_archivo2):
    
    with open(nombre_archivo2) as file:
        registros = fileparse.parse_csv(file, types = [str, float], has_headers = False)
    
        registro_precios = dict((nombre, precio) for nombre, precio in registros)
    
    return registro_precios



#calculamos los gastos de compra de la mercadería


def gastos(nombre_archivo1):
    
    mercaderia = leer_camion(nombre_archivo1)

    gastos = 0

    for n_registro, registro in enumerate(mercaderia):
        
        try:
            ncajones = int(registro['cajones'])
            precio = float(registro['precio'])
            gastos += ncajones * precio
                    
            return gastos
        
        except ValueError:
            print(f'Fila {n_registro}: No pude interpretar: {registro}')





#calculamos los ingresos de las ventas de esta mercadería    


def ventas(nombre_archivo1, nombre_archivo2):

    ventas = 0
    
    mercaderia = leer_camion(nombre_archivo1)
    
    precios = leer_precios(nombre_archivo2)
        
        
    for n_registro, registro in enumerate(mercaderia):
        
        try:
            if registro ['nombre'] in precios:        
                ncajones = int(registro['cajones'])
                precio = float(precios[registro['nombre']])
                ventas += ncajones * precio
                
            return ventas
        
        except ValueError:
                continue



#calculamos el balance del negocio


def hacer_balance(nombre_archivo1, nombre_archivo2):
    
    egresos = gastos(nombre_archivo1)
    
    ingresos = ventas(nombre_archivo1, nombre_archivo2)

    balance = ingresos - egresos
    
    return balance



# definimos la función para hacer la lista con los datos para el informe






def hacer_informe(nombre_archivo1, nombre_archivo2):
    
    
    mercaderia = leer_camion(nombre_archivo1)
    
    precios = leer_precios(nombre_archivo2)
    
    informe = []
    
    for row in mercaderia:
        
                
        informe.append((row['nombre'], int(row ['cajones']), precios[row['nombre']], (precios[row['nombre']] - float(row['precio']))))
    
    return informe



#definimos una función para imprimir el informe



def informe_camion(nombre_archivo1, nombre_archivo2):
    
    informe = hacer_informe(nombre_archivo1, nombre_archivo2)


    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')


    print (f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print (('-'*10 + ' ')*4)

    for nombre, cajones, precio, cambio in informe:
    
        precio = '$' + str('%0.2f' % precio)
    
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')




## definimos una función para imprimir el balance


def imprimir_balance(nombre_archivo1, nombre_archivo2):
    
    balance = hacer_balance(nombre_archivo1, nombre_archivo2)


    if balance > 0:
        comentarios = 'hubo ganancias. Todo va bien!'
    elif balance == 0:
        comentarios = 'no hubo ganancias ni pérdidas. Hay que mejorar.'
    else:
        comentarios = 'hubo pérdidas. Hay que pensar un plan de acción!!'

    print()
    print (f'El gasto fue de ${gastos:0.2f} y las ventas fueron de ${ventas:0.2f}. Esto da un balance de ${balance:0.2f}, por lo que {comentarios}')




##############


def f_principal(parametros):
    
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    camion = parametros[1]
    precios = parametros[2]
    informe_camion(camion, precios)
    




if __name__ == '__main__':
    import sys
    f_principal(sys.argv)



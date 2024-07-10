import random
import csv

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos_trabajadores = {}


def asignar_sueldos(trabajadores):
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos_trabajadores[trabajador] = sueldo
        print("Sueldos asignados correctamente")
        

def clasificar_sueldos(sueldos_trabajadores):
    clasificacion_menor = {} #menor a $800.000
    clasificacion_mid = {} #entre $800.000 y $2.000.000
    clasificacion_mayor = {} #mayor a $2.000.000

    for trabajador,sueldo in clasificacion_menor:
        print("Sueldos menores a 800000 TOTAL:",len(clasificacion_menor))
        print(clasificacion_menor)

    for trabajador,sueldo in clasificacion_mid:
        print("Sueldos entre 800000 y $2000000 TOTAL:",len(clasificacion_mid))
        print(clasificacion_mid)

    for trabajador,sueldo in clasificacion_mayor:
        print("Sueldos mayores a $2000000 TOTAL:",len(clasificacion_mayor))
        print(clasificacion_mayor)

    total_sueldos = sum(sueldos_trabajadores)
    print("TOTAL SUELDOS: $", total_sueldos)


def mostrar_estadisticas(sueldos_trabajadores):
    sueldo_menor = min(sueldos_trabajadores)
    sueldo_mayor = max(sueldos_trabajadores)
    promedio_sueldos = sum(sueldos_trabajadores) / len(sueldos_trabajadores)

    print("Sueldo menor: ", sueldo_menor)
    print("Sueldo mayor: ", sueldo_mayor)
    print("Promedio de sueldos: ", promedio_sueldos)


def reporte_sueldos(sueldos_trabajadores):
    desc_salud = sueldos_trabajadores * 0.07
    desc_afp = sueldos_trabajadores * 0.12
    sueldo_liquido = sueldos_trabajadores - desc_salud - desc_afp

    resumen_sueldos = {
        'Nombre empleado' : trabajadores,
        'Sueldo base' : sueldos_trabajadores,
        'Descuento salud' : desc_salud,
        'Descuento AFP' : desc_afp,
        'Sueldo líquido' : sueldo_liquido
    }

    print(resumen_sueldos)
    print("Se creó una copia en reporte_sueldos.csv")

    with open ('reporte_sueldos.csv','w','newline=') as archivo:
        escritor = csv.writerow(trabajadores, sueldos_trabajadores, desc_salud, desc_afp, sueldo_liquido,'delimiter=')
        archivo = escritor.write(['Trabajador', 'Sueldo base', 'Desc. Salud', 'Desc. AFP', 'Sueldo Liquido'])
    
        

def menu():
    while True:
        print("Empresa X")
        print("1. Asignar sueldos")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir")
        try:
            opcion = int(input("Ir a: "))
            if opcion == 1:
                asignar_sueldos(trabajadores)
            elif opcion == 2:
                clasificar_sueldos(sueldos_trabajadores)
            elif opcion == 3:
                mostrar_estadisticas(sueldos_trabajadores)
            elif opcion == 4:
                reporte_sueldos(sueldos_trabajadores)
            elif opcion == 5:
                print("Saliendo del sistema.")
                print("Desarollado por Sofia Blau Rodriguez.")
                print("RUT 21.101.913-1")
                break
            else:
                print("Debe ingresar una opcion de 1 a 5.")
        except ValueError:
            print("Debe ingresar una opcion de 1 a 5.")

menu()
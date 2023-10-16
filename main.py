import csv
import os

# Función para registrar ingresos
def registrar_ingreso(monto, descripcion):
    with open('contabilidad.csv', mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Ingreso', monto, descripcion])

# Función para registrar gastos
def registrar_gasto(monto, descripcion):
    with open('contabilidad.csv', mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Gasto', monto, descripcion])

# Función para calcular el saldo
def calcular_saldo():
    saldo = 0
    with open('contabilidad.csv', mode='r') as archivo_csv:
        reader = csv.reader(archivo_csv)
        # Omitir la primera fila que contiene los encabezados
        next(reader)
        for row in reader:
            tipo, monto, descripcion = row
            monto = float(monto)
            if tipo == 'Ingreso':
                saldo += monto
            elif tipo == 'Gasto':
                saldo -= monto
    return saldo

# Función principal
def main():
    while True:
        print("\nSistema de Contabilidad")
        print("1. Registrar Ingreso")
        print("2. Registrar Gasto")
        print("3. Calcular Saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            monto = float(input("Ingrese el monto del ingreso: "))
            descripcion = input("Ingrese la descripción: ")
            registrar_ingreso(monto, descripcion)
        elif opcion == '2':
            monto = float(input("Ingrese el monto del gasto: "))
            descripcion = input("Ingrese la descripción: ")
            registrar_gasto(monto, descripcion)
        elif opcion == '3':
            saldo = calcular_saldo()
            print(f"El saldo actual es: {saldo}")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    if not os.path.exists('contabilidad.csv'):
        with open('contabilidad.csv', mode='w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['Tipo', 'Monto', 'Descripción'])
    
    main()

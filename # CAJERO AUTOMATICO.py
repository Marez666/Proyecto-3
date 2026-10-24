#  CAJERO AUTOMATICO 
denominaciones = [500, 200, 100]# billetes disponibles
while True:
    try:#  ingreso de monto a retirar
        m = int(input("Ingrese el monto a retirar: "))
    except ValueError:# en caso de que no sea un número entero, se captura el error y se le pide al usuario que ingrese un número válido
        print("Por favor, ingrese un número válido.")
        continue
# Validación de condiciones
    if m % 100 != 0:# multiplo de 100
        print("El monto debe ser múltiplo de 100.")
        continue
    elif m > 10000:# máximo a retirar
        print("El monto máximo a retirar es de 10,000.")
        continue
    elif m < 0:# debe ser positivo, no negativo
        print("El monto debe ser un número positivo.")
        continue
    elif m == 0:# no puede ser cero
        print("El monto debe ser mayor que cero.")
        continue
    elif m == "X" or m == "x":# si el usuario ingresa X o x, se sale del bucle
        print("Cancelando operación.")
        break
    else:# si todas las condiciones se cumplen, se imprime el mensaje de retiro exitoso y se sale del bucle
        print(f"Retiro exitoso de ${m} pesos.")
        break
for billete in denominaciones:# se recorre la lista de billetes disponibles
    cantidad = m // billete# se calcula la cantidad de billetes de cada denominación
    if cantidad > 0:# si hay billetes de esa denominación, se imprime la cantidad y el valor del billete
        print(f"{cantidad} billetes de ${billete}")
        m -= cantidad * billete# se resta el valor de los billetes retirados al monto total
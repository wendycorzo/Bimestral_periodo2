"""Ejercicio: Bimestral Teoría-Práctica
Presentado por: Wendy Vanessa Vargas Corzo

El cajero de un banco solo dispone de billetes de
$10000, $2000 y monedas de $100. Su función es
cambiar los cheques a los clientes, dándoles el
menor número posible de billetes. Asumiendo que
todos los cheques son múltiples de $100, hacer el
diagrama de flujo y el programa en Python que
reciba el valor del cheque a cambiar y que le
informe al cajero cuántos billetes de cada
denominación debe entregar. Como no se sabe
cuántos clientes vienen en un día, el programa
debe terminar cuando reciba cero como valor del
cheque, y al final del día debe informar cuántos
billetes de cada denominación se gastaron.
"""

# Entradas
print("-----------------------")
print("Ingresa el valor a retirar en multiplos de 100 (Cero para salir):")
print("-----------------------")
retiro = float(input())

# Inicio ciclo mientras

while retiro > 0:
    # Calculos
    monedas_de_100 = retiro
    billetes_de_10000 = (monedas_de_100-monedas_de_100%10000)/10000
    monedas_de_100 = monedas_de_100%10000
    billetes_de_2000 = (monedas_de_100-monedas_de_100%2000)/2000
    monedas_de_100 = monedas_de_100%2000/100
    # Salidas
    print("Cantidad billetes de 10000: ",billetes_de_10000)
    print("Cantidad billetes de 2000: ",billetes_de_2000)
    print("Cantidad monedas de 100: ",monedas_de_100)
    # Reinicio
    print("Ingresa el valor a retirar en multiplos de 100 (Cero para salir): ")
    retiro = float(input())
print("Programa terminado")
# Entradas
print("-----------------------")
print("Ingresa el valor a retirar en multiplos de 100 (Cero para salir):")
print("-----------------------")
retiro = float(input())

# Inicio ciclo mientras

while retiro > 0:
    # Calculos
    monedas_de_100 = retiro
    billetes_de_10000 = (monedas_de_100-monedas_de_100%10000)/10000
    monedas_de_100 = monedas_de_100%10000
    billetes_de_2000 = (monedas_de_100-monedas_de_100%2000)/2000
    monedas_de_100 = monedas_de_100%2000/100
    # Salidas
    print("Cantidad billetes de 10000: ",billetes_de_10000)
    print("Cantidad billetes de 2000: ",billetes_de_2000)
    print("Cantidad monedas de 100: ",monedas_de_100)
    # Reinicio
    print("Ingresa el valor a retirar en multiplos de 100 (Cero para salir): ")
    retiro = float(input())
print("Programa terminado")
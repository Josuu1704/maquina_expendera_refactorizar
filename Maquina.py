import os;

Productos = ["Agua", "Refrescos", "Zumos"]
Precios = [0.50, 0.75, 0.95]
ReservasMonedas = [20, 20, 20, 20, 20]
ValoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]


def menu(Productos, precios):
    cont = 0
    textomenu = ""
    for nombre in Productos:
        textomenu += f"{cont + 1} - {nombre} = {precios[cont]} \n"
        cont += 1
    textomenu += f"{cont + 1} - Salir"
    return textomenu


def ProductosElegido(opcion, Productos, Precios):
    if opcion == 1 or opcion == 2 or opcion == 3:
        return f"\nHas escogido {Productos[opcion - 1]} \nTotal a pagar: {Precios[opcion - 1]}"
    elif opcion == 4:
        return "Fin del Programa"


def MonedasIngresadas(SumaPago, Precios, ReservasMonedas, ValoresMonedas, opcion):
    precio = Precios[opcion - 1]
    if SumaPago < precio:
        return f"Cantidad insuficiente, faltan {round(precio - SumaPago, 2)}"
    cambio = round(SumaPago - precio, 2)
    mensaje = f"Pago recibido: {SumaPago} \nCantidad devuelta: {cambio} \n"
    for i in range(len(ReservasMonedas)):
        valor = ValoresMonedas[i]
        while cambio >= valor and ReservasMonedas[i] > 0:
            cambio = round(cambio - valor, 2)
            ReservasMonedas[i] -= 1
    if cambio < 0:
        return "No hay suficiente cambio disponible."
    return mensaje + "Pago completado"


opcion = 0
while opcion != 4:
    continuar = True
    print(menu(Productos, Precios))
    opcion = int(input("Escoge una opcion: "))
    os.system("cls")
    if opcion == 4:
        print(ProductosElegido(opcion, Productos, Precios))
        continuar = False
    else:
        print(ProductosElegido(opcion, Productos, Precios))
        SumaPago = 0
        while continuar:
            print(MonedasIngresadas(SumaPago, Precios, ReservasMonedas, ValoresMonedas, opcion))
            Pago = float(input(f"Ingresa la moneda para el pago").replace(",", "."))
            SumaPago += Pago
            if SumaPago >= Precios[opcion - 1]:
                continuar = False
        os.system("cls")
        print(MonedasIngresadas(SumaPago, Precios, ReservasMonedas, ValoresMonedas, opcion))
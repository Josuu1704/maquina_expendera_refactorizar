import os

productos = ["Agua", "Refrescos", "Zumos"]
precios = [0.50, 0.75, 0.95]
reserva_monedas = [20, 20, 20, 20, 20]
valores_monedas = [2, 1, 0.50, 0.20, 0.10, 0.05]


def menu(productos, precios):
    texto_menu = ""
    for i, nombre in enumerate(productos):
        texto_menu += f"{i + 1} - {nombre} = {precios[i]}\n"
    texto_menu += f"{len(productos) + 1} - Salir"
    return texto_menu


def ProductoElegido(opcion, productos, precios):
    if opcion in range(1, len(productos) + 1):
        return f"\nHas escogido {productos[opcion - 1]} \nTotal a pagar: {precios[opcion - 1]}"
    elif opcion == len(productos) + 1:
        return "Fin del Programa"


def MonedasIngresadas(suma_pago, precios, reservas_monedas, valores_monedas, opcion):
    precio = precios[opcion - 1]
    if suma_pago < precio:
        return f"Cantidad insuficiente, faltan {round(precio - suma_pago, 2)}"

    cambio = round(suma_pago - precio, 2)
    mensaje = f"Pago recibido: {suma_pago} \nCantidad devuelta: {cambio} \n"

    for i in range(len(reservas_monedas)):
        valor = valores_monedas[i]
        while cambio >= valor and reservas_monedas[i] > 0:
            cambio = round(cambio - valor, 2)
            reservas_monedas[i] -= 1

    if cambio > 0:
        return "No hay suficiente cambio disponible."

    return mensaje + "Pago completado"


opcion = 0
while opcion != len(productos) + 1:
    print(menu(productos, precios))
    opcion = int(input("Escoge una opcion: "))
    os.system("cls")

    if opcion == len(productos) + 1:
        print(ProductoElegido(opcion, productos, precios))
        break
    else:
        print(ProductoElegido(opcion, productos, precios))

        SumaPago = 0
        while SumaPago < precios[opcion - 1]:
            Pago = float(input("Ingresa la moneda para el pago: ").replace(",", "."))
            SumaPago += Pago
            print(MonedasIngresadas(SumaPago, precios, reserva_monedas, valores_monedas, opcion))

        os.system("cls")
        print("Transacción finalizada. Gracias por su compra!\n")

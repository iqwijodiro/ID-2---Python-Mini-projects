import random

amount = random.randint(0, 100) * 100 # Generamos un nro aleatorio en 0 - 100000 como saldo actual

options = {
    "1": "Recargar",
    "2": "Saldo actual",
    "3": "Envía saldo",
    "4": "Finalizar"
}

def menu() -> str:
    print('Tu menú: ')
    for key, value in options.items(): # mostramos opciones
        print(f"{key}. {value}")
    option_selected = input("Que opción desea seleccionar?: ") # Capturamos la opcion elegida
    return option_selected

def add():
    global amount
    added = int(input("Cuanto desea recargar?: "))
    amount += added # acumulamos el saldo añadido
    print(f"Su saldo es: ${amount}, luego de recargarle ${added}")

def show_amount():
    print(f"\nActualmente posee un saldo de ${amount}\n")

def send():
    global amount
    transfer_to = input("A que numero telefónico desea transferir: ")
    transfer_amount = int(input(f"Que cantidad desea transferir al nro [{transfer_to}]?: "))
    if transfer_amount <= amount:
        amount -= transfer_amount # descontamos el saldo transferido
        print(f"Se transfirió correctamente {transfer_amount} al usuario del nro [{transfer_to}]")
        print(f"Su saldo actual es de: {amount}")
    else:
        print("No posee saldo suficiente para transferir")

def main():
    option_selected = menu() # ejecutamos la funcion que corresponde a la opcion seleccionada
    while option_selected != "4":
        if option_selected == "1":
            add()
        elif option_selected == "2":
            show_amount()
        elif option_selected == "3":
            send()
        else:
            print("Seleccione una opción valida")
        option_selected = menu()


if __name__ == "__main__":
    main()
number_words = {0:"cero", 1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco", 6:"seis",
         7:"siete", 8:"ocho", 9:"nueve", 10:"diez", 11:"once", 12:"doce",
         13:"trece", 14:"catorce", 15:"quince", 16:"dieciséis", 17:"diecisiete",
         18:"dieciocho", 19:"diecinueve", 20:"veinte", 30:"treinta", 40:"cuarenta", 50:"cincuenta",
         60:"sesenta", 70:"setenta", 80:"ochenta", 90:"noventa", 100:"cien"}

#Recibe el nro indicado por el usuario
number = input("Ingrese un número entre 0 y 100 (español): ")

#Convierte el string recibido en un numero (int)
string_to_number = eval(number)

#Valida que cumpla condiciones
if string_to_number >=0 and string_to_number <=100:
    #Verifica si el valor ingresado esta disponible en el array de numeros en letras
    if string_to_number in number_words:
        print(number_words.get(string_to_number))
    else:
    # Si el usuario ingresa un nro que no esta en el array se concatena el residuo y su decena
        residuo = string_to_number % 10 # obtiene el residuo de la division entre 10 para saber que nro compara en el array para asignar la unidad
        decena = int(string_to_number / 10) * 10 # convierte a entero el valor y compara con su imagen en el array
        print(number_words.get(decena) + " y " + number_words.get(residuo)) #concatena la decena y el residuo
else:
    print("Por favor el numero debe estar entre 0 y 100")
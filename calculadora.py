print ("Calculadora\n")

print("--------------------")
print("* Menú de opciones *")
print("--------------------")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

numero = int(input("Introduce la opción deseada:"))

if numero == 1:

    print("Elegiste suma \n")
    numero = int(input("Introduce el primer número:"))
    numero += int(input("Introduce el segundo número:"))
    print("El resultado de la suma es:", numero)

elif numero == 2:

    print("Elegiste resta \n")
    numero = int(input("Introduce el primer número:"))
    numero -= int(input("Introduce el segundo número:"))
    print("El resultado de la resta es:", numero)

elif numero == 3:

    print("Elegiste multiplicación \n")
    numero = int(input("Introduce el primer número:"))
    numero *= int(input("Introduce el segundo número:"))
    print("El resultado de la multiplicación es:", numero)

elif numero == 4:

    print("Elegiste división \n")
    numero= float(input("Introduce el primer número:"))
    numero1= float(input("Introduce el segundo número diferente de 0:   "))
    
    if numero1 == 0:
        print("Error al dividir entre 0")
    else:
        resultado= numero/numero1
        print("El resultado de la división es:", round(resultado, 2))

else:
    print("La opción elegida no existe, vuelve a intentar.")

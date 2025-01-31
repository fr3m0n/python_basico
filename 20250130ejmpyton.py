
texto = "bUeNos dÍAs"
print(texto.lower()) 
print(texto.capitalize()) 

'''
preguntar la edad al usuario

si tiene menos de 12 años eres un niño

si tienes menos de 18 años eres un adolescente

si tienes menos de 30 eres muy joven

si tienes menos de 40 eres joven pero menos

si tienes mas más tu puedes con todo

''''''
edad = int(input("Por favor indica tu edad"))

if 0 <= edad < 12:
    print("Eres un niño")
elif edad < 18:
     print("Eres un adolescente")
elif edad < 30:
     print("Eres muy joven")
elif edad < 40:
     print("Eres joven, pero menos")
 elif edad < 120:
     print("Eres joven, pero menos")    
else:
     print("No me lo creo")

'''

'''
preguntar la edad al usuario

si tiene menos de 0 o mas de 120 no me lo creo

si tienes menos de 18 aun no puedes votar, te faltan x años para hacerlo

si tienes 18 o mas puedes votar desde hace años

'''
'''
edad = int(input("Por favor indica tu edad "))

edad_sobrante = edad - 18 

if edad <= 0:
    print("No me lo creo")
elif edad > 120:
    print("No me lo creo") 
elif edad < 18:
    
    print(f"No puedes votar de faltan: {edad_faltante}")
else:
    
    print(f"No puedes votar desde: {edad_sobrante}")

'''
'''
pedir al usuario un numero
pedir otro numero
pedir que operacion matematica quiere hacer (las 7 posobilidaddes)
y si no es una de estas mostraremos un mensaje de error
suma , 
resta, 
multiu, 
divi, 
exponente, 
division entera,
modulo
y si divide por cero tambien
si no son numero le diremos que no se puede hacer

'''
primer_numero = input("Introducir el primer número: ")

segundo_numero = input("Introducir el segundo número: ")

operacion = input("Deseo hacer una : ")


if  primer_numero.alpha() == True:
    print("Introduzca un numero: ") 
elif segundo_numero.isnumeric() == True:
    print("Introduzca un numero: ") 
elif operacion == "suma":
    print(f"{float(primer_numero)} + {float(segundo_numero)} = operacion")
elif  operacion == "resta":
    print(f"{float(primer_numero)} - {float(segundo_numero)} = operacion")
elif operacion == "multiplicacion":
    print(f"{float(primer_numero)} * {float(segundo_numero)} = operacion")
elif operacion == "division":
    if segundo_numero == 0:
        print("no se puede hacer la division entre 0")
        else
        print(f"{int(primer_numero)} / {int(_numero)} = operacion")   
elif operacion == "exponente":
    print(f"{float(primer_numero)} ** {float(segundo_numero)} = operacion")
elif operacion == "division entera":
    if segundo_numero == 0:
        print("no se puede hacer la division entre 0")
        else
        print(f"{int(primer_numero)} / {int(_numero)} = operacion") 
else operacion == "modulo":
    if segundo_numero == 0:
        print("no se puede hacer la division entre 0")
        else
        print(f"{int(primer_numero)} % {int(_numero)} = operacion") 
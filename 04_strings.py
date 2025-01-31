nombre = "Freddy"
apellido = "Chau"
edad = 60
frase01 = "Mi nombre y apellido es :" + " "+ nombre + " " + apellido + " "+ "y mi edad es : " + str(edad)+ " "+ "años"
print(frase01)

frase = f"Mi nombre completo es : {nombre} {apellido} y mi edad es : {edad} años" # utilizando el formateo
print(frase)
'''
# Obtener datos del usuario
nombre = input ("Escribe tu nombre: ")

print(type(nobre)) #siempre sera str

apellido = input ("Escribe tu apellido: ")

edad = input ("Escribe tu edad: ")
'''

frase = "Esto es una frase un poco larga"

# Primer caracter del string
print("frase[0] ->", frase[0])

# Ultimo caracter del string
print("frase[-1] ->", frase[0-1])


# 6 primeros caracteres
print("frase[0:6] ->", frase[:6]) # ^[inicio : fin]

# 6 ultimos caracteres
print("frase[0:6] ->", frase[:-6])


# caracteres en posicion par
print("frase[0::2] ->", frase[::2])
print("frase[0::2] ->", frase[::-1]) # invertir la cadena

# Cuantos caracteres hay en el string
print"(len(frase) ", len(frase())


# Convertir el texto en Mayusculas
print(frase.upper())
frase = frase.upper()
print(frase)


# Convertir el texto en Minusculas
print(frase.lower())
frase = frase.lower()
print(frase)


# Invertir  Mayusculas y Minusculas
print(frase.swapcase())

# Contar caracteres
print("frase.count('Es')", frase.count("Es"))


# Encontrar caracteres
print("frase.find('a')", frase.find("a"))

# Verificar si el texto empieza por cierto caracter o grupo de caracteres
frase = "https://google.com"
print(frase.stratwith("htpps"))

frase = "https://google.com"
print(frase.endwith("htpps"))

# Verificar si el texto es convertible a numero
numero = "10"
print(int(numero))
print(numero.isnumeric())#solo numero

print(numero.isalpha())#solo texto

print(numero.isalnum())#aplfanumerico

#Cambiar caracteres
print(frase.repalce("a","i"))#aplfanumerico

palabras_en_frase = frase.split(" ")
print(len(palabras_en_frase))

# Mini Ejercicio








# Ej 1
print(f"Hola Mundo!")  

#Ej 2
Nombre =input("Cual es tu nombre") 
print(f"Hola {Nombre}")


#Ej 3
Nombre =input("Cual es tu Nombre?")
Apellido =input("Cual es tu Apellido?")
Edad =input("Cual es tu Edad?")
Vivienda = input("Donde Vivis?")


print(f"Hola Soy {Nombre} {Apellido}, tengo {Edad} y vivo en {Vivienda}")

#Ej 4

Radio=int(input("ingresa el radio del circulo"))
Area= (Radio * Radio)*3.14

print(f"su area es {Area}")


#Ej 5
Segundos =  int(input("escribi una cantidad de segundos"))
Horas = Segundos * 60
print(f"{Segundos} es igual a {Horas}")

#Ej 6   

Numero = int(input("ingresa un numero a multiplicar"))
        
for i in range (11):
    print(f"{Numero*i}")

#Ej7    
Numero1=int(input("escribi el primer numero"))
Numero2=int(input("escribi el segundo numero numero"))

print(f"la suma de {Numero1} y {Numero2} es {Numero1 + Numero2}")
print(f"la resta de {Numero1} y {Numero2} es {Numero1 - Numero2}")
print(f"la multiplicacion de {Numero1} y {Numero2} es {Numero1 * Numero2}")
print(f"la divison de {Numero1} y {Numero2} es {Numero1 / Numero2}")

#Ej 8

Altura=float(input("ingresa tu altura"))
Peso=float(input("ingresa tu peso"))

Masa= Peso / (Altura*Altura)

print(f"Tu IMC es de {Masa}")

#Ej 9

Celsius=float(input("Ingresa grados Celsius"))

Farenheit=(Celsius* 9/5)+ 32


print(f"El equivalente en farenheit es de {Farenheit}")



#Ej 10
Numero1=float(input("Ingresa el primer nuemero"))
Numero2=float(input("Ingresa el segundo numero"))
Numero3=float(input("Inresa el tercer numero"))


Promedio=(Numero1+Numero2+Numero3) / 3 


print(f"El promedio de los numeros ingresados es {Promedio}")
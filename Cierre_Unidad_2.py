#Ej 1

nombre = input("Ingresa tu nombre: ")

while not nombre.isalpha():
    print("Error, ingresar solametne letras")
    nombre = input("Ingresa tu nombre: ")

cantidad= input("Ingresa la cantidad de productos :")

while not cantidad.isdigit() and int(cantidad)<=0:
    print("Error, ingresa un numero entero mayor a 0")
    cantidad= input("Ingresa la cantidad de productos :")


cantidad = int(cantidad)
precio_con_descuento= 0
precio_sin_descuento= 0
total_sin_descuento= 0
total=0
descuento = .10
ahorro= 0

for i in range(1,cantidad +1):
    precio= input(f"Producto {i} : Precio: ")
    while not precio.isdigit():
        print("Error, ingresar un numero entero mayor a 0")
        precio= input(f"Producto {i} : Precio: ")

    precio= int(precio)

    descuento=input("Descuento S/N")
     
    while descuento.lower() not in ["s","n"]:
        print("Error, ingresar S o N")
        descuento= input("Descuento S/N: ")

    
    total += precio    

    if descuento.lower() == "s":
        precio_con_descuento+= precio* 0.9
    else:
        precio_sin_descuento +=precio
    
     
total_con_descuento= precio_sin_descuento + precio_con_descuento
promedio= total_con_descuento/ cantidad
#print(f"{total_descuento}")

print(f"Total compra sin descuentos {total}")
print(f"Total compra con descuentos: {total_con_descuento}")
print(f"Ahorro de compra {total - total_con_descuento}")
print(f"Promedio por producto {promedio:.2f}")




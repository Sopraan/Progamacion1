#Ej 1

# nombre = input("Ingresa tu nombre: ")

# while not nombre.isalpha():
#     print("Error, ingresar solametne letras")
#     nombre = input("Ingresa tu nombre: ")

# cantidad= input("Ingresa la cantidad de productos :")

# while not cantidad.isdigit() and int(cantidad)<=0:
#     print("Error, ingresa un numero entero mayor a 0")
#     cantidad= input("Ingresa la cantidad de productos :")


# cantidad = int(cantidad)
# precio_con_descuento= 0
# precio_sin_descuento= 0
# total_sin_descuento= 0
# total=0
# descuento = .10
# ahorro= 0

# for i in range(1,cantidad +1):
#     precio= input(f"Producto {i} : Precio: ")
#     while not precio.isdigit():
#         print("Error, ingresar un numero entero mayor a 0")
#         precio= input(f"Producto {i} : Precio: ")

#     precio= int(precio)

#     descuento=input("Descuento S/N")
     
#     while descuento.lower() not in ["s","n"]:
#         print("Error, ingresar S o N")
#         descuento= input("Descuento S/N: ")

    
#     total += precio    

#     if descuento.lower() == "s":
#         precio_con_descuento+= precio* 0.9
#     else:
#         precio_sin_descuento +=precio
    
     
# total_con_descuento= precio_sin_descuento + precio_con_descuento
# promedio= total_con_descuento/ cantidad


# print(f"Total compra sin descuentos {total}")
# print(f"Total compra con descuentos: {total_con_descuento}")
# print(f"Ahorro de compra {total - total_con_descuento}")
# print(f"Promedio por producto {promedio:.2f}")


#Ej 2
usuario="alumno"
clave="python123"
intentos = 0
inscripcion= "inscripto"
mensaje= "sos una maquina"
menu= 0
while intentos <3:
    nombre_de_usuario=input("ingresa tu nombre de usuario: ")
    password= input("ingresa tu contraseña: ")

    if  nombre_de_usuario != usuario and password != clave:
      
        print("Usuario o contraseña erroneo")

    


    elif nombre_de_usuario == usuario and password == clave:
        print("bienvenido")
        print("1. Estado  2. Cambiar Clave  3. Mensaje  4. Salir")
        break

    intentos +=1


if intentos == 3:
    print("cuenta bloqueada")
else:
    while menu != 4 :
       #arreglar confirmacion de int, con letras explota     
        menu=input("ingresa el numero de la opcion deseada")
        if not menu.isdigit() or 1 <= int(menu) <= 4:     
            print("ingresa un numero valido")   
            menu=int(menu)       

        if menu == 1:
             print(f"el estado del alumno es {inscripcion}")
             continue
        if menu == 2:
             clave = input("ingresar nueva clave")
             confimar_clave= False
             if len(clave) < 6:
                 print("ingresa una clave con al menos digitos")
             else:
                 
                 #aca nose que quiciste hacer, pero no valida nada
                 clave = input("ingresar nueva clave")
                 confirmar_clave = input("confirmar nueva clave")
                 if clave == confimar_clave:
                     clave= clave
                     print(f"{clave}")

                    #cuando supuestamente cambias la calve, algo del while se rompe y corre break automaticamentegit
                     continue
        if menu == 3:
             print(f"{mensaje}")
             continue
        else:   
             print("sesion cerrada")
             break
                
                
             


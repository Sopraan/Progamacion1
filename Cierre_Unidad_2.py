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

# usuario="alumno"
# clave="python123"
# intentos = 0
# inscripcion= "inscripto"
# mensaje= "sos una maquina"
# menu= 0
# while intentos <3:
#     nombre_de_usuario=input("ingresa tu nombre de usuario: ")
#     password= input("ingresa tu contraseña: ")

#     if  nombre_de_usuario != usuario and password != clave:
      
#         print("Usuario o contraseña erroneo")

#     elif nombre_de_usuario == usuario and password == clave:
#         print("bienvenido")
#         print("1. Estado  2. Cambiar Clave  3. Mensaje  4. Salir")
#         break

#     intentos +=1

# if intentos == 3:
#     print("cuenta bloqueada")
# else:
#     while menu != 4 :
#        #arreglar confirmacion de int, con letras explota     
#         menu=input("ingresa el numero de la opcion deseada")
#         if not menu.isdigit() or 1 <= int(menu) <= 4:     
#             print("ingresa un numero valido")   
#         menu=int(menu)           

#         if menu == 1:
#              print(f"el estado del alumno es {inscripcion}")
#              continue
        
#         if menu == 2:
#              clave = input("ingresar nueva clave")
             
#              if len(clave) < 6:
#                  print("ingresa una clave con al menos digitos")
             
#              confirmar_clave=input("Confirmar nueva clave")     
#                  #aca nose que quiciste hacer, pero no valida nada

#              if clave != confirmar_clave:
#                 print("Las claves no coinciden")
#              if clave == confirmar_clave:
#                  print("Clave Modificada")

#         if menu == 3:
#              print(f"{mensaje}")
#              continue
      
#         if menu == 4:
#             print("Sesion cerrada")
#             break        
             


# EJ 3

# lunes1= ""
# lunes2= ""
# lunes3= ""
# lunes4= ""
# martes1= ""
# martes2= ""
# martes3= ""

# menu=0
# nombre=input("Ingresa tu nombre ")

# while menu != 5:

#     print("1. Resevar turno  2. Cancelar turno  3. Ver Agenda del dia  4. Ver resumen general  5.  Cerrar Sistema ")


#     menu=input("ingresa el numero de la opcion deseada ")
#     if not menu.isdigit() or not (1 <= int(menu) <= 5):
#         print("ingresa un numero valido")
#         continue
#     else:
#         menu = int(menu)

# # RESERVA DE TURNO
#     if menu == 1:
#          dia = input("ingresa 1 para Lunes 2 para Martes ")

#          if not dia.isdigit():
#             print("Dia invalido")
#             continue

#          dia = int(dia)
#          nombre=input("ingresa el nombre del paciente ")
         
         
#          if dia == 1:
#             if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
#                print("Ese paciente ya tiene turno")
#                continue
            
#             if lunes1 == "": 
#               lunes1= nombre 
#               print("Turno agendado")
#             elif lunes2 == "": 
#               lunes2= nombre
#               print("Turno agendado")
#             elif lunes3 == "": 
#               lunes3= nombre
#               print("Turno agendado")
#             elif lunes4 == "": 
#               lunes4= nombre
#               print("Turno agendado")

#          if dia == 2:

#             if nombre == martes1 or nombre == martes2 or nombre == martes3:
#                 print("Ese paciente ya tiene turno")
#                 continue
#             if martes1 == "": 
#               martes1= nombre 
#               print("Turno agendado")
#             elif martes2 == "": 
#               martes2= nombre
#               print("Turno agendado")
#             elif martes3 == "": 
#               martes3= nombre
#               print("Turno agendado")


#         #CANCELACION TURNO 
#     if menu == 2:
#          dia = input("ingresa 1 para Lunes 2 para Martes ")

#          if not dia.isdigit():
#             print("Dia invalido")
#             continue

#          dia = int(dia)
#          nombre=input("ingresa el nombre del paciente ")
         
#          if dia == 1:
#             if lunes1 == nombre:
#                 lunes1 = ""
#                 print("turno cancelado")
#             elif lunes2 == nombre:
#                 lunes2 = ""
#                 print("turno cancelado")
#             elif lunes3 == nombre:
#                  lunes3 = ""
#                  print("turno cancelado")
#             elif lunes4 == nombre:
#                 lunes4 = ""
#                 print("turno cancelado")
#             else:
#                 print("No se encontró el turno")

#          if dia == 2:
#             if martes1 == nombre: 
#                 martes1= ""         
#                 print("turno cancelado")            
#             elif martes2 == nombre: 
#                 martes2= ""
#                 print("turno cancelado")
#             elif martes3 == nombre: 
#                 martes3= ""
#                 print("turno cancelado")

# # AGENDA DE TURNOS POR DIA

#     if menu == 3:
#         dia = input("ingresa 1 para Lunes 2 para Martes")

#         if not dia.isdigit():
#             print("Dia invalido")
#             continue

#         dia = int(dia)

#         if dia == 1:
#           if lunes1 == "":
#              print("Vacio")
#           elif lunes1 != "":
#              print(f"{lunes1}")

#           if lunes2 == "":
#              print("Vacio")
#           elif lunes2 != "":
#              print(f"{lunes2}")

#           if lunes3 == "":
#              print("Vacio")
#           elif lunes3 != "":
#              print(f"{lunes3}")

#           if lunes4 == "":
#              print("Vacio")
#           elif lunes4 != "":
#              print(f"{lunes4}")        

#         if dia == 2:
#           if martes1 == "":
#              print("Vacio")
#           elif martes1 != "":
#              print(f"{martes1}")

#           if martes2 == "":
#              print("Vacio")
#           elif martes2 != "":
#              print(f"{martes2}")

#           if martes3 == "":
#              print("Vacio")
#           elif martes3 != "":
#              print(f"{martes3}")

           

#     if menu == 4:    
#         print("Resumen General")
#         print("Turnos dia lunes \n ")
#         if lunes1 == "":
#              print("Vacio")
#         elif lunes1 != "":
#              print(f"{lunes1}")

#         if lunes2 == "":
#              print("Vacio")
#         elif lunes2 != "":
#              print(f"{lunes2}")

#         if lunes3 == "":
#              print("Vacio")
#         elif lunes3 != "":
#              print(f"{lunes3}")

#         if lunes4 == "":
#              print("Vacio")
#         elif lunes4 != "":
#              print(f"{lunes4}")  

#         print("Turnos dia martes \n")

#         if martes1 == "":
#              print("Vacio")
#         elif martes1 != "":
#              print(f"{martes1}")

#         if martes2 == "":
#              print("Vacio")
#         elif martes2 != "":
#              print(f"{martes2}")

#         if martes3 == "":
#              print("Vacio")
#         elif martes3 != "":
#              print(f"{martes3}")

               
#     if menu == 5:    
#         print("Sesion Cerrada")    
#         break



# Ej 4

energia= 100
tiempo=12
cerraduras_abiertas=0
alarma= False
codigo_parcial=""

# Inut dentro de while

nombre_del_agente=input("Ingres el nombre del agente")
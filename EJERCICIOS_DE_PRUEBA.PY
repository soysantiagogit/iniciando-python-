# def notas_escolares(nota):
    
#     if nota < 0 or nota > 10:
#         return "nota no valida"
    
#     elif nota < 5:
#         return "suspenso"
    
#     elif nota < 7:
#         return "aprobado"
    
#     elif nota < 9:
#         return "notable"            
    
#     else:
#         return "sobresaliente"
    
# nota_de_usuario = float(input("cual fue tu nota: "))
# resultado = notas_escolares(nota_de_usuario)
# print(resultado)        
               
#creando una función

# def precio_fianl (precio,tiene_tarjeta):
    
#     if precio <= 0:
#         return "precio no valido" 
    
#     if tiene_tarjeta:
#         if precio >= 100:
#             descuento = 0.20
#         else:
#             descuento = 0.10     
               
#     else:
#         if precio >= 100:
#             descuento = 0.10
#         else:
#             descuento = 0.0
    
#     return precio * (1 - descuento) 
         

# print(precio_fianl(120, True))
# print(precio_fianl(80, True))
# print(precio_fianl(120, False))
# print(precio_fianl(50, False))
    
    #programa para recomendación de sueldo mensual segun los gastos mensuales

# gasto_arriendo = float(input("cuanto pagas de arriendo: "))
# gasto_servicios = float(input("cuanto pagas de servicios: "))
# gastos_comida = float(input("cuanto gastas en comida: "))


# suma_gastos = gasto_arriendo + gasto_servicios + gastos_comida


# sueldo_requerido = suma_gastos + 200

# print("los gastos son: \n arriendo \n servicios \n comida")
# print(f"el total de los gastos es: {suma_gastos}USD")
# print(f"el sueldo que deberias ganar es de: {sueldo_requerido}USD ")

#creando una función para recomendar un sueldo 

#función para calcular gastos mensuales de la persona  
 
# def gastos_mensuales():
    
#     #pidiendo al usuario los gastos
     
#     gasto_arriendo = int(input("cuanto pagas de arriendo: "))
#     gasto_servicio = int(input("cuanto gastas en los servicios: "))
#     gasto_comida = int(input("cuanto gastas en comida: "))
    
#     #retornando la suma de sus gastos
     
#     return gasto_arriendo + gasto_servicio + gasto_comida

# # creando una función con el sueldo ideal 

# def sueldo_ideal(gastos):
    
#     return gastos + 200


# #variable que guarde la función anterior 

# gastos = gastos_mensuales()

# #imprimiendo el resultado 
# print("-----------------")
# print("en total gastas: ",gastos,"USD")
# print("-----------------")
# print("tu sueldo ideal seria: ", sueldo_ideal(gastos),"USD para que alcances ahorrar por lo menos 100 USD")

#creando funcion para la tarifa de un cine 

# def calcular_precio():
    
    
#     edad = int(input("ingresa la edad: "))
#     precio = float(input("ingresa el precio: "))
#     descuento = float(input("ingresa el descueto: "))
    
    
#     if precio < 8:
#         return "el precio base es de 8 USD"
    
#     elif edad < 18:
#         return f"tienes un descueto del 25% te queda en {precio - (precio * descuento / 100)} USD"
    
#     elif edad < 66:
#         return f"tienes un descuento del 30% te queda en {precio - (precio * descuento / 100)} USD"
    

# print(calcular_precio())

#haciendo el mismo problema pero con parametro 

# def calcular_precio(edad):
    
#     precio_base = 8 
    
#     if edad < 18:
#         return f"el 25% de descueto, precio total : {precio_base * 0.75} USD" # es el 25% de descuento 
    
#     elif edad >= 65:
#         return f"el 30% de descuento, precio total : {precio_base * 0.70} USD" # 30% de descuento 
    
#     else:
#         return f"no tienes descuetos, precio total : {precio_base} USD"
    
# print(calcular_precio(15)) #menor de edad 
# print(calcular_precio(30)) #adulto 
# print(calcular_precio(70)) #adulto mayor 

#creando ejercició mas largo 

#funcion de compras 

# def calcular_total():
    
#     #pidiendo precio y cantidad
    
#     precio = float(input("ingrese el precio: "))
#     cantidad = float(input("ingrese la cantidad: "))
    
#     #calculando el total de precio y cantidad
    
#     sub_total = precio * cantidad 
    
#     #en caso de no poner precio 
    
#     if precio <= 0 or cantidad <= 0:
#         print("precio y cantidad deben ser mayor a cero ")
#         return None
    
#     #el descuento 
    
#     elif sub_total >= 200:
        
#         return f"tienes el 20% de descueto, el total es: {sub_total * 0.80}"  #20% de descuento
    
#     elif sub_total  >= 100:
        
#         return f"tienes el 10% de descueto, el total es: {sub_total * 0.90}"  #10% de descuento 
    
        
# #preguntando si quiere otra compra 

# while True:
    
#     total = calcular_total()
    
#     if total is not None:
        
#         print(total)
        
#     usuario = input("¿ deseas otra compra? (s/n): ")
    
#     if usuario != "s":
#         print("gracias por su compra")
        
#         break
 
    
#Nivel 1 lista de productos 

# def calcular_total():
    
#     productos = []
    
#     while True:
        
#         precio = int(input("ingrese precio: "))
        
#         if precio == 0:
            
#             print("hasta aqui llego")
            
#             break
        
#         productos.append(precio)
    
#     total = sum(productos)
    
#     return total

# print("total: ", calcular_total())
                

#nivel 2 menú simple 
    
# funcion para agregar un numero 
# def agregar_numero(lista):
    
#     numero = int(input("ingresa un numero: "))
    
#     lista.append(numero)
        
        
        
# def ver_total(lista):
    
#     total = sum(lista)
#     print("total: ", total)
    
    

# def menu():
    
#     print("\n1. agregar numero")
#     print("2. ver total")
#     print("3. salir")
        

# numeros = []


# while True:
    
#     menu()
#     opcion = input("elija una opcion: ")
    
#     if opcion == "1":
        
#         agregar_numero(numeros)
        
#     elif opcion == "2":
        
#         ver_total(numeros)
        
#     elif opcion == "3":
        
#         print("adios")
        
#         break
    
#     else:
        
#         print("opcion incorrecta ")

#nivel 3 mini sistema de ventas (con descuentos)

# función para agregar productos
def agregar_productos(lista):
    
    precio = float(input("ingrese el precio: "))
    lista.append(precio)
    

#funcion para sumar los productos agregados
def ver_subtotal(lista):
    
    total = sum(lista)
    print("subtotal:",total)
        

#función para hacer cuenta de los descuentos 
def calcular_total(lista):
    
    sub_total = sum(lista)
    
    if sub_total >= 200:
        
        total = sub_total * 0.80    #20% de descuento
        print("descuento 20%")
        print("total: ", round(total,2))
        
    elif sub_total >= 100:
        
        total = sub_total * 0.90    #10% de descuento 
        print("descuento 10%")
        print("total: ", round(total,2))
        
    
    else:
        
        print("sin descuento")
        print("total: ", round(total,2))
        

#creando menu 
def menu():
    
    print("\n1. agregar productos")
    print("2. ver subtotal")
    print("3. ver total con descuentos")
    print("4. salir")
    

#lista vacia para almacenar el total
precios = []


# bucle while para ejecutar cada opción del menú    
while True:
    
    menu()
    
    #opción 1.
    opcion = input("elija una opción: ")
    
    if opcion == "1":
        
        agregar_productos(precios)
        
    
    #opcion 2
    elif opcion == "2":
        
        ver_subtotal(precios)
        
    
    #opcion 3
    elif opcion == "3":
        
        calcular_total(precios)
        
    
    #opción 4
    elif opcion == "4":
        
        print("adios")
        break
    
    
    #en caso de poner otro caracter 
    else:
        print("opcion incorrecta")
        

    



    
    
    
    
    







    
  
     


    
      

       


    

     
    



    

    

    

        
    
    

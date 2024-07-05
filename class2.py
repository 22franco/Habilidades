# Clase para representar una tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []  # Lista que almacena cada producto de la tienda
    
    # Agrega un producto al inventario
    def agregar_producto(self, codigo):
        self.inventario.append(codigo)  

    # metodo de algoritmo de busqueda lineal
    def buscar_producto(self, codigo):
        for producto in self.inventario:
            if producto == codigo:
                return True
        return False


# inicia la clase Majeador_de_tiendas
class administrar_tiendas:
    def __init__(self):
        self.tiendas = []  # Lista para guardar las tiendas
    
    # Método para agregar una nueva tienda a la lista
    def agregar_tienda(self, tienda):
        self.tiendas.append(tienda)  
    
    # Método para buscar una tienda por nombre en la lista de tiendas
    def seleccionar_tienda(self, nombre):
        for tienda in self.tiendas:
            if tienda.nombre == nombre:
                return tienda 
        return None  


    # Comienza el menú interactivo
    
    def menu_interactivo(self):
        # Inicio de un bucle while que se detendra al oprimir la opcion 4
         while True:
            print("\n Bienvenido al Menú de gestión de Tiendas Electronicas")
            print("\n Por favor, seleccione una opción:")
            print("1. Agregar nueva tienda")
            print("2. Agregar producto a tienda")
            print("3. Buscar producto en tienda")
            print("4. Salir")
            
            opcion = input("Ingrese su opción: ")
            
            # Condición al seleccionar la opción 1. Agregar tienda
            if opcion == "1":
                nombre_tienda = input("Ingrese el nombre de la nueva tienda: ")
                nueva_tienda = Tienda(nombre_tienda)
                self.agregar_tienda(nueva_tienda)
                print(f"Tienda {nombre_tienda} agregada correctamente.")
                
            # Condición al seleccionar la opción 2. Agregar producto a tienda
            elif opcion == "2":
                nombre_tienda = input("Ingrese el nombre de la tienda: ")
                tienda = self.seleccionar_tienda(nombre_tienda)
                if tienda:
                    codigo_producto = input("Ingrese el código del producto: ")
                    tienda.agregar_producto(codigo_producto)
                    print(f"Producto {codigo_producto} agregado a la tienda {nombre_tienda}.")
                else:
                    print("La tienda no existe.")
           
            # Condición al seleccionar la opción 3. Buscar Producto en Tienda
            elif opcion == "3":
                nombre_tienda = input("Ingrese el nombre de la tienda: ")
                tienda = self.seleccionar_tienda(nombre_tienda)
                if tienda:
                    codigo_producto = input("Ingrese el código del producto que desea buscar: ")
                    if tienda.buscar_producto(codigo_producto):
                        print(f"El producto {codigo_producto} está disponible en la tienda {nombre_tienda}.")
                    else:
                        print(f"No se encontró el producto {codigo_producto} en la tienda {nombre_tienda}.")
                else:
                    print("La tienda no existe.")
                    
            # Condición que rompe el bucle while al seleccionar la opción 4. Salir
            elif opcion == "4":
                print("Gracias por su atencion, saliendo del menu de la.")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

# Crear instancia del manejador de tiendas
manejador_tiendas = administrar_tiendas()

# imprimir el menú interactivo
print(manejador_tiendas.menu_interactivo())
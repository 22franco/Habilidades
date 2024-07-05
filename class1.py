# inicio la clase de los clientes
class Cliente:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial  # Inicio el saldo del cliente
        

    #  El método depositar permite aumentar el saldo de un cliente al realizar los depositos
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False
    
    
    # Reduce el saldo del cliente al realizar una extraccion valida
    def extraer(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    # Devuelve el saldo actual del cliente
    def obtener_saldo(self):  
        return self.saldo

    # Obtiene el nombre del cliente actual(self.nombre),eliminando espacios y devolviendolo a minúsculas
    def comparar_nombre(self, nombre):
        return self.nombre.strip().lower() == nombre.strip().lower()



# Inicio la clase del banco
class Banco:
    def __init__(self):
        self.clientes = []  # Lista para guardar los clientes del banco

    # Agrego un cliente nuevo a la lista de clientes
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Calcula la cantidad total de dinero depositado en el banco
    def calcular_total_depositado(self):
        total = sum(cliente.obtener_saldo() for cliente in self.clientes)
        return total


   # Menu de consultas
    
    def menu(self, operaciones):
        for operacion in operaciones:
            print("\nSe encuentra en el Menu de consultas del Banco ILBA") 
            print("\nPor favor, seleccione la opción que desea utilizar")
            print("Clientes activos: agustin, carlos, tomas")
            print("1. Depósito")
            print("2. Extracción")
            print("3. Dinero total depositado")
            print("4. Salir")
            
            opcion = operacion[0]
            print(f"Seleccionaste la opción: {opcion}")

            # Condicion al aceptar la opcion 1. Deposito
            if opcion == 1:
                nombre_cliente = operacion[1]
                cliente = self.buscar_cliente(nombre_cliente)
                if cliente:
                    monto = operacion[2]
                    if cliente.depositar(monto):
                        print(f"Se depositaron {monto} a la cuenta de {cliente.nombre}.")
                    else:
                        print("Monto no válido para depósito.")
                else:
                    print("Cliente no encontrado.")
                    
            # Condicion al seleccionar opcion 2. Extraccion
            elif opcion == 2:
                nombre_cliente = operacion[1]
                cliente = self.buscar_cliente(nombre_cliente)
                if cliente:
                    monto = operacion[2]
                    if cliente.extraer(monto):
                        print(f"Se extrajeron {monto} de la cuenta de {cliente.nombre}.")
                    else:
                        print("Monto no válido o saldo insuficiente.")
                else:
                    print("Cliente no encontrado.")
                    
            # Condicion al seleccionar opcion 3. Dinero total depositado
            elif opcion == 3:
                total = self.calcular_total_depositado()
                print(f"La cantidad total de dinero depositado en el banco es: {total}")
                
            # Se rompe el bucle while al oprimir la opcion 4.Salir
            elif opcion == 4:
                print("Saliendo del menú.")
                break

            else:
                print("Opción no válida, por favor intente de nuevo.")

    def buscar_cliente(self, nombre):
        # Busca un cliente por nombre en la lista de clientes
        for cliente in self.clientes:
            if cliente.comparar_nombre(nombre):
                return cliente
        return None



# instancia del banco
mi_banco = Banco()

# instancia de los clientes 
cliente1 = Cliente(nombre="agustin")
cliente2 = Cliente(nombre="carlos")
cliente3 = Cliente(nombre="tomas")
mi_banco.agregar_cliente(cliente1)
mi_banco.agregar_cliente(cliente2)
mi_banco.agregar_cliente(cliente3)


# Asignar el nombre de los usuarios 
operaciones = [
    (1, "agustin", 1000),  
    (1, "carlos", 500),    
    (2, "agustin", 300),   
    (3, None, None),       
    (4, None, None)        
]

# imprimir el menu del banco con las operaciones 
print(mi_banco.menu(operaciones))
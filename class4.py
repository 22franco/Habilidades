# Inicio la clase 'contacto', asigno las variables y el nodo de la lista enlazada
class Contacto:
    def __init__(self, nombre, telefono, Email):
        self.nombre = nombre
        self.telefono = telefono
        self.Email = Email
        self.siguiente = None

# Inicio la clase 'lista_de_contactos'
class lista_de_contactos:
    def __init__(self):
        self.cabeza = None  # estructura para almacenar los contactos enlazados

    # Función para agregar contactos
    def agregar_contacto(self, nombre, telefono, Email):
        nuevo_contacto = Contacto(nombre, telefono, Email)
        if self.cabeza is None:
            self.cabeza = nuevo_contacto  # Agrega un nuevo contacto
        else:
            inicio = self.cabeza  # comienza de nuevo en la estructura de contactos

            # Recorre la estructura de contactos hasta el último contacto
            while inicio.siguiente:
                inicio = inicio.siguiente
            inicio.siguiente = nuevo_contacto

        # Imprime el registro con éxito
        print(f"Contacto {nombre} registrado con éxito.")

    # Función para eliminar contactos
    def eliminar_contacto(self, nombre):
        inicio = self.cabeza
        anterior = None

        while inicio:
            # Compara el nombre del contacto actual (inicio.nombre) con el nombre buscado (nombre)
            if inicio.nombre == nombre:
                # condicion si no hay contacto anterior en la lista
                if anterior:
                    anterior.siguiente = inicio.siguiente
                # condicion si hay contacto anterior en la lista
                else:
                    self.cabeza = inicio.siguiente
                print(f"Contacto {nombre} eliminado con éxito.")
                return
            anterior = inicio
            inicio = inicio.siguiente  # Enlaza el contacto anterior con el siguiente del actual

        print(f"El contacto: {nombre} no se ha encontrado. Por favor, inténtelo de nuevo.")

    # Función para mostrar contactos
    def mostrar_contactos(self):
        inicio = self.cabeza

        if inicio is None:
            print("No se encontraron contactos registrados.")
        else:
            print("Lista de contactos:")
            while inicio:
                print(f"Nombre: {inicio.nombre}, Teléfono: {inicio.telefono}, Email: {inicio.Email}")
                inicio = inicio.siguiente

    # Método para buscar un contacto por su nombre
    def buscar_contacto(self, nombre):
        inicio = self.cabeza
        while inicio:
            if inicio.nombre == nombre:
                return inicio
            inicio = inicio.siguiente
        return None

    # Método para cargar los datos de ejemplo de contacto
    def datos_contacto(self):
        self.agregar_contacto("Franco", "+54911885521", "francoalburquerque@gmail.com")
        self.agregar_contacto("Sofia", "+54911551238", "sofia2024@gmail.com")
        self.agregar_contacto("Tomas Perez", "+5491156652849", "tomasperez@gmail.com")
        self.agregar_contacto("Joaquin", "+545215238", "joaquin@gmail.com")
        self.agregar_contacto("Santiago", "+5491155466", "santiago@gmail.com")

# Función principal 'main'
def main():
    # Crea una nueva instancia de lista_de_contactos
    lista_contactos = lista_de_contactos()

    # Carga los datos de contacto usando el método datos_contacto
    lista_contactos.datos_contacto()

    # Muestra todos los contactos almacenados
    print("\nMostrando todos los contactos:")
    lista_contactos.mostrar_contactos()

    # Busca un contacto específico por su nombre
    print("\nBuscando un contacto por nombre:")
    contacto_buscar = lista_contactos.buscar_contacto("Tomas Perez")  # Nombre de ejemplo
    if contacto_buscar:
        print(f"Contacto encontrado: {contacto_buscar.nombre}, {contacto_buscar.telefono}, {contacto_buscar.Email}")
    else:
        print("Contacto no encontrado.")

    # Elimina un contacto por su nombre
    print("\nEliminando un contacto:")
    lista_contactos.eliminar_contacto("Sofia")  # Nombre de ejemplo

    # Muestra los contactos actualizados después de la eliminación
    lista_contactos.mostrar_contactos()

if __name__ == "__main__":
    main()
class 1:
# Descripción:

Este proyecto implementa un sistema bancario simple en Python utilizando programación orientada a objetos. Permite gestionar clientes, realizar depósitos y extracciones, calcular el dinero total depositado.

# Funcionalidades Principales:

- Lista las principales funcionalidades que el sistema ofrece, como:
- Gestión de clientes (crear, agregar, buscar).
- Realización de depósitos y extracciones.
- Cálculo del dinero total depositado en el banco.
- Menú interactivo para realizar operaciones.

# Detalles de Implementación:

- **Clase Cliente**: Maneja la información de cada cliente y sus operaciones financieras.

- **Clase Banco**: Gestiona una lista de clientes y proporciona funcionalidades como depósitos,extracciones y consultas de saldo.

- **Menú de Consultas**: Interfaz interactiva que permite a los usuarios realizar diferentes operaciones bancarias.

# Habilidades Técnicas Demostradas:

- Desarrollo en Python utilizando programación orientada a objetos:
Implementación de clases como Cliente y Banco para encapsular datos y operaciones bancarias.
Uso de atributos y métodos para gestionar clientes, depósitos, extracciones y cálculo de dinero total depositado.




class 2: 

# Descripción:

Este proyecto implementa un sistema de gestión de tiendas electrónicas mediante clases en Python. Permite agregar nuevas tiendas, gestionar su inventario de productos y realizar búsquedas de productos específicos dentro de cada tienda.


# Funcionalidades principales:

- Permite crear una nueva tienda y agregarla a la lista de tiendas disponibles.

- Permite añadir un producto específico al inventario de una tienda existente.

- Realiza una búsqueda de un producto por su código dentro de una tienda seleccionada.

- Proporciona un menú interactivo donde el usuario puede seleccionar entre las diferentes opciones disponibles para gestionar las tiendas electrónicas.


# Detalles de implementación:

**Clase Tienda**:
 Representa cada tienda con un nombre y un inventario implementado como una lista.
 Métodos:
 agregar_producto(codigo): Añade un producto al inventario de la tienda.
 buscar_producto(codigo): Realiza una búsqueda lineal para verificar si un producto está en el inventario.

**Clase administrar_tiendas**:
 Gestiona una lista de tiendas disponibles.
 Métodos:
 agregar_tienda(tienda): Agrega una nueva instancia de Tienda a la lista de tiendas.
 seleccionar_tienda(nombre): Busca y devuelve una tienda específica por su nombre.
 menu_interactivo(): Presenta un menú interactivo para que el usuario seleccione las acciones a realizar sobre las tiendas y sus productos.


# Habilidades demostradas:

- Desarrollo en Python utilizando clases y métodos para la implementación de objetos:
Manejo de estructuras de datos como listas para mantener inventarios y gestionar listas de objetos.
Implementación de métodos para agregar productos a tiendas y buscar productos en un inventario.




class 3: 

# Descripción:

Este script en Python ordena una lista de países junto con su población en dos maneras diferentes: alfabéticamente por nombre de país y de mayor a menor por población. Utiliza el algoritmo de ordenamiento "bubble sort" para ambos casos.


# Funcionalidades principales:

- Orden Alfabético de Países:
Ordena los países en orden alfabético utilizando el método "bubble sort" basado en sus nombres.
Imprime los países junto con su población después de ordenarlos alfabéticamente.

- Orden por Población (de Mayor a Menor):
Ordena los países en función de su población de mayor a menor utilizando "bubble sort".
Imprime los países junto con su población ordenados por población de mayor a menor.


# Detalles de implementación:

- Listas Utilizadas:
paises: Contiene los nombres de los países.
problacion: Contiene la población correspondiente a cada país en la misma posición que en la lista paises.

- Ordenamiento Alfabético:
Utiliza un doble bucle "bubble sort" para comparar y intercambiar los elementos según el orden alfabético de los nombres de los países.

- Ordenamiento por Población:
Aplica otro bucle "bubble sort" para ordenar los países según su población de mayor a menor.


# Habilidades demostradas:

- Implementación de algoritmos de ordenamiento "bubble sort" para diferentes criterios:
 Uso de estructuras de datos como listas para almacenar y ordenar datos relacionados, como países y poblaciones.
 Manipulación eficiente de listas y bucles en Python para realizar operaciones de ordenamiento de manera efectiva.




class 4:

# Descripción:

- El script define dos clases principales: Contacto y lista_de_contactos, que permiten la creación, gestión, búsqueda y eliminación de contactos. Utiliza una lista enlazada para mantener los contactos de manera eficiente.

# Funcionalidades principales:

**Clase Contacto**:
 Cada contacto tiene atributos como nombre, telefono, Email y un enlace siguiente para apuntar al siguiente contacto en la lista.

**Clase lista_de_contactos**:
 Agregar Contacto (agregar_contacto): Permite agregar un nuevo contacto al final de la lista enlazada.
 Eliminar Contacto (eliminar_contacto): Elimina un contacto específico por su nombre de la lista enlazada.
 Mostrar Contactos (mostrar_contactos): Imprime todos los contactos almacenados en la lista enlazada.
 Buscar Contacto (buscar_contacto): Busca un contacto por su nombre y devuelve el contacto si se encuentra.
 Datos de Contacto de Ejemplo (datos_contacto): Carga datos de contacto predefinidos utilizando el método agregar_contacto.

Función Principal (main):
 Crea una instancia de lista_de_contactos.
 Carga datos de ejemplo usando datos_contacto.
 Muestra todos los contactos almacenados.
 Busca un contacto específico por su nombre.
 Elimina un contacto por su nombre y muestra los contactos actualizados después de la eliminación.

# Detalles de implementación:

- Estructura de Datos: Utiliza una lista enlazada donde cada nodo (Contacto) contiene los datos de un contacto y un enlace al siguiente nodo.

- Métodos de Manipulación: Implementa métodos para agregar, eliminar, mostrar y buscar contactos.

- Uso de Condicionales y Bucles: Emplea condicionales para manejar casos como la inserción o eliminación de contactos, y bucles para recorrer la lista enlazada.

# Habilidades demostradas:

- Programación Orientada a Objetos:
 Utilización de clases (Contacto y lista_de_contactos) para encapsular datos y operaciones relacionadas con la gestión de contactos.
 Implementación de una lista enlazada para almacenar y gestionar dinámicamente una colección de contactos.
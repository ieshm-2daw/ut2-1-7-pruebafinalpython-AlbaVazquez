"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Alba Vázquez Guillén_______________________________________
Fecha: 4 de noviembre de 2025______________________________________

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, codigo, nombre, contacto):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f"{self.codigo, self.nombre, self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def __str__(self):
        return f"{self.codigo} {self.nombre} - {self.precio} € ({self.stock} uds.) | Proveedor: {self.proveedor} {self.proveedor['contacto']}"
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        lista_productos = self.productos = []
        lista_proveedores = []
        
        try:
            with open ('inventario.json', 'r') as f: 
                datos = json.load(f)
                
            for d in datos:
                producto = Producto(d['codigo'], d['nombre'], d['precio'], d['stock'], d['proveedor'])
                lista_productos.append(producto)
                
                proveedor = Proveedor(d['proveedor']['codigo'], d['proveedor']['nombre'], d['proveedor']['contacto'])
                
                # for p in d['proveedor'].items():
                #     proveedor = Proveedor(p)
                    
                if proveedor not in lista_proveedores:
                    lista_proveedores.append(proveedor)
                    
        except FileExistsError:
            lista_productos = []
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        pass

    def anadir_producto(self, producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                print("Ese producto ya está añadido.")
                return
        self.productos.append(producto)
        print("Producto añadido.")
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo

    def mostrar(self):
        for p in self.productos:
            print (f"{p}\n")
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados

    def buscar(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        p = self.buscar(codigo)
        
        if p is None:
            print("No existe un producto con ese código.")
        else:
            nombre = input("Nuevo nombre: ")
            precio = input("Nuevo precio: ")
            stock = input("Nuevo stock: ")
            
            p.nombre = nombre
            p.precio = precio
            p.stock = stock
            
            print("Producto modificado.")
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos

    def eliminar(self, codigo):
        p = self.buscar(codigo)
        
        if p is None:
            print("No hay un producto con ese código.")
        else:
            self.productos.remove(p)
            print("Procuto borrado")
        
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista


    def valor_total(self):
        valor = 0
        for p in self.productos:
            valor += (p.precio * p.stock)
        return valor
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock

    def mostrar_por_proveedor(self, nombre_proveedor): #POR CÓDIGO!!! 
        productos = ""
        encontrado = False
        for p in self.productos:
            if p.proveedor['codigo'] == nombre_proveedor:
                productos += f"{p}\n"
                encontrado = True
        if encontrado:
            return productos
        else:
            return "El proveedor no existe."
        
    """
    Muestra todos los productos de un proveedor determinado.
    Si no existen productos de ese proveedor, mostrar un mensaje.
    """
    # TODO: filtrar y mostrar los productos de un proveedor concreto


# ======================================================
# Funcións principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    inventario = Inventario('inventario.json')
    proveedor1 = Proveedor('PR05', 'Alguno', 'alguno@dominiochuli.com')
    producto1 = Producto("P006", "Ratón inalámbrico", 13.5, 10, proveedor1)
    
    inventario.cargar()
    

    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        # TODO: implementar las acciones correspondientes a cada opción del menú
        if opcion == '1':
            producto = input("Producto a añadir: ")
            inventario.anadir_producto(producto)
        
        elif opcion == '2':
            inventario.mostrar()
        
        elif opcion == '3':
            codigo = input("Código del producto a buscar: ")
            print(inventario.buscar(codigo))
        
        elif opcion == '4':
            codigo = input("Código del producto a modificar: ")
            inventario.modificar(codigo)
        
        elif opcion == '5':
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar(codigo)
        
        elif opcion == '6':
            print(inventario.valor_total() + "€")
        
        elif opcion == '7':
            codigo = input("Código del proveedor a buscar: ")
            print(inventario.mostrar_por_proveedor(codigo))
        
        elif opcion == '8':
            break

if __name__ == "__main__":
    main()

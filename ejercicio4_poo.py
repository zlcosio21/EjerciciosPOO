#Moral de Perro S.A. desea crear un comercio electrónico, pero no cuentan con el software para lograrlo, ayúdelos creando: una clase Producto y una clase CarritoDeCompras , con las siguientes especificaciones: a. La clase Producto debe tener dos atributos: nombre , y precio                     b. La clase Producto debe tener un método que permita modificar el nombre del producto.                    c. La clase CarritoDeCompras debe tener un atributo llamado productos que será una lista de elementos en el carrito.  d. La clase CarritoDeCompras debe tener los siguientes métodos: agregar_item(self, producto) - un método que permita agregar un producto al carrito si éste aún no está en la lista. eliminar_item(self, producto) - un método que permita eliminar un producto del carrito si éste está en la lista. Si el producto no está en la lista, el método debe imprimir un mensaje de error. obtener_items(self) - un método que devuelve la lista de productos en el carrito. obtener_total(self) - un método que calcula y devuelve el costo total de todos los productos en el carrito.     NOTA: Los elementos en la lista del carrito de compras deben ser productos, es decir, objetos creados con la clase Product.


class Producto:
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

  def modificar_nombre(self, nuevo_nombre):
    self.nombre = nuevo_nombre


class CarritoDeCompras:
  def __init__(self):
    self.productos = []
  
  def agregar_item(self, producto_nuevo):
    if producto_nuevo not in self.productos:
      self.productos.append(producto_nuevo)
      print(f"Se ha agregado el producto {producto_nuevo.nombre}, en el carrito de compras.\n")
    else:
      print("El producto ya se encuentra en el carrito de compras")
  def eliminar_item(self, producto):
    if producto in self.productos:
      self.productos.remove(producto)
      print(f"Se ha eliminado el producto {producto.nombre} del carrito de compras.\n")
    else:
      print("El producto no se encuentra en el carrito de compras.\n")
      
  def obtener_items(self):
    print("Los productos que hay en el carrito son:\n")
    for producto in self.productos:
      print(f"{producto.nombre}.")

  def obtener_total(self):
    total = 0
    for producto in self.productos:
      total += producto.precio
    print(f"\nEl total de la comopra es ${total}.")


producto1 = Producto("Nave espacial", 2500)
producto2 = Producto("Revolver", 500)
producto3 = Producto ("Nevera", 250)
producto4 = Producto("Desfibrilador", 500)
producto5 = Producto ("Celulares", 100)

carrito = CarritoDeCompras()
carrito.agregar_item(producto1)
carrito.agregar_item(producto2)
carrito.agregar_item(producto3)
carrito.agregar_item(producto4)
carrito.eliminar_item(producto4)
carrito.eliminar_item(producto5)
carrito.obtener_items()
carrito.obtener_total()
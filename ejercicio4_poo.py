# Moral de Perro S.A. desea crear un comercio electrónico, pero no cuentan con el software para lograrlo, ayúdelos creando: una clase Producto y una clase CarritoDeCompras , con las siguientes especificaciones: 
# a. La clase Producto debe tener dos atributos: nombre , y precio                     
# b. La clase Producto debe tener un método que permita modificar el nombre del producto.
# c. La clase CarritoDeCompras debe tener un atributo llamado productos que será una lista de elementos en el carrito
# d. La clase CarritoDeCompras debe tener los siguientes métodos: agregar_item(self, producto) - un método que permita agregar un producto al carrito si éste aún no está en la lista. eliminar_item(self, producto) - un método que permita eliminar un producto del carrito si éste está en la lista. Si el producto no está en la lista, el método debe imprimir un mensaje de error. obtener_items(self) - un método que devuelve la lista de productos en el carrito. obtener_total(self) - un método que calcula y devuelve el costo total de todos los productos en el carrito.     
# NOTA: Los elementos en la lista del carrito de compras deben ser productos, es decir, objetos creados con la clase Producto.""""

class Producto:
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

class CarritoDeCompras:
  def __init__(self):
    self.productos = []

  def agregar_item(self, producto):
    if producto not in self.productos:
      self.productos.append(producto)
      return f"Se ha agregado el producto {producto.nombre} al carrito"
      
    return f"El producto {producto.nombre} ya se encuentra en el carrito"

  def eliminar_item(self, producto):
    if producto in self.productos:
      self.productos.remove(producto)
      return f"Se ha eliminado el producto {producto.nombre} del carrito"

    return f"El producto {producto.nombre}, no se encuentra en el carrito"

  def obtener_items(self):
    if self.productos:
      return f"Los productos del carrito son: {[producto.nombre for producto in self.productos]}"

    return "No se han añadido productos al carrito"

  def obtener_total(self):
    total = 0
    for producto in self.productos:
      total += producto.precio
    return f"El coste total de los productos en el carrito es de ${total}"

producto1 = Producto("Pantalon", 20)
producto2 = Producto("Camisa", 30)
producto3 = Producto("Zapatos", 50)
producto4 = Producto("Reloj", 100)

carrito = CarritoDeCompras()
print(carrito.agregar_item(producto1))
print(carrito.agregar_item(producto2))
print(carrito.agregar_item(producto3))
print(carrito.agregar_item(producto4))

print(carrito.eliminar_item(producto4))
print(carrito.eliminar_item(producto3))

print(carrito.obtener_items())
print(carrito.obtener_total())

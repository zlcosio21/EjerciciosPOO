#Crea una clase llamada Empleado que tenga los atributos nombre , edad , y salario y que además, tenga los siguientes métodos:                   a. aumentar_salario - un método que toma un porcentaje como parámetro y aumenta el salario del empleado en ese porcentaje.                           b. mostrar_informacion - un método que imprime el nombre, la edad y el salario del empleado.


class Empleado:
  def __init__(self, nombre, edad, salario):
    self.nombre = nombre
    self.edad = edad
    self.salario = salario

  def aumentar_salario(self, porcentaje):
    if self.salario > 0:
      self.salario = (self.salario * porcentaje / 100) + self.salario
      print(f"Se aumento su salario un {porcentaje}%, su salario actual es de {self.salario}.\n")
    else:
      print("El empleado debe tener un salario mayor a $0.")

  def mostrar_imformacion(self):
    print(f"Empleado {self.nombre} de {self.edad} años con salario de ${self.salario}.")


empleado1 = Empleado("Kvaratskhelia", 21, 100)
empleado1.mostrar_imformacion()
empleado1.aumentar_salario(50)

empleado2 = Empleado("Marco Reus", 32, 0)
empleado2.mostrar_imformacion()
empleado2.aumentar_salario(10)

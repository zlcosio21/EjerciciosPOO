# Crea una clase llamada Empleado que tenga los atributos nombre , edad ,y salario y que además, tenga los siguientes métodos:                   
# a. aumentar_salario - un método que toma un porcentaje como parámetro y aumenta el salario del empleado en ese porcentaje.                         
# b. mostrar_informacion - un método que imprime el nombre, la edad y el salario del empleado.

class Empleado:
  def __init__(self, nombre, edad, salario):
    self.nombre = nombre
    self.edad = edad
    self.salario = salario
    
  def aumentar_salario(self, porcentaje):
    if self.salario > 0:
      self.salario  = ((self.salario * porcentaje) / 100) + self.salario
      return f"Se ha aumentado el salario un {porcentaje}% el total es de ${self.salario}"
            
    return "No se aumento el salario"
        
  def mostrar_informacion(self):
    return f"Empleado {self.nombre}, {self.edad} años, salario de ${self.salario}"
        
empleado1 = Empleado("Sebastian", "21", 200)
print(empleado1.aumentar_salario(20))
print(empleado1.mostrar_informacion())

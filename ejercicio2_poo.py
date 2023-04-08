#Crear una clase llamada CuentaBancaria con las siguientes especificaciones:   a. La clase debe tener los atributos numero_de_cuenta , saldo , y propietario b. La clase debe tener un método para depositar dinero en la cuenta.          c. La clase debe tener un método para retirar dinero de la cuenta.


class CuentaBancaria:
  def __init__(self, numero_de_cuenta, saldo, propietario):
    self.numero_de_cuenta = numero_de_cuenta
    self.saldo = saldo
    self.propietario = propietario

  def depositar(self, depositar_dinero):
    if depositar_dinero > 0:
      self.saldo += depositar_dinero
      print(f"Se ha depositado ${depositar_dinero} su saldo es de ${self.saldo}.")
    else:
      print("El monto a depositar debe ser mayor a cero.")

  def retirar(self, retirar_dinero):
    if retirar_dinero <= self.saldo:
      self.saldo -= retirar_dinero
      print(f"Se ha retirado ${retirar_dinero} su saldo es de ${self.saldo}. \n")
    else:
      print("El monto a retirar es mayor a su saldo. \n")


cuenta_usuario1 = CuentaBancaria (210606, 0, "Sebastián")
cuenta_usuario1.depositar(2000)
cuenta_usuario1.retirar(400)

cuenta_usuario2 = CuentaBancaria (11092011, 0, "JohnCena")
cuenta_usuario2.depositar(0)
cuenta_usuario2.retirar(100)
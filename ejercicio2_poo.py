# Crear una clase llamada CuentaBancaria con las siguientes especificaciones:
# a. La clase debe tener los atributos numero_de_cuenta , saldo , y propietario
# b. La clase debe tener un método para depositar dinero en la cuenta.         
# c. La clase debe tener un método para retirar dinero de la cuenta.

class CuentaBancaria:
  def __init__(self, numero_de_cuenta, saldo, propietario):
    self.numero_de_cuenta = numero_de_cuenta
    self.saldo = saldo
    self.propietario = propietario
    
  def depositar(self, dinero_depositado):
    if dinero_depositado > 0:
      self.saldo += dinero_depositado
      return f"Se ha depositado ${dinero_depositado} a su cuenta"
           
    return "Debe ingresar un monto mayor a 0"
    
  def retirar(self, dinero_retirado):
    if dinero_retirado <= self.saldo:
      self.saldo -= dinero_retirado
      return f"Se ha retirado un monto de {dinero_retirado} de su cuenta"
            
    return f"No cuenta con el suficiente saldo en su cuenta su saldo es de {self.saldo}"
        
propietario1 = CuentaBancaria("3105217565", 500, "Sebastian")
print(propietario1.depositar(500))
print(propietario1.retirar(800))
print(propietario1.saldo)

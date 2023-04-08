#Hacer una clase llamada Password con las siguientes especificaciones:        a. La clase debe tener los atributos longitud y password. La longitud por defecto será de 8.                      b. La clase debe tener un método que indique si la contraseña es fuerte teniendo en cuenta que para ser fuerte debe tener mínimo una longitud de 6.    c. La clase debe tener un método para cambiar la contraseña.


class Password:
  def __init__(self, password, longitud):
    self.password = password
    self.longitud = 8

  def contrasena_fuerte(self, longitud):
    if longitud >= 6:
      print(f"La contraseña {self.password} es fuerte")
    else:
      print(f"La contraseña {self.password} es débil")
  
  def cambio_password(self, actual_password, nueva_password):
    if actual_password == self.password:
      print("La contraseña se ha cambiado correctamente \n")
    else:
      print("Su contraseña actual es incorrecta \n")


password_usuario1 = Password("12345678", 8)
password_usuario1.contrasena_fuerte(8)
password_usuario1.cambio_password("12345678", "rosamelano")

password_usuario2 = Password("12345", 5)
password_usuario2.contrasena_fuerte(5)
password_usuario2.cambio_password("12345", "rosamelano")

password_usuario3 = Password("johnwick", 8)
password_usuario3.contrasena_fuerte(8)
password_usuario3.cambio_password("keanureeves", "rosamelano")

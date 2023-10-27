#Hacer una clase llamada Password con las siguientes especificaciones:
#a. La clase debe tener el atributo password.
#b. La clase debe tener un método que indique si la contraseña es fuerte teniendo en cuenta que para ser fuerte debe tener mínimo una longitud de 6.  
#c. La clase debe tener un método para cambiar la contraseña.


class Password:
  def __init__(self, password):
    self.password = password

  def es_fuerte(self):
    if len(self.password) >= 6:
      return f"La contraseña {self.password} es fuerte"
    
    return f"La contraseña {self.password} es débil"
  
  def cambiar_password(self, actual_password, nueva_password):
    if actual_password == self.password:
      return "La contraseña se ha cambiado correctamente \n"
    
    return "Su contraseña actual es incorrecta \n"

usuario1 = Password("12345678")
print(usuario1.es_fuerte())
print(usuario1.cambiar_password("12345678", "987654321"))

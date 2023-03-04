from empleado import Empleado
from gerente import Gerente
from cliente import Cliente

def mostrar_informacion(persona):
    print("#"*30)
    persona.mostrar_info()    

emp = Empleado("GULJ", "Jesus", "18 años", "j@gmaoo.com",
               "77718176761", 10, 100)

ger = Gerente("GULJ", "Jesus", "18 años", "j@gmaoo.com",
               "77718176761", 10, 100)

cli = Cliente("GUMK", "Karina", "32 años", "k@gmaoo.com",
               "77711116761", "Calle Ocuila #18")
cli.asignarEstadoMembresia(True)


mostrar_informacion(emp)
mostrar_informacion(ger)
mostrar_informacion(cli)
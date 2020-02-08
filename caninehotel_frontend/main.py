import xmlrpc.client

from caninehotel_frontend.config import(
	URL_SERVER
)
 
from caninehotel_frontend.operations import operations

def main():

	with xmlrpc.client.ServerProxy(URL_SERVER, allow_none = True) as client_stub:

		while True:

			print("seleccione la prueba a realizar: ")
			print("1. Carga prediseñada de usuarios")
			print("2. Carga prediseñada de perros")
			print("3. Carga prediseñada de habitaciones")
			print("4. Asignacion de cuarto")
			print("5. Retiro del perro del hotel")

			print("6. Obtener cantidad de cuartos ocupados")
			print("7. Lista de mascotas albergadas y no.cuarto asignado")
			print("8. Veces que se ha registrado una mascota")

			option = input("opcion : ")

			operations[int(option) - 1](client_stub)

if __name__ == '__main__':
	main()
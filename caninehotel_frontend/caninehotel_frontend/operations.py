from .data import(
	users,
	dogs,
	rooms,
	assignations
)

from .utils import obj_to_str

def register_users(stub):

	for user in users.users:
		print("GUARDANDO: " )
		print(user)

		print(stub.user.add(user))

def register_dogs(stub):

	for dog in dogs.dogs:
		print("GUARDANDO: " )
		print(dog)

		print(stub.dog.add(dog))

def register_rooms(stub):

	for room in rooms.rooms:
		print("GUARDANDO: " )
		print(room)

		print(stub.room.add(room))

def delete_dog(stub):
	print("LISTA DE MASCOTAS: ")

	print("IDENTIFICADOR   NOMBRE	RAZA	SEXO	DUEÑO")
	for dog in stub.dog.list(None):
		print("     {}		     {}		 {}		 {}		  {}".format(dog['_id'], dog['name'], dog['race'], dog['gender'], dog['owner']))

	dog = int(input("(identificador) : "))

	print(stub.dog.delete(dog))
	
def assignation_room(stub):

	print("LISTA DE MASCOTAS: ")

	print("IDENTIFICADOR  	 	NOMBRE		RAZA		SEXO		DUEÑO")
	for obj in stub.dog.list(None):
		print("     {}		     {}		 {}		 {}		  {}".format(obj['_id'], obj['name'], obj['race'], obj['gender'], obj['owner']))

	dog = int(input("(identificador) : "))

	print("LISTA DE HABITACIONES DISPONIBLES: ")

	print("NUMERO   TIPO	COSTO")
	for room in stub.room.list(False, False):
		print(room)
		print("  {}		 {}		  {}".format(room['_id'], room['type_room'], room['cost']))

	room = int(input("(numero) : "))

	reservation_date = input("Fecha de reservacion(dd/mm/YYYY)")
	culmination_date = input("Fecha de culminacion(dd/mm/YYYY)")

	reservation = dict(
		room = room,
		reservation_date = reservation_date,
		culmination_date = culmination_date
	)

	print(stub.stay.assign_room_to_dog(dog, reservation))


def list_rooms_occupied(stub):

	print("HABITACIONES OCUPADAS")

	print("NUMERO   		RESERVACION			CULMINACION")
	for room in stub.room.list(True, False):
		print("  {}		 {}		  {}".format(room['room'], obj_to_str(room['reservation_date']), obj_to_str(room['culmination_date'])))

	print("TOTAL: ", stub.room.list(True, True))


def list_dogs_housed(stub):

	print("MASCOTAS ALBERGADAS Y HABITACION")

	print("IDENTIFICADOR   		NOMBRE			RAZA			SEXO			DUEÑO  		HABITACIONES 		RESERVACION 		CULMINACION")
	for obj in stub.dog.list(True):
		print("     {}		     {}		 {}		 {}		  {} 	   {}          {}          {}".format(
			obj['dog']['_id'], obj['dog']['name'], obj['dog']['race'], obj['dog']['gender'], obj['dog']['owner'], obj['reservation']['room'], obj_to_str(obj['reservation']['reservation_date']), obj_to_str(obj['reservation']['culmination_date'])
		))

def count_register_dog(stub):

	print("IDENTIFICADOR   NOMBRE	RAZA	SEXO	DUEÑO")
	for dog in stub.dog.list(None):
		print("     {}		     {}		 {}		 {}		  {}".format(dog['_id'], dog['name'], dog['race'], dog['gender'], dog['owner']))

	dog = int(input("(identificador : )"))

	print("NUMERO DE REGISTROS : ")
	print(stub.dog.count_reservations(dog))

operations = tuple(
	[register_users,
	register_dogs,
	register_rooms,
	assignation_room,
	delete_dog,
	list_rooms_occupied,
	list_dogs_housed]
)
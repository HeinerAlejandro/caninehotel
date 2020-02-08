from datetime import datetime

from caninehotel_backend.decorators import (
	namespace_decorator,
	verify_format
)

from caninehotel_backend.utils import (
	logic_comparison_add_default,
	convert_object_to_list_dict,
	add_prefix_key_data
)

from caninehotel_backend.config import (
	DATE_FORMAT,
	message_error_add_object,
	message_object_saved,
	message_object_not_saved,
	message_list_error,
	message_object_updated,
	message_object_updated_error,
	message_object_not_found
)

from caninehotel_backend.modules.dogs.models import Dog

from .models import (
	Room,
	Reservation,
	Stay
)

@namespace_decorator('room')
def add(data):

	try:

		is_registrable = not bool(Room.objects(number = data.get('number')))
		
		if not is_registrable:
			return message_object_not_saved

		room = Room(**data)

		room.save()

		return message_object_saved.format(data)

	except Exception as err:
		print(err)
		return message_object_not_saved

@namespace_decorator('room')
def find(number):
	try:

		room = Room.objects.get(number = number)

		return room.to_mongo().to_dict()

	except Exception as e:
	
		return message_object_not_found.format(
			getattr(find, 'namespace'),
			number
		)

@namespace_decorator('room')
def list(actives = None, count = False):

	try:

		if actives == None:
			rooms_query = Room.objects
		else:
			rooms_query = Room.objects.get_rooms(active = actives)

		if count:
			return len(rooms_query)
		
		return convert_object_to_list_dict(rooms_query)

	except Exception as e:
		return message_list_error.format('rooms')


@namespace_decorator('stay')
def assign_room_to_dog(dog_identifier, data_reservation):
	
	try:

		dog = Dog.objects.get(identifier = dog_identifier)
		
		stay =  Stay.objects.get(dog = dog)
	
		data_reservation['room'] = Room.objects.get(number = data_reservation['room'])
		data_reservation['reservation_date'] = datetime.strptime(data_reservation['reservation_date'], DATE_FORMAT) 
		data_reservation['culmination_date'] = datetime.strptime(data_reservation['culmination_date'], DATE_FORMAT)
		
		reservation = Reservation(**data_reservation)
			
		stay.reservations.append(reservation)

		try:
			stay.save()
		except Exception as e:
			return message_object_updated_error.format(assign_room_to_dog.namespace)

		return message_object_updated.format(assign_room_to_dog.namespace)

	except Exception as e:

		return message_object_updated_error.format(assign_room_to_dog.namespace)
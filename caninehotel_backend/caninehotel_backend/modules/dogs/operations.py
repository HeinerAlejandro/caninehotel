from caninehotel_backend.decorators import (
	namespace_decorator,
	verify_format
)

from caninehotel_backend.config import(
	message_format_invalid,
	message_object_not_found,
	message_object_delete,
	message_object_saved,
	message_object_not_saved,
	message_object_delete_error,
	message_list_error,
	message_stack_void
)

from .formats import (
	FORMAT_DOG
)

from caninehotel_backend.utils import(
	logic_comparison_add_default,
	add_prefix_key_data,
	convert_object_to_list_dict
)

from caninehotel_backend.modules.users.models import User
from caninehotel_backend.modules.room.models import Stay

from .models import (
	Dog
)

@namespace_decorator('dog')
def add(data):

	try:

		user = User.objects.get(identification_card = data['owner'])
		print(user)
		data['owner'] = user

		dog = Dog(**data)

		stay = Stay(dog = dog)
		dog.save()
		stay.save()
		

		return message_object_saved.format(add.namespace)

	except Exception as e:
		return message_object_not_saved.format(add.namespace)

@namespace_decorator('dog')
def list(housed = True):

	try:

		try:
			if housed == None:
				dogs = Dog.objects
			else:
				dogs = Dog.objects.get_dogs(housed = housed)
		except Exception as e:
			
			print(e)

		if(dogs):
		
			data = convert_object_to_list_dict(dogs)

			return data

		return message_stack_void.format(add.namespace)

	except Exception as e:
		
		return message_list_error.format(add.namespace)

@namespace_decorator('dog')
def find(identifier):
	try:

		dog = Dog.objects.get(identifier = identifier)

		return dog.to_mongo().to_dict()

	except Exception as e:
	
		return message_object_not_found.format(
			find.namespace,
			identifier
		)

@namespace_decorator('dog')
def delete(identifier):

	try:
		dog = Dog.objects.get(identifier = identifier)
		
		dog.delete()

		return message_object_delete.format(delete.namespace)
	except Exception as e:
		print(e)
		return message_object_not_found.format(
			delete.namespace,
			identifier
	)

@namespace_decorator('dog')
def count_reservations(dog_identifier, count):

	try:

		dog = Dog.objects.get(identifier = dog_identifier)

		history = Stay.objects.get(dog = dog)

		if count:
			return len(history.reservations)

		return convert_object_to_list_dict(history.reservations)

	except Exception as e:
		return message_object_not_found.format(count_reservations.namespace)


from caninehotel_backend.decorators import (
	namespace_decorator,
	verify_format
)

from .models import User

from .formats import FORMAT_USER

from caninehotel_backend.config import (
	message_object_not_found,
	message_object_saved,
	message_object_not_saved,
	message_list_error
)

from caninehotel_backend.utils import (
	add_prefix_key_data,
	logic_comparison_add_default,
	convert_object_to_list_dict
)

@namespace_decorator('user')
def add(data):

	try:

		user = User(**data)

		user.save()

		return message_object_saved.format(add.namespace)

	except Exception as e:
		print(e)
		return message_object_not_saved.format(add.namespace)

@namespace_decorator('user')
def list():

	users = User.objects
	print(convert_object_to_list_dict(users))
	if users:
		return convert_object_to_list_dict(users)

	return message_list_error.format(add.namespace)

@namespace_decorator('user')
def find(card_identifier):
	
	try:

		user = User.objects.find(card_identifier = card_identifier)
		return user.to_mongo().to_dict()

	except Exception as e:
		
		return message_object_not_found.format(
			getattr(find, 'namespace'),
			card_identifier
		)

@namespace_decorator('user')
def delete(card_identifier):
	
	user = User.objects(card_identifier__exact = card_identifier)
	print(user)
	if user:
		user.delete()

		return message_delete_object.format(getattr(find, 'namespace'))

	return message_object_not_found.format(
		getattr(find, 'namespace'),
		card_identifier
	)

#@verify_format(FORMAT_USER, logic_comparison_add_default)
@namespace_decorator('user')
def modify(card_identifier, data):
	
	data = add_prefix_key_data(data, prefix = 'set', separator = '__')

	user = User.objects(card_identifier__exact = card_identifier)

	if user:
		user.update(**data)

		return user

	return message_object_not_found.format(
		getattr(find, 'namespace'),
		card_identifier
	)
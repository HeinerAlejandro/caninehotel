from datetime import datetime

from mongoengine import (

	Document,
	StringField,
	IntField,
	ReferenceField,
	EmailField,
	SequenceField,
	QuerySet
)

GENDERS_DOG = (
	'HEMBRA',
	'MACHO'
)

from caninehotel_backend.modules.room.models import Stay
from caninehotel_backend.modules.users.models import User

class DogQuerySet(QuerySet):

	def get_dogs(self, housed = True):


		now = datetime.now()
		
		stays_reserved = Stay.objects(
			reservations__reservation_date__lt = now,
			reservations__culmination_date__gte = now,
		)

		if not housed:

			stays = set(Stay.objects).difference(set(stays_reserved))
			print(stays[0].dog)
			dogs = list(map(lambda stay: stay.dog, stays))
		else:
			stays = stays_reserved

			dogs = list(map(lambda stay: dict(dog = stay.dog, reservation = stay.reservations[-1:]), list(stays)))

		return dogs

class Dog(Document):

	identifier = SequenceField(primary_key = True)
	name = StringField(min_length = 4, max_length = 20)
	age = IntField(min_value = 0)
	race = StringField(min_length = 4)
	gender = StringField(choice = GENDERS_DOG)
	owner = ReferenceField(User)

	meta = { 'queryset_class' : DogQuerySet }
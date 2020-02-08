from datetime import datetime

from mongoengine import (

	Document,
	StringField,
	FloatField,
	IntField,
	ReferenceField,
	DateTimeField,
	ListField,
	EmbeddedDocument,	
	EmbeddedDocumentField,
	QuerySet,
	CASCADE
)

from mongoengine.queryset.visitor import Q

class RoomQuerySet(QuerySet):

    def get_rooms(self, active):

    	now = datetime.now()

    	args_filter = dict(
    		reservations__reservation_date__lte = now,
    		reservations__culmination_date__gte = now
    	)

    	stays = Stay.objects(**args_filter)

    	if active:

    		rooms = tuple(
    			map(lambda stay : stay.reservations[-1], stays)
    		)

    	else:

    		rooms_all = set(Room.objects)
    		rooms_ocuped = set(map(lambda stay : stay.reservations[-1].room, stays))

    		rooms = rooms_all.difference(rooms_ocuped)

    	return rooms


class Room(Document):

	number = IntField(primary_key = True)
	type_room = StringField()
	cost = FloatField()

	meta = { 'queryset_class': RoomQuerySet }


class Reservation(EmbeddedDocument):

	room = ReferenceField('Room', require = True)
	reservation_date = DateTimeField()
	culmination_date = DateTimeField()
	
	def clean(self):
		
		super(Reservation, self).clean()
		
		now = datetime.now()

		stay = Stay.objects(
			reservations__culmination_date__gte = self.reservation_date,
			reservations__reservation_date__lte = self.culmination_date
		)

		if stay:
			raise ValueError('No se puede reservar una habitacion que ya esta siendo ocupada')


class Stay(Document):

	dog = ReferenceField('Dog')
	reservations = ListField(EmbeddedDocumentField(Reservation))


			

	

from mongoengine import (

	Document,
	StringField,
	FloatField,
	IntField,
	ReferenceField,
	DateTimeField,
	ListField,
	EmbeddedDocument
)

class Room(Document):

	type_room = StringField()
	cost = FloatField()
	number = IntField()

class Reservation(Document):

	number_room = ReferenceField('Room')
	reservation_date = DateTimeField()
	culmination_date = DateTimeField()

class Stay(Document):

	dog = ReferenceField('Dog')
	reservations = ListField(EmbeddedDocument(Reservation))


	def isActive(self):
		pass



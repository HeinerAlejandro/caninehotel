from mongoengine import (

	Document,
	StringField,
	IntField,
	ReferenceField,
	EmailField,
	ObjectIdField

)

GENDERS_DOG = (
	'HEMBRA',
	'MACHO'
)

class Dog(Document):

	identifier = ObjectIdField()
	name = StringField(min_length = 4, max_length = 20)
	age = IntField(min_value = 0)
	race = StringField(min_length = 4)
	gender = StringField(choice = GENDERS_DOG)
	owner = ReferenceField('User')
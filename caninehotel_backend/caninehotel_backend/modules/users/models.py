from mongoengine import (

	Document,
	StringField,
	IntField,
	ReferenceField,
	EmailField,
	ObjectIdField

)

class User(Document):

	identification_card = StringField()
	name = StringField()
	age = IntField()
	contact = StringField()

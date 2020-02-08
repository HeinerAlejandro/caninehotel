from mongoengine import (

	Document,
	StringField,
	IntField,
	ReferenceField,
	EmailField,
	ObjectIdField

)

class User(Document):

	identification_card = StringField(primary_key = True)
	name = StringField()
	age = IntField()
	contact = StringField()

from mongoengine import *

connect('caninehotel')

class o1(Document):
	a = StringField(primary_key = True)
	b = StringField()

class o2(Document):
	a = StringField()
	b = ReferenceField(o1)

o1o = o1(a = "dsdfafs", b = "vcxvx")
o2o = o2(a = "bbbb", b = o1o)

print("o1o:")
print(o1o.a)

print("o2o")
print(o2o.b)

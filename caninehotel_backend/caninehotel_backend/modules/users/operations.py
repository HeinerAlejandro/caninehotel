from caninehotel_backend.decorators import namespace_decorator

@namespace_decorator('user')
def add(data):
	pass

@namespace_decorator('user')
def find(card_identifier):
	pass

@namespace_decorator('user')
def delete(card_identifier):
	pass

@namespace_decorator('user')
def modify(card_identifier):
	pass
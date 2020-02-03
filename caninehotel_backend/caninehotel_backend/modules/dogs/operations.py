from caninehotel_backend.decorators import namespace_decorator

@namespace_decorator('dog')
def add(data):
	return "hay que hacer la logica llave"

@namespace_decorator('dog')
def find(card_identifier):
	return "pero que fresca, crees que puedes buscar a un usuario, sin siquiera haberlo registrado?"

@namespace_decorator('dog')
def delete(card_identifier):
	return "tu tas pasada chama, como vas a eliminar si no hay nadie?"

@namespace_decorator('dog')
def modify(card_identifier):
	return "mmm...como te digo..."
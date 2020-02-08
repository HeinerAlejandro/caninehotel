#ESTE RPROYECTO SOLO TENDRA SOPORTE PARA MONGODB
import socket
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#por si acaso 

MONGODB_NAME = 'caninehotel'
MODULE_OPERATIONS_NAME = 'operations'

modules = (
	'caninehotel_backend.modules.dogs',
	'caninehotel_backend.modules.room',
	'caninehotel_backend.modules.users',
)

DATE_FORMAT = '%d/%m/%Y'

PORT = 8080
HOST = socket.gethostbyname(socket.gethostname())

message_stack_void = 'Base de datos de {} se encuentra vacia'
message_list_error = 'Lista de objetos de {} no pudo ser obtenida'
message_object_saved = 'Objecto {} guardado exitosamente'
message_format_invalid = 'Lo siento, pero el formato de datos no es valido, debe ser el siguiente: {}.'
message_object_not_found = 'Lo siento, pero el objeto {} para el codigo {} no fue encontrado en nuestras Bases de datos.'
message_error_add_object = 'Lo siento, pero no ha podido registrar el objeto'
message_object_delete = '{} Eliminado correctamente'
message_object_not_saved = 'Objeto no guardado.'
message_object_updated = 'Objecto {} actualizado exitosamente'
message_object_updated_error = 'Objecto {} no actualizado'
message_object_delete_error = 'Objecto {}-{} no eliminado'
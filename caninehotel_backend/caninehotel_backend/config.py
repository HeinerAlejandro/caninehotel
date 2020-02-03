#ESTE RPROYECTO SOLO TENDRA SOPORTE PARA MONGODB

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#por si acaso 

MONGODB_NAME = 'canine_hotel'
MODULE_OPERATIONS_NAME = 'operations'

modules = (
	'caninehotel_backend.modules.dogs',
	'caninehotel_backend.modules.room',
	'caninehotel_backend.modules.users',
)

PORT = os.environ.get('PORT', 8080)
HOST = os.environ.get('HOST', 'localhost')
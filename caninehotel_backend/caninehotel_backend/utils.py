from importlib import import_module

from inspect import(

	getmembers,
	getmodule,
	isfunction
)

from .config import (
	modules,
	MODULE_OPERATIONS_NAME
)

from bson.objectid import ObjectId


import_module_path = lambda module_path : import_module(module_path + '.' + MODULE_OPERATIONS_NAME)

def register_rpc_operations(server, select_modules = None):

	if not select_modules:
		modules_imported = map(import_module_path, modules)
	else:
		modules_imported = map(register_rpc_operations, select_modules)

	count_modules = len(modules)

	print('cargando modulos ---> {}'.format(count_modules))

	for module in modules_imported:	

		name_func_tuples = getmembers(module, isfunction)
		rpc_tuple_operations = [t for t in name_func_tuples if getmodule(t[1]) == module]
		
		for name, procedure in rpc_tuple_operations:
			server.register_function(procedure, '{}.{}'.format(procedure.namespace, name))
			print('Procedimiento registrado ------> {}.{}'.format(procedure.namespace, name))

		count_modules = count_modules - 1

		print('Restantes ---> {}'.format(count_modules))

	return server

def iter_list_comprobate(data, logic_comparison:callable)->bool:

	for key in data.keys():
		if not logic_comparison(key):
			return False

	return True

def add_prefix_key_data(data, prefix = '', separator = ''):

	new_data = dict()

	for key, value in data.items():
		new_data[prefix + separator + key] = value

	return new_data

logic_comparison_add_default = lambda format_data : lambda key : key in format_data


def convert_object_to_list_dict(object_list):

	data_return = list()

	for object_element in object_list:

		if isinstance(object_element, (list, tuple)):
			object_dict = convert_object_to_list_dict(object_element)
			
		elif isinstance(object_element, dict):

			object_dict = object_element

			for key, data in object_dict.items():
				object_dict[key] = data.to_mongo().to_dict()

		else:
			object_dict = object_element.to_mongo().to_dict()

		data_return.append(object_dict)

	return tuple(data_return)
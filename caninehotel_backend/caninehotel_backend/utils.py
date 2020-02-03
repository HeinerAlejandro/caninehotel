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
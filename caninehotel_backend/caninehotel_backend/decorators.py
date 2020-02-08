from functools import wraps
from .utils import iter_list_comprobate

def namespace_decorator(namespace:str):

	def decorator(func):

		@wraps(func)
		def wrapper_func(*args, **kwargs):
			return func(*args, **kwargs)

		wrapper_func.namespace = namespace

		return wrapper_func

	return decorator

def verify_format(format_data:tuple, algorithm_logic:callable):

	def decorator(func):

		@wraps(func)
		def wrapped_func(*args):

			is_format_valid = iter_list_comprobate((isinstance(args[0], dict) and args[0]) or args[1], algorithm_logic(format_data))

			if not is_format_valid:
				from .config import message_format_invalid
				return message_format_invalid.format(format_data)

			func(*args)


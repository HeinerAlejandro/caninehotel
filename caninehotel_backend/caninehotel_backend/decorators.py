from functools import wraps

def namespace_decorator(namespace):

	def decorator(func):

		@wraps(func)
		def wrapper_func(*args, **kwargs):
			return func(*args, **kwargs)

		wrapper_func.namespace = namespace

		return wrapper_func

	return decorator

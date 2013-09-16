class Verbose(function):
	def __init__(self, func):
		self.func = func
		self.calls = 0

	def __call__(self, *args):
		result = self.func(*args)
		print calls, args, result
		return result

	def __repr__(self):
	 	"""Return docstring of original function."""
	 	return self.func.__doc__
	def __get__(self, obj, objtype):
		"""Allow instance methods on a wrapped object."""
		return functools.partial(self.__call__, obj)
		
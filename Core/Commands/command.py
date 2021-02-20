class Command:
	"""
	A class that stores the properties of the command passed by the user.
	"""
	def __init__(self):
		self.name = ''			# The name of the command that is sent
		self.type = '' 			# The type of command passed: start a connect, help, or general command.
		self.options = [] 		# The options
		self.args = []			# The arguments of command

	def __str__(self):
		"""
		Displays information about the properties of the command.
		"""
		out_string = 'Command info:\n\n' + \
					 f'Type:{self.type}\n' + \
					 f'Name:{self.name}\n' + \
					 f'Options:{self.options}\n' + \
					 f'Arguments:{self.args}\n'
		return out_string
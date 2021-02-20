from Core.JSRL.jsloader import load_links
from Core.Commands.command import Command
from include import INCLUDES


def encode_run(compiler, opts, ex_files, out_file):
	"""
	Generates a command to execute link via the terminal
	"""
	fmt = '{} {} {} -o {} && {}'			# Command format
	ex_files_string = ' '.join(ex_files)	# A string listing executable files
	opts_string = ' '.join(opts)			# A string listing compiler options

	return fmt.format(compiler, opts_string, ex_files_string, out_file, out_file)



class CommandDecoder:
	"""
	Command Decoder class
	Сonverts user-passed arguments to Command object for further execution.
	"""
	def __init__(self):
		self.cmd = Command()									# A command object
		self.links = load_links()								# A links dict
		self.commands = INCLUDES.keys()							# A list of available commands
		self.command_types = ['STANDARD', 'RUNLINK', 'HELP']	# Types of existing commands

	def decode(self, args):
		"""
		The main method that converts arguments to Command object
		"""
		self.cmd.type, self.cmd.name = self.__parse_cn__(args)	# Highlights the type and name of the command
		self.cmd.options = self.__parse_opt__(args)				# Highlights the user-passed options
		self.cmd.args = self.__parse_args__(args) 				# Highlights the args for command execution
		
		return self.cmd 										# Return the command object

	def show_command_info(self):
		"""
		Shows the properties of the command object
		"""
		print(self.cmd)
	
	def __parse_cn__(self, args):
		"""
		Retrieves the name and type of the command from the list of arguments, if it exists.
		"""
		first = args[0]										# First argument is command or link
		# Loop through all passed arguments
		if first.lower() in self.commands:					# If the word is in the list of commands
			return (self.command_types[0], first.lower())	# We return the STANDARD type and the name of the command

		if first in self.links:								# If the word is in the list of links
			return (self.command_types[1], first)			# We return the RUNLINK type and the name of the link
		
		if first.lower() == 'help':							# If the word is help
			return (self.command_types[2], first.lower())	# We return the HELP type and the name is equal 'help'

		return 'EXCEPTION', 'COMMAND_NOT_FOUND'				# If the first argument is not a command or link then we return the EXCEPTION type and the name COMMAND_NOT_FOUND

	def __parse_opt__(self, args):
		"""
		Remove options from the passed arguments.
		"""
		return [word for word in args if word.startswith('-') or word.startswith('--')]

	def __parse_args__(self, args):
		"""
		Remove arguments from the passed arguments.
		"""
		return [word for word in args if word not in self.cmd.options and word != self.cmd.name]

from Core.JSRL.jsloader import load_links, load_settings
from Core.Commands.cde import encode_run
from Core.Excepts.retcodes import STRING_TO_CODE
import include
import os



class EXC:
	"""
	The class responsible for passing the command to execution 
	after processing the Command Encoder by the class
	"""
	def __init__(self):
		self.command_list = include.INCLUDES.keys()	# A list of available commands
		self.links = load_links()					# List of existing links

	def run(self, command) -> int:
		"""
		The main method is responsible for the execution of the command that is sent.
		Accepts:
			command - Command object.
		"""	

		return_code = STRING_TO_CODE['COMMAND_NOT_FOUND']				# Standard return code - command not found

		if self._is_command(command):									# If the command is standard
			return_code = self._run_module(command.name, 'run', 
										   args=command.args,
										   opts=command.options)			# The run function is run in the module specified in includes
		
		elif self._is_link(command):									# If a link name is passed
			return_code = self._run_link(command)						# Calls the run link method and passes it the command object

		elif self._is_help(command):									# If the first word was help:
			return_code = self._run_help(command)						# Calls the method responsible for processing help commands

		# After performing all the previous actions, we process the return code
		if return_code:													
			return return_code
		else:
			return STRING_TO_CODE['EXIT_SUCCESS']

	def _run_help(self, command):
		"""
		Method that processes the user's help requests.
		Assepts:
			command - Command object.
		"""
		
		if command.args and command.args[0] in self.command_list:		# If the command exists and the list of passed commands is not empty
			return_code = self._run_module(command.args[0], 'get_help',
										   args=command.args,
										   opts=command.options) 		# The module passed to includes is started with the corresponding command
			return return_code

		elif not command.args:							# If the list of arguments after help is empty
			from Commands.main_help import run 			# Run the function that displays the general information
			run()
			return STRING_TO_CODE['EXIT_SUCCESS']
		
		else:											# If none of the above works, the team is not identified
			print('Command not found.')
			return STRING_TO_CODE['COMMAND_NOT_FOUND']

	def _run_module(self, module_name, func_name, args=[], opts=[]):
		"""
		Running a function from a specific module
		Accepts:
			module_name - [Str]  : The module from which the function is started 
			func_name   - [Str]  : Function name
			args  		- [List] : The arguments passed to the execution
			opts        - [List] : The options passed to the execution
		"""
		import_module = 'import Commands.{} as command_model'.format(module_name)
		runner = 'command_model.{}(args, opts)'.format(func_name)

		exec(import_module)
		exec(runner)

		return STRING_TO_CODE['EXIT_SUCCESS']

	def _run_link(self, command):
		"""
		The method is responsible for starting the bundle passed for execution
		"""

		main_settings = load_settings()				# Basic ASMR Settings
		link_setting = self.links[command.name]		# Settings of the transmitted link
		out_file_path = link_setting[-1]			# Path to the out file
		ex_files = link_setting[1:-1]				# Path to the execute files
		link_type = link_setting[0]					# Type of the link

		# Checking the correctness of the paths to the link files
		if self._is_correct_link(ex_files):
			print('Output:\n')
			os.system(encode_run(main_settings['compiler'], main_settings['compiler-flags'], ex_files, out_file_path))
			return STRING_TO_CODE['EXIT_SUCCESS']
		
		else:
			print('Incorrect data in link {}.\nCheck asmr salinks'.format(command.name))
			return STRING_TO_CODE['INCORRECT_LINK_DATA']

	def _is_correct_link(self, ex_files):
		"""
		Checking the correctness of the paths to the link files
		"""
		flag = True
		for file in ex_files:
			flag = flag and os.path.isfile(file)
		return flag

	def _is_command(self, command):
		"""
		Checking for belonging to the list of teams
		"""
		if command.type == 'STANDARD':
			return True
		return False

	def _is_link(self, command):
		"""
		Checking for belonging to the link list
		"""
		if command.type == 'RUNLINK':
			return True
		return False

	def _is_help(self, command):
		"""
		Checking for help membership
		"""
		if command.type == 'HELP':
			return True
		return False

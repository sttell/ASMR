"""
	Example of an executable command interface
"""

def run(args, opts):

	# The function is executed when the user enters
	# Called by: asmr [opts] test_command [args]
	print('args:', args)
	print('opts:', opts)

def get_help(args, opts):
	# Help to help the user.
	# Called by: asmr help test_command
	print('\n\nCommand test help\n\n')
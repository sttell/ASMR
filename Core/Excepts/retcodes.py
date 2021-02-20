"""
Module for storing return codes
"""
# Code entry form number - > String representation
CODE_TO_STRING = {None: 'The return code is not specified',
				  0: 'EXIT_SUCCESS',
			 	  1: 'COMMAND_NOT_FOUND',
			 	  2: 'INCORRECT_LINK_DATA'}

# Code entry form String representation - > number
STRING_TO_CODE = {}

# Initializes by passing through the previous dictionary
for key, item in CODE_TO_STRING.items():
	STRING_TO_CODE[item] = key 

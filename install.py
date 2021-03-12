import os
import json as js


def create_js(path):
	file = open(path, 'w')
	file.close()
	return os.path.abspath(path)


PATH = str(os.getcwd())			# full path from install directory

TEPMLATE_BASH = """#!/bin/bash
# Определение команды asmr

COMMAND=cmd
count=1
sep=[*]
""" + \
f'\nFULL_PATH_TO_SC={PATH}' + \
"""
while [ -n "$1" ]
do
COMMAND=${COMMAND}${sep}${1}
count=$[ $count + 1 ]
shift
done
""" + f'python3 {PATH}/pyasmr.py ' + '${sep} ${COMMAND}'

BASH_FILE_PATH = '/usr/local/bin/asmr'

file = open(BASH_FILE_PATH, 'w')
file.write(TEPMLATE_BASH)
file.close()

os.system(f'chmod 755 {BASH_FILE_PATH}')

settings_path = create_js(PATH + './JS/settings.json')
links_path = create_js(PATH + './JS/links.json')

TEMPLATE_INCLUDE_PY = '''
FULL_PATH_ASMR = '{}'

SETTINGS_PATH = FULL_PATH_ASMR + '/JS/settings.json'
DEFAULT_SETTINGS_PATH = FULL_PATH_ASMR + '/JS/dsettings.json'
LINK_FILE_PATH = FULL_PATH_ASMR + '/JS/links.json'
COMMANDS_MODULES_PATH = FULL_PATH_ASMR + '/Commands/'

# DICT: {COMMAND_NAME: MODULE IN COMMANDS FOLDER}
INCLUDES = {'sl': 'sl',
		    'showlinks': 'sl',
		    'nl':'nlink',
		    'nlink': 'nlink',
		    'newlink': 'nlink',
		    'ed': 'edit',
		    'edit': 'edit',
		    'rm': 'rml',
		    'rml': 'rml',
		    'rmlink': 'rml',
		    'sf': 'setflag',
		    'setf': 'setflag',
		    'setflag': 'setflag',
		    'ss': 'showsettings',
		    'showset': 'showsettings',
		    'showsettings': 'showsettings',
		    'settings': 'showsettings'}
'''
file = open('include.py', 'w')
file.write(TEMPLATE_INCLUDE_PY.format(PATH))
file.close()
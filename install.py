import os

PATH = str(os.getcwd())			# full path from install directory

TEPMLATE_BASH = """#!/bin/bash
# Определение команды asmr

COMMAND=cmd
count=1
sep=[*]
"""
+
f'\nFULL_PATH_TO_SC={PATH}'
+"""
while [ -n "$1" ]
do
COMMAND=${COMMAND}${sep}${1}
count=$[ $count + 1 ]
shift
done
s
""" + f'python3 {PATH}/pyasmr.py ' + '${sep} ${COMMAND}'

BASH_FILE_PATH = '/usr/local/bin/asmr'

file = open(BASH_FILE_PATH, 'w')
file.write(TEPMLATE_BASH)
file.close()

os.system(f'chmod 755 {BASH_FILE_PATH}')

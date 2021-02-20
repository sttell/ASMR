import os
import sys
import include
from Core.Commands.cde import CommandDecoder
from Core.Exec.executer import EXC

dir_path = sys.argv[1]
splitter = sys.argv[2]
user_args = sys.argv[3].split(splitter)[1:]

include.FULL_PATH_ASMR = dir_path

command_decenc = CommandDecoder()
command_exec = EXC()

command_object = command_decenc.decode(user_args)
command_exec.run(command_object)



# print(include.FULL_PATH_ASMR)
# print(dir_path, user_args)
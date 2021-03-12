import os
from Core.JSRL.jsloader import load_links, update_links, load_settings

'''
This command allows you to create a new bundle.
Several options are possible: Creating bundles With, Assembler, C + Assembler with automatic file naming, and manually specifying the path.
If the program does not find the path to the executable files, it will create a new file with the specified name along this path.
For correct execution, it is desirable to specify the full or relative paths, or not to specify them at all.

To use the command, you must specify the name of the bundle and its type, then the files will be named after the project name:
   asmr nlink [-c | -s | -sc] [Имя Связки] ---> creates 2 or 3 files(depending on the project type) with the names at the current path: [Link Name].[c | s]

If you want to set different file names, there are 2 ways to do this:
   1. asmr nlink test.c test.s TestLink    ---> creates a bundle of the Assembler + C type named TestLink along the current path with the test.c & test.s executable files
      asmr nlink test.s TestLink           ---> creates a bundle of the Assembler type named TestLink at the current path with the test.s executable file
      asmr nlink test.с TestLink           ---> creates a C-type bundle named TestLink at the current path with the test.c executable file
   
   2. asmr nlink -c test.c TestLink        ---> it works the same way as the commands above, the only difference is in the way the file is specified, the type of bundle is explicitly specified.
      asmr nlink -s test.s TestLink        ---> it works the same way as the commands above, the only difference is in the way the file is specified, the type of bundle is explicitly specified.
      asmr nlink -sc test.s test.c TestLink---> it works the same way as the commands above, the only difference is in the way the file is specified, the type of bundle is explicitly specified.
Самый простой синтаксис выглядит так:

asmr nlink -sc TestLink    --->   Creates a C + Assembler bundle with the TestLink.c, TestLink.s, and TestLink.out files at the current path.

Note that if the project type is not explicitly specified using the [-s | -c | -sc] option, then it is mandatory to specify the name of the files with extensions.
You can also use absolute or relative paths instead of the name if you want to create files in different locations.

Опции:
  -in 	| Create files in the current directory
  -s  	| Create a link of the Assembler type
  -sc 	| Create a link of the Assembler + C type
  -с  	| СCreate a link of the C type
  -nasm | Create a link-a file executed by the NASM translator
'''

ASM_SPEC = '.s' 	# Default Assembler file format
NASM_SPEC = '.asm'	# NASM Assembler file format
C_SPEC = '.c'		# C file format


# The function creates a file at the specified path and returns the absolute path
def create_file(fp):
	if os.path.isfile(fp):
		return os.path.abspath(fp)
	else:
		file = open(fp, 'w')
		file.close()
		return str(os.path.abspath(fp))
	

# -in opt
def inplace_opt(fp, ln, lt):
	links = load_links()								# load links dict
	if ln in links.keys():								# If this link is not in the list of links
		print('Связка с таким именем уже существует.')	# Inform user
		return 1										# return Error

	# Depending on the type of links, we create files and create a link
	if lt == 'CASM':
		asm_path = create_file(fp[ASM_SPEC])
		c_path = create_file(fp[C_SPEC])
		out_path = create_file(ln + '.out')
		link_info = ['sc', c_path, asm_path, out_path]
	elif lt == 'C':
		c_path = create_file(fp[C_SPEC])
		out_path = create_file(ln + '.out')
		link_info = ['c', c_path, out_path]
	elif lt == 'ASM':
		asm_path = create_file(fp[ASM_SPEC])
		out_path = create_file(ln + '.out')
		link_info = ['s', asm_path, out_path]
	elif lt == 'NASM':
		asm_path = create_file(fp[NASM_SPEC])
		out_path = create_file(ln + '.out')
		link_info = ['nasm', asm_path, out_path]
	elif lt == 'NOTYPE':
		return 1

	# Update links dict
	links[ln] = link_info
	update_links(links)
	return 0

# Then there are functions that handle specific types of bundles in the same way.
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# -c option
def c_opt(fp, ln, lt):
	links = load_links()		# Load links dict
	settings = load_settings()	# Load settigs dict

	# if link name not in links list
	if ln in links.keys():
		print('Связка с таким именем существует.')
		return 1

	# if link type 'NOTYPE'
	if lt == 'NOTYPE':
		# create files, update link
		c_path = create_file(ln + '.c')
		out_path = create_file(ln + '.out')
		link_info = ['c', c_path, out_path]
		links[ln] = link_info
		update_links(links)
	else:
		try:
			c_path = create_file(fp[C_SPEC])
			out_path = create_file(ln + '.out')
			link_info = ['c', c_path, out_path]
			links[ln] = link_info
			update_links(links)
		except KeyError:
			print('Произошла ошбика создания связки. Неверно указано расширение создаваемого файла.')
			return 1
		except:
			print('Произошла ошбика создания связки. Неверно указан файл или не удалось создать файл с таким именем.')
			return 1

# -s option
def asm_opt(fp, ln, lt):
	links = load_links()
	settings = load_settings()
	if ln in links.keys():
		print('Связка с таким именем существует.')
		return 1

	if lt == 'NOTYPE':
		asm_path = create_file(ln + '.s')
		out_path = create_file(ln + '.out')
		link_info = ['s', asm_path, out_path]
		links[ln] = link_info
		update_links(links)
	else:
		try:
			asm_path = create_file(fp[ASM_SPEC])
			out_path = create_file(ln + '.out')
			link_info = ['s', asm_path, out_path]
			links[ln] = link_info
			update_links(links)
		except KeyError:
			print('Произошла ошбика создания связки. Неверно указано расширение создаваемого файла.')
			return 1
		except:
			print('Произошла ошбика создания связки. Неверно указан файл или не удалось создать файл с таким именем.')
			return 1

# -sc option
def casm_opt(fp, ln, lt):
	links = load_links()
	settings = load_settings()
	if ln in links.keys():
		print('Связка с таким именем существует.')
		return 1

	if lt == 'NOTYPE':
		c_path = create_file(ln + '.c')
		asm_path = create_file(ln + '.s')
		out_path = create_file(ln + '.out')
		link_info = ['sc', c_path, asm_path, out_path]
		links[ln] = link_info
		update_links(links)
	else:
		try:
			c_path = create_file(fp[C_SPEC])
			asm_path = create_file(fp[ASM_SPEC])
			out_path = create_file(ln + '.out')
			link_info = ['sc', c_path, asm_path, out_path]
			links[ln] = link_info
			update_links(links)
		except KeyError:
			print('Произошла ошбика создания связки. Неверно указано расширение создаваемого файла.')
			return 1
		except:
			print('Произошла ошбика создания связки. Неверно указан файл или не удалось создать файл с таким именем.')
			return 1



# unparse arguments
def unparse_args(args):
	# Bit mask for all file types
	mask = {ASM_SPEC: 0,
			C_SPEC: 0,
			NASM_SPEC: 0}
	
	# File path dict
	fp_dict = {}

	for arg in args:
		if arg.endswith(ASM_SPEC):
			mask[ASM_SPEC] += 1
			fp_dict[ASM_SPEC] = arg
		elif arg.endswith(C_SPEC):
			mask[C_SPEC] += 1
			fp_dict[C_SPEC] = arg
		elif arg.endswith(NASM_SPEC):
			mask[NASM_SPEC] += 1
			fp_dict[NASM_SPEC] = arg
		else:
			link_name = arg

	# Link type
	if mask[ASM_SPEC] == 1 and mask[C_SPEC] == 1:
		ltype = 'CASM'
	elif mask[ASM_SPEC] == 1 and mask[C_SPEC] == 0:
		ltype = 'ASM'
	elif mask[ASM_SPEC] == 0 and mask[C_SPEC] == 1:
		ltype = 'C'
	elif mask[NASM_SPEC] == 1:
		ltype = 'NASM'
	else:
		ltype = 'NOTYPE'

	return fp_dict, link_name, ltype

# -nasm option
def nasm_opt(fp, ln, lt):
	links = load_links()
	settings = load_settings()

	if ln in links.keys():
		print('Связка с таким именем существует.')
		return 1

	if lt == 'NOTYPE':
		asm_path = create_file(ln + '.asm')
		out_path = create_file(ln + '.out')
		link_info = ['nasm', asm_path, out_path]
		links[ln] = link_info
		update_links(links)
	else:
		try:
			asm_path = create_file(fp[NASM_SPEC])
			out_path = create_file(ln + '.out')
			link_info = ['nasm', asm_path, out_path]
			links[ln] = link_info
			update_links(links)
		except KeyError:
			print('Произошла ошбика создания связки. Неверно указано расширение создаваемого файла.')
			return 1
		except:
			print('Произошла ошбика создания связки. Неверно указан файл или не удалось создать файл с таким именем.')
			return 1


def run(args, opts):
	opt_funcs = {'-in': inplace_opt,
	        '-c': c_opt,
	        '-s': asm_opt,
	        '-sc': casm_opt,
	        '-nasm': nasm_opt}
	if args:
		fp, ln, lt = unparse_args(args)
	else:
		print('Input the args. asmr help nlink')
		return 1

	if opts:
		opt_funcs[opts[0]](fp, ln, lt)
	else:
		pass


def get_help(args, opts):
	print('''                        nlink - New Link.
Данная команда позволяет созать новую связку.
Возможны несколько опций: Создание связок С, Assembler, C + Assembler с автоматическим наименованием файлов, ручное указание пути.
Если программа не найдет пути к исполняемым файлам, то создаст по этому пути новый файл с указанным именем.
Для корректного выполнения желательно указывать полный или относительный пути, либо не указывать их вообще.

Чтобы использовать команду необходимо указать имя связки и ее тип, тогда файлы будут названы именем проекта:
   asmr nlink [-c | -s | -sc] [Имя Связки] ---> создаст по текущему пути 2 или 3 файла(в зависимости от типа проекта) с именами [Имя Связки].[c | s]
Если же вы хотите задать иные имена файлам, то есть 2 способа это сделать: 
   1. asmr nlink test.c test.s TestLink    ---> создаст связку типа Assembler + C с именем TestLink по текущему пути с исполняемыми файлами test.c & test.s
      asmr nlink test.s TestLink           ---> создаст связку типа Assembler с именем TestLink по текущему пути с исполняемым файлом test.s
      asmr nlink test.с TestLink           ---> создаст связку типа С с именем TestLink по текущему пути с исполняемым файлом test.c
   
   2. asmr nlink -c test.c TestLink        ---> работает также как и команды выше, различие лишь в способе указания файла, явно указывается тип связки.
      asmr nlink -s test.s TestLink        ---> работает также как и команды выше, различие лишь в способе указания файла, явно указывается тип связки.
      asmr nlink -sc test.s test.c TestLink---> работает также как и команды выше, различие лишь в способе указания файла, явно указывается тип связки.

Самый простой синтаксис выглядит так:

asmr nlink -sc TestLink    --->   Создаст связку C + Assembler с файлами TestLink.c, TestLink.s, TestLink.out по текущему пути.

Обратите внимание, что если тип проекта явно не указан с помощью опции [-s | -c | -sc], то обязательно указание названия файлов с расширениями.
Так же вместо названия можно использовать абсолютные или относительные пути, если вы хотите создать файлы в разных местах.

Опции:
  -in 	| Создать файлы в текущей директории
  -s  	| Создать связку типа Assembler
  -sc 	| Создать связку типа Assembler + C
  -с  	| Создать связку типа C
  -nasm | Создать связку-файл исполняемый транслятором NASM

''')
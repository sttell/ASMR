import os
from Core.JSRL.jsloader import load_links, update_links, load_settings

ASM_SPEC = '.s'
C_SPEC = '.c'


def create_file(fp):
	if os.path.isfile(fp):
		return os.path.abspath(fp)
	else:
		file = open(fp, 'w')
		file.close()
		return str(os.path.abspath(fp))
	

def inplace_opt(fp, ln, lt):
	links = load_links()
	if ln in links.keys():
		print('Связка с таким именем уже существует.')
		return 1

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
	elif lt == 'NOTYPE':
		return 1

	links[ln] = link_info
	update_links(links)
	return 0


def c_opt(fp, ln, lt):
	links = load_links()
	settings = load_settings()
	if ln in links.keys():
		print('Связка с таким именем существует.')
		return 1

	if lt == 'NOTYPE':
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


def unparse_args(args):

	mask = {ASM_SPEC: 0,
			C_SPEC: 0}
	fp_dict = {}

	for arg in args:
		if arg.endswith(ASM_SPEC):
			mask[ASM_SPEC] += 1
			fp_dict[ASM_SPEC] = arg
		elif arg.endswith('.c'):
			mask[C_SPEC] += 1
			fp_dict[C_SPEC] = arg
		else:
			link_name = arg

	if mask[ASM_SPEC] == 1 and mask[C_SPEC] == 1:
		ltype = 'CASM'
	elif mask[ASM_SPEC] == 1 and mask[C_SPEC] == 0:
		ltype = 'ASM'
	elif mask[ASM_SPEC] == 0 and mask[C_SPEC] == 1:
		ltype = 'C'
	else:
		ltype = 'NOTYPE'

	return fp_dict, link_name, ltype


def run(args, opts):
	opt_funcs = {'-in': inplace_opt,
	        '-c': c_opt,
	        '-s': asm_opt,
	        '-sc': casm_opt}
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
  -in | Создать файлы в текущей директории
  -s  | Создать связку типа Assembler
  -sc | Создать связку типа Assembler + C
  -с  | Создать связку типа C

''')
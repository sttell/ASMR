from Core.JSRL import jsloader as jsl


'''
					SL - Show Links.
This command allows you to view existing file links.
Outputs the following information:
  1. For all links - Name, Type, number of files.
  2. For a specific bundle-Name, Type, number of files, file paths
To view information about a specific bundle, enter: asmr sl [Name]

Ex: asmr sl TestLinkName

Опции:
  -a  | Show all existing links
  -s  | Show links of the Assembler type
  -sc | Show links of the Assembler + C type
  -с  | Show links of the C type

Ex: asmr sl -a
    asmr sl -s
    asmr sl -sc
'''


def a_flag(links, type_dict):
	print('Существующие связки:')
	for i, (key, item) in enumerate(links.items()):
		print(f'# {i + 1} -- {key} ---> Тип: {type_dict[item[0]]}. Исполняемые файлы: {len(item) - 1} шт.')


def s_flag(links, type_dict):
	print('Существующие связки типа Assembler:')
	counter = 1
	for key, item in links.items():
		if type_dict[item[0]] == type_dict['s']:
			print(f'# {counter} -- {key} ---> Тип: {type_dict[item[0]]}. Исполняемые файлы: {len(item) - 1} шт.')
			counter += 1


def sc_flag(links, type_dict):
	print('Существующие связки типа Assembler + C:')
	counter = 1
	for key, item in links.items():
		if type_dict[item[0]] == type_dict['sc']:
			print(f'# {counter} -- {key} ---> Тип: {type_dict[item[0]]}. Исполняемые файлы: {len(item) - 1} шт.')
			counter += 1


def c_flag(links, type_dict):
	print('Существующие связки типа C:')
	counter = 1
	for key, item in links.items():
		if type_dict[item[0]] == type_dict['c']:
			print(f'# {counter} -- {key} ---> Тип: {type_dict[item[0]]}. Исполняемые файлы: {len(item) - 1} шт.')
			counter += 1

def nasm_flag(links, type_dict):
	print('Существующие связки исполняемые NASM:')
	counter = 1
	for key, item in links.items():
		if type_dict[item[0]] == type_dict['nasm']:
			print(f'# {counter} -- {key} ---> Тип: {type_dict[item[0]]}. Исполняемые файлы: {len(item) - 1} шт.')
			counter += 1


def run(args, opts):
	settings = jsl.load_settings()
	links = jsl.load_links()
	type_dict = {'s':'Assembler',
	 			 'sc': 'Assembler + C',
	 			 'c': 'C',
	 			 'nasm': 'NASM'}
	opts_funcs = {'-a': a_flag,
				  '-s': s_flag,
				  '-sc': sc_flag,
				  '-c': c_flag,
				  '-nasm': nasm_flag}

	if opts:
		try:
			opts_funcs[opts[0]](links, type_dict)
			return 0
		except KeyError:
			print('Такой опции не существует в команде SL. Введите asmr help sl')
		except IndexError:
			pass
	if args:
		if args[0] in links.keys():
			link_info = links[args[0]]
			print(f'Связка {args[0]} ---> Тип: {type_dict[link_info[0]]}. Кол-во исполняемых файлов: {len(link_info) - 1} шт.')
			print(f'Исполняемые файлы:')
			for i, file in enumerate(link_info[1:]):
				print(f'  #{i + 1}: {file}')
			return 0
		else:
			print('Связки с таким именем не найдено.')
			return 1
	print('Введите опцию или название связки.')



def get_help(args, opts):
	print('''                        SL - Show Links.
Данная команда позволяет посмотреть существующие связки файлов.
Выводит следующую информацию:
  1. Для всех связок - Название, Тип, кол-во файлов.
  2. Для конкретной связки - Название, Тип, кол-во файлов, пути к файлам
Чтобы посмотреть информацию о конкретной связке введите asmr sl [Название]

Ex: asmr sl TestLinkName

Опции:
  -a  | Показать все существующие связки
  -s  | Показать связки типа Assembler
  -sc | Показать связки типа Assembler + C
  -с  | Показать связки типа C

Ex: asmr sl -a
    asmr sl -s
    asmr sl -sc
''')
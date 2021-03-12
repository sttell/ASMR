import os
from Core.JSRL.jsloader import load_links, load_settings

'''
This command allows you to start editing the bundle files.
By default, all executable files of the bundle are started for editing(option-e).

There are several ways to use it:
  1. Enter asmr edit [Bundle Name] - edit all executable files
  2. Enter asmr edit-option [Bundle Name] - edit a specific file type

Ex: asmr edit Test Link Name

Options:
  -e | By default. Opens all executable files.
  -s | Open all files of the "*.s" type for editing
  -c | Open all files of the "*.c" type for editing
  -o | Open all files of the "*.out" type for editing

Ex: asmedit -e Test Link Name
asmr edit -s Test Link Name
asmr edit -o Test Link Name
'''


# option -e
def opt_e(tr, link):
	no_opt(tr, link)


# option -c
def opt_c(tr, link):
	for f in link[1:]:
		if f.endswith('.c'):
			os.system(tr + f' {f}')


# option -s
def opt_s(tr, link):
	for f in link[1:]:
		if f.endswith('.s') or f.endswith('.asm'):
			os.system(tr + f' {f}')


# option -o
def opt_o(tr, link):
	for f in link[1:]:
		if f.endswith('.out'):
			os.system(tr + f' {f}')


# no options
def no_opt(tr, link):
	for file in link[1:-1]:
		os.system(tr + f' {file}')


def run(args, opts):
	settings = load_settings()   # load settiongs from json
	tr = settings['text-reader'] # get text-reader
	links = load_links()		 # load links dict

	# dict 'opt_name' = > function
	opt_dict = {'-e': opt_e,
	 			'-c': opt_c,
	 			'-s': opt_s,
	 			'-o': opt_o,
	 			'no_opt': no_opt}

	
	# if args list not empty and 1st argument in links list
	if args and args[0] in links.keys():
		link = links[args[0]] # get link info

		# if opts list empty
		if not opts:
			opt_dict['no_opt'](tr, link)

		# else called opt func from optrions dict
		else:
			opt_dict[opts[0]](tr, link)
	else:
		print('Связки с таким именем не существует.')



def get_help(args, opts):
	print('''\n                        Edit -- Edit Link.
Данная команда позволяет запустить редактирование файлов связки.
По умолчанию на редактирование запускуются все исполняемые файлы связки(опция -е).
Существует несколько способов использования:
   1. Введите asmr edit [ИмяСвязки] - редактирование всех исполняемых файлов
   2. Введите asmr edit -опция [ИмяСвязки] - редактирование конкретного типа файлов

Ex: asmr edit TestLinkName

Опции:
  -e  | По умолчанию. Открывает все исполняемые файлы.
  -s  | Открыть на редактирование все файлы типа "*.s"
  -c  | Открыть на редактирование все файлы типа "*.c"
  -o  | Открыть на редактирование все файлы типа "*.out"

Ex: asmr edit -e TestLinkName
    asmr edit -s TestLinkName
    asmr edit -o TestLinkName


''')
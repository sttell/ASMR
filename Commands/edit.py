import os
from Core.JSRL.jsloader import load_links, load_settings


def opt_e(tr, link):
	no_opt(tr, link)


def opt_c(tr, link):
	for f in link[1:]:
		if f.endswith('.c'):
			os.system(tr + f' {f}')


def opt_s(tr, link):
	for f in link[1:]:
		if f.endswith('.s'):
			os.system(tr + f' {f}')

def opt_o(tr, link):
	for f in link[1:]:
		if f.endswith('.out'):
			os.system(tr + f' {f}')


def no_opt(tr, link):
	for file in link[1:-1]:
		os.system(tr + f' {file}')


def run(args, opts):
	settings = load_settings()
	tr = settings['text-reader']
	links = load_links()
	opt_dict = {'-e': opt_e,
	 			'-c': opt_c,
	 			'-s': opt_s,
	 			'-o': opt_o,
	 			'no_opt': no_opt}

	
	if args[0] in links.keys():
		link = links[args[0]]
		if not opts:
			opt_dict['no_opt'](tr, link)
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
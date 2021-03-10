from Core.JSRL.jsloader import load_settings


def run(args, opts):
	settings = load_settings()
	compiler = settings['compiler']
	opts = settings['compiler-flags']
	text_reader = settings['text-reader']
	tmp = '''
Текущие настройки сборки связок:
   Компилятор: {}
   Передаваемые компилятору опции: {}

Для редактирования файлов назначен редактор: {}
'''
	opt_string = f'[{opts[0]}'
	for opt in opts[1:]:
		opt_string += f', {opt}'
	opt_string += ']'
	print(tmp.format(compiler, opt_string, text_reader))


def get_help(args, opts):
	print('''\n                        showsettings -- Show Settings.
Команда показывает текущие настройки сборки и программу отвечающую за редактирование файлов.


''')
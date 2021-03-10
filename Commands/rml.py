import os
from Core.JSRL.jsloader import load_links, update_links


def f_opt(args, links):
	link_name = args[0]
	if link_name in links.keys():
		asw = input(f'Вы уверены, что хотите удалит связку {link_name} вместе с ее файлами?(Да/Нет || Yes/No)\n>>> ')
		if asw.strip().lower() in 'yes y yeah ye д да':
			for file in links[link_name][1:]:
				try:
					os.remove(file)
				except:
					print('Файл {} не найден. Удаление продолжается.'.format(file))
			del links[link_name]
			update_links(links)
			print(f'Связка с именем {link_name} успешно удалена. Исполняемые файлы удалены.')
		else:
			print('Удаление отменено.')
	else:
		print('Связки с таким именем не существует.')


def run(args, opts):
	links = load_links()
	opt_dict = {'-f': f_opt}

	if args:
		link_name = args[0]
		if opts:
			try:
				opt_dict[opts[0]](args, links)
			except KeyError:
				print(f'Опции "{opts[0]}" не существует. Для справки введите asmr help rml.')
		else:
			if link_name in links.keys():
				asw = input(f'Вы уверены, что хотите удалит связку {link_name}?(Да/Нет || Yes/No)\n>>> ')
				if asw.strip().lower() in 'yes y yeah ye д да':
					del links[link_name]
					update_links(links)
					print(f'Связка с именем {link_name} успешно удалена. Исполняемые файлы остались.')
				else:
					print('Удаление отменено.')
			else:
				print('Связки с таким именем не существует.')

	else:
		print('Укажите имя связки которую хотите удалить.')


def get_help(args, opts):
	print('''                        RML - Remove Link.
Данная команда удаляет связку файлов. По умолчанию удаление происходит без удаления исполняемых файлов.
Чтобы удалить конкретную связку введите: asmr rml [Имя Связки]

Ex: asmr rml TestLinkName

Опции:
  -f  | Удалить связку вместе с файлами

Ex: asmr rml -f TestLink
	asmr rml TestLink

''')
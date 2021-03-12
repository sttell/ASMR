import os
from Core.JSRL.jsloader import load_links, update_links


'''
                        RML - Remove Link.
This command deletes a bundle of files. By default, deletion occurs without deleting executable files.
To delete a specific bundle, enter: asmr rml [Имя Связки]

Ex: asmr rml TestLinkName

Options:
  -f  | Delete the bundle along with the files

Ex: asmr rml -f TestLink
	asmr rml TestLink
'''


# -f option
def f_opt(args, links):
	link_name = args[0]
	# if link name in links list
	if link_name in links.keys():
		# confirm operation
		asw = input(f'Вы уверены, что хотите удалить связку {link_name} вместе с ее файлами? (Да/Нет || Yes/No)\n>>> ')
		# if confirmed
		if asw.strip().lower() in 'yes y yeah ye д да':
			# Delete all files
			for file in links[link_name][1:]:
				
				try:
					os.remove(file)
				except:
					print('Файл {} не найден. Удаление продолжается.'.format(file))
			
			# delete link
			del links[link_name]
			# update links settings
			update_links(links)
			
			print(f'Связка с именем {link_name} успешно удалена. Исполняемые файлы удалены.')
		
		# if do not confirmed
		else:
			print('Удаление отменено.')
	
	else:
		print('Связки с таким именем не существует.')


def run(args, opts):
	links = load_links()		# Load links
	opt_dict = {'-f': f_opt}	# Options dict 'opt_name' -> function

	# if args list not empty
	if args:
		link_name = args[0] 	# get link

		# if options list
		if opts:
		
			try:
				opt_dict[opts[0]](args, links) # run option function
			
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
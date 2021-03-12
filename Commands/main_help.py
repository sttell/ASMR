def run():
	print('''\n\n
Добро пожаловать в ASMR.
На данный момент доступны следующие команды:
	
	# asmr [Link Name]                     	- исполнение связки
	
	# asmr edit [opts] [LinkName]          	- редактировать связку
	  [ed | edit]
	
	# asmr nlink [opts] [files] [LinkName] 	- создать новую связку
	  [nl | nlink | newlink]
	
	# asmr rml [opts] [LinkName]          	- удалить существующую связку
	  [rm | rml | rmlink]
	
	# asmr setflag [Flags] 					- назначить передаваемые компилятору флаги
	  [sf | setflag] 
	
	# asmr showsettings 					- посмотреть текущие настройки
	  [ss | showset | showsettings]
	
	# asmr sl [opts]						- посмотреть список существующих связок 
	  [sl | showlinks]						  или информацию о конкретной
	

Чтобы запустить связку на исполнение введите asmr LinkName, где всместо LinkName будет
соответственно название связки.
Если хотите посмотреть подробную информацию по конкретной команде введите asmr help CommandName.
Большинство команд имеют свои синонимы которые указаны под кратким описанием команды.
То есть asmr ed Link и asmr edit Link работают эквивалентно.
\n\n'''')
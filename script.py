import requests
import datetime
from zipfile import ZipFile

def script(serverName='default'):  # имя по умолчанию
	urlPage = 'https://raw.githubusercontent.com/GreatMedivack/files/master/list.out'
	r = requests.get(urlPage) # запрос со страницы
	rText = str(r.text)  # преобразование запроса в строку
	nowTime = datetime.datetime.now().strftime('%d-%m-%Y') # получение времени
	fileName = serverName + '_' + nowTime + '_' + 'running.out' # имя файла
	zipName = serverName + '_' + nowTime + '.zip' # имя архива
	with open('downloadFile', 'w', encoding='utf-8') as f: # записываем в файл
		f.write(rText)

	with open('downloadFile', 'r', encoding='utf-8') as f:
		for i in f:
			data = i.split()  # разбиваем строку на пробелы, получаем столбцы
			if data[2] == 'Running': # если второй столбец Running
				with open(fileName, "a", encoding='utf-8') as sortFile:
					a = f'{data[0]}\n'  # записываем нулевой столбец
					sortFile.write(a)

	with ZipFile(f'archives/{zipName}', 'w') as zip: # создание зип архива
		zip.write(fileName)
		if zip.testzip() == None:  # проверка на целостность
			print('Zip OK')
		else:
			print('Error')

script()
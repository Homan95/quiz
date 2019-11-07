symb=['а', 'б', 'в', 'г', 'д', 'А', 'Б', 'В', 'Г', 'Д','q']

def correct_inmput(a):
	while a not in symb:
		print('Не правитьний ввід данних')
		a=input()

	return a

def imput_answer():
	wasd=input()
	wasd=correct_inmput(wasd)
	if wasd=='q':
		exit(0)
	elif wasd=='а' or wasd=='А':
		qwe=0
	elif wasd=='б' or wasd=='Б':
		qwe=1
	elif wasd=='в' or wasd=='В':
		qwe=2
	elif wasd=='г' or wasd=='Г':
		qwe=3
	elif wasd=='д' or wasd=='Д':
		qwe=4
	return qwe


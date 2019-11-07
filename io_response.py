def veryfy(q,a):
	if q.choices[a]['is_correct']:
		return True
	else:
		return False

def print_result(a,i):
	if i :
		print ('Відповідь правильна')
	else:
		print ('Відповідь не правильна')

def is_continue():
	k=input('Продовжити тестування? Y/N ')
	if k=='Y' or k=='y':
		return True
	else:
		quit(0)	
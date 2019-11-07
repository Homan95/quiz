import json
import random

def read_from_file():
	with open('questions.json') as abc:
		data=abc.read()
		questionss=json.loads(data)
	return questionss

class Questions:
	def __init__(self, question):
		self.question=question
	def len_questions(self):
		return len(self.question)
b=[]
def get_random_question():
	a=Questions(read_from_file())
	fx=random.randint(0,a.len_questions()-1)
	if fx not in b:
		b.append(fx)
		return question4print(a.question[fx])
	elif len(b)>=a.len_questions():
		print("ви відповіли на всі питання")
		exit(0)
	else:
		get_random_question()

class question4print:
	def __init__(self,a):
		self.id=a['id']
		self.content=a['content']
		self.choices=a['choices']
		#self.iscorrekt=a['choices']
	def display(self):
		print (self.content)
		print('Варіанти відповіді')
		print(self.choices[0]['content'])
		print(self.choices[1]['content'])
		print(self.choices[2]['content'])
		print(self.choices[3]['content'])
		try:
			print(self.choices[4]['content'])
		except:
			pass			

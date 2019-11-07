#import questionss, answers, io_response
from questionss import get_random_question
from answers import imput_answer
from io_response import veryfy
from io_response import print_result
from io_response import is_continue

def run_quiz():
	question=get_random_question()
	question.display()
	answer=imput_answer()
	is_correct=veryfy(question,answer)
	print_result(answer,is_correct)
	if is_continue():
		run_quiz()

if __name__ =="__main__":	
	run_quiz()
########## Building a Multiple Choice Quiz ##########

### Question.py ###
class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.prompt = answer
	

	
### app.py ###
from Question import Question

question_prompts = [ ... ]

questions = [
	Question(question_prompts[0], "a")
	Question(question_prompts[1], "b")
	Question(question_prompts[2], "c")
]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
	print("You got " + str(score) + "/" + str(len(questions) + "Correct")
				
run_test(questions)

				
	

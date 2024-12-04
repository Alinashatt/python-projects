from data import question_data
from question_model import Qusetion
from quiz_brain import QuizBrain
question_bank = []
for x in question_data["results"]:
    question_text = x["question"]
    question_answer = x["correct_answer"]
    question_bank.append(Qusetion(question_text,question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"\nCONGRATULATIONS you finish the quiz. \nYour score is {quiz.attribute}")
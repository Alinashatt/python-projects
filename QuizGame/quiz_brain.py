class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.attribute = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)



    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q {self.question_number + 1}: {current_question.text} (True/False)? : ")
        self.question_number += 1
        self.check_answer(current_question.answer,user_answer)

    def check_answer(self,current_question_user,user_answer):
        if user_answer == current_question_user.lower():
            self.attribute += 1
            print("you're right keep going!")
            print(f"your score is {self.attribute}/{self.question_number}")
        else:
            print("you are wrong!")
            print(f"your score is {self.attribute}/{self.question_number} \n")

        print(f"the correct answer is {current_question_user}")

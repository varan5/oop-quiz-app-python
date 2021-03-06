class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def increament_score(self):
        self.score += 1

    def print_score(self):
        print('Your current score is: ', self.score)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text}. (True/False):  ')
        result_flag = self.check_answer(user_answer)
        if result_flag == True:
            print('Congrats, your answer is correct')
            self.increament_score()
            self.print_score()
        else:
            print('Wrong answer, All the best for the next question')
            self.print_score()


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        print('User answered: ', user_answer)
        print('Correct answer: ', correct_answer)
        if correct_answer == user_answer:
            return True
        else:
            return False




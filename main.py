from question_model import Question as Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    single_question_set = Question(question_text, question_answer)
    question_bank.append(single_question_set)

quiz_brain_object = QuizBrain(question_bank)
while quiz_brain_object.still_has_questions():
    quiz_brain_object.next_question()








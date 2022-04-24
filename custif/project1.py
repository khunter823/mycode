#!/usr/bin/env python3



class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "I'm the rare case when today comes before yesterday. What am I? ",
     "What goes all the way around the world but stays in a corner? ",
     "What gets bbigger the more you take away? "
]

questions = [
     Question(question_prompts[0], "dictionary"),
     Question(question_prompts[1], "stamp"),
     Question(question_prompts[2], "hole")
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)


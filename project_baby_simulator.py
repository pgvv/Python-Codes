from random import choice

questions = ["Why is the sky blue? ",
             "Where are all the dinosaurs? ",
             "Why is the sun so bright? "]
question = choice(questions)

answer = input(question).capitalize()

while answer != "Just because":
    answer = input("Why??? ").capitalize()

print("Hmmmmm.....")

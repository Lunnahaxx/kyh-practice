from yt_quiz_class_questions import Question_class
import random
question_prompts = [
    "Vad är en bil?\n(a) En leksak\n(b) En låt\n(c) En brumum\n",
    "Vem är jag?\n(a) Nej\n(b) Vem vet\n(c) Varför\n",
    "Bästa vännen?\n(a) Hunden\n(b) Katten \n(c) Glassen\n"
]

questions = [
    Question_class(question_prompts[0], "b"),
    Question_class(question_prompts[1], "b"),
    Question_class(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for sho in questions:
        random.shuffle(prompten)
        answer = input(sho.prompten) #store user input response
        print(f"Ditt svar: {answer}\n")

        if answer == sho.answer:
            score += 1
    print(f"Du fick {score} av {len(questions)} rätt")

run_test(questions)
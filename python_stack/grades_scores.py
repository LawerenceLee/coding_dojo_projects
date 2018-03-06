import random


def random_scores():
    scores = []
    for _ in range(10):
        scores.append(random.randint(60, 100))
    return scores


def grades(score_list):
    print("Scores and Grades")
    for score in score_list:
        grade = ""
        if score <= 69:
            grade = "D"
        elif score <= 79:
            grade = "C"
        elif score <= 89:
            grade = "B"
        else:
            grade = "A"
        print("Score: {} Your grade is {}".format(score, grade))
    print("End of program. Bye!")


grades(random_scores())

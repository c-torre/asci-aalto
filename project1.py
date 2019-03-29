#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np


np.random.seed(0)


# useless stuff down there
def main():
    learn()


class Teacher:

    def __init__(self):
        self.sheet = {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 2, 7: 3, 8: 4}

    # This can be a class method (i.e. @classmethod[new line]def ask(cls):[same as before]
    def ask(self):
        question = np.random.randint(low=1, high=9)
        return question

    def answer_check(self, student, question, answer):
        if answer == self.sheet[question]:
            # It would be better to this by calling a method (e.g., student.learn(question, answer) )
            student.memory[question] = answer
        else:
            pass


class Student:

    def __init__(self):
        self.memory = {1: "a", 2: "a", 3: "a", 4: "a", 5: "a", 6: "a", 7: "a",
                       8: "a"}

    def think(self, question):
        if self.memory[question] == "a":
            answer = np.random.randint(low=1, high=5)
        else:
            answer = self.memory[question]
        return answer

# Create a SmartStudent class that inherit from student but is smarter by using RL

# Reduce to two options


def learn():
    epoch = 0

    student = Student()
    teacher = Teacher()

    print("training begins...")

    # This is very beautiful... Another idea?
    while "a" in student.memory.values():

        question = teacher.ask()
        answer = student.think(question)
        teacher.answer_check(student=student, question=question, answer=answer)

        epoch += 1

        # Consider using tqdm library
        # plt graph
        print("epochs:", epoch)

    print("finished training")
    print(student.memory)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import numpy as np

np.random.seed(0)


def main():
    pass


class Teacher:

    def __init__(self):
        self.sheet = {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 2, 7: 3, 8: 4}

    def ask(self):
        question = random.randint(1, 8)
        return question

    def answer_check(self, question, answer):
        if answer == self.sheet[question]:
            student.memory[question] = answer
        else:
            pass


class Student:

    def __init__(self):
        self.memory = {1: "a", 2: "a", 3: "a", 4: "a", 5: "a", 6: "a", 7: "a",
                       8: "a"}

    def think(self, question):
        if self.memory[question] == "a":
            answer = random.randint(1, 4)
        else:
            answer = self.memory[question]
        return answer

    def learn(self):
        epoch = 0

        print("training begins...")

        while "a" in self.memory.values():
            question = teacher.ask()
            answer = self.think(question)
            teacher.answer_check(question, answer)

            epoch += 1
            # print(memory) # Debugging
            print("epochs:", epoch)

        print("finished training")
        print(self.memory)


student = Student()
teacher = Teacher()
student.learn()

if __name__ == "__main__":
    main()

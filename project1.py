#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import time
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


# np.random.seed(0)


class Main:

    def reinforcement_learn(self):
        """Reinforcement learning using the Rescorla-Wagner model"""
        student0 = SmartStudent()
        teacher0 = Teacher()

        student0.learn(teacher0.reward_vector0, teacher0.reward_vector1)

    def stupid_learn(self):
        """Learning by random guessing"""
        epoch = 0

        student = Student()
        teacher = Teacher()

        print("training begins...")

        # This is very beautiful... Another idea?
        while "a" in student.memory.values():

            question = teacher.ask()
            answer = student.think(question)
            teacher.answer_check(student=student, question=question,
                                 answer=answer)

            epoch += 1

            print("epochs:", epoch)

        print("finished training")
        print(student.memory)


class Teacher:

    def __init__(self):
        self.sheet = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 1}
        self.reward_vector0 = np.array([100, 0, 100, 0, 100, 0, 100, 0, 100, 0])
        self.reward_vector1 = np.array([0, 100, 0, 100, 0, 100, 0, 100, 0, 100])

    # This can be a class method
    # (i.e. @classmethod[new line]def ask(cls):[same as before]
    def ask(self):
        question = np.random.randint(low=0, high=10)
        return question

    def answer_check(self, student, question, answer):
        if answer == self.sheet[question]:
            # It would be better to this by calling a method
            # (e.g., student.learn(question, answer) )
            student.memory[question] = answer
        else:
            pass


class Student:

    def __init__(self):
        self.memory = {0: "a", 1: "a", 2: "a", 3: "a", 4: "a", 5: "a", 6: "a",
                       7: "a", 8: "a", 9: "a"}

    def think(self, question):
        if self.memory[question] == "a":
            answer = np.random.randint(low=0, high=2)
        else:
            answer = self.memory[question]
        return answer


class SmartStudent(Student):

    def __init__(self, alpha=1, beta=1):
        self.v0 = np.random.random()
        self.v1 = 1 - self.v0
        self.alpha = alpha
        self.beta = beta
        self.answers = []
        super().__init__()

    def softmax(self, v0, v1=0.4, beta=1):
        """Softmax function as in https://hannekedenouden.ruhosting.nl/
        RLtutorial/html/SoftMax.html"""

        p0 = (math.exp(beta * self.v0)) / (math.exp(beta * self.v0) +
                                           math.exp(beta * self.v1))
        return p0

    def RW(self, v0, reward, alpha=1):
        """Rescorla-Wagner Model function as in https://hannekedenouden
        .ruhosting.nl/RLtutorial/html/RescorlaWagner.html"""

        v0 = v0 + alpha * (reward - v0)
        return v0

    def trial(self, p0):
        """Decides the answer using the probability value given by the softmax
        function"""

        if p0 > 0.5:
            answer = 0
        elif p0 < 0:
            answer = 1
        else:
            answer = np.random.randint(low=0, high=2)
        return answer

    def assess(self, teacher_vector, teacher_vector1, trialno):
        """Assigns a reward value based on which answer was chosen vs. the
        correct answer"""

        if self.answer == 0:
            reward = teacher_vector[trialno]
        elif self.answer == 1:
            reward = teacher_vector1[trialno]
        else:
            print("Error: answer must be 0 or 1")
        return reward

    def learn(self, teacher_vector, teacher_vector1):
        """Start the learning loop using tqdm to track progress"""

        with tqdm(total=100) as pbar:
            for i in range(0, teacher_vector.size):
                time.sleep(0.075)  # Wastes time for aesthetic reasons right now
                p0 = self.softmax(self.v0)
                self.answer = self.trial(p0)
                self.answers.append(self.answer)
                reward = self.assess(teacher_vector, teacher_vector1, i)
                self.v0 = self.RW(self.v0, reward)
                pbar.update(10)
        trialno = np.arange(0, teacher_vector.size, 1)
        plt.plot(trialno, self.answers, '+',
                 trialno, (teacher_vector/100), '-')
        plt.show()


if __name__ == "__main__":
    main = Main()
    main.reinforcement_learn()

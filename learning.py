#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import time
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


class Main:

    @staticmethod
    def reinforcement_learn():
        """Reinforcement learning using the Rescorla-Wagner model"""

        # np.random.seed(0)

        student0 = SmartStudent()
        teacher0 = Teacher()

        student0.learn(teacher0.reward_vector0, teacher0.reward_vector1)

    @staticmethod
    def stupid_learn():
        """Learning by random guessing"""

        np.random.seed(0)

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

    def __init__(self, sheet_size=10):

        """
        "Sheet" is a data structure similar to a multiple choice exam
        answer sheet in which a question is mapped to a correct answer.

        In order to assess which answers are correct from the human-readable
        answer sheet, reward vectors are defined as below:


        sheet = {"France": 1, "US": 0, "Spain": 1}

        Q1. US?
        Q2. France?
        Q3. US?
        Q4. US?
        Q5. ....

        reward_vector0 = 0, 1, 0
        reward_vector1 = 1, 0, 1
        """

        # sheet = {}
        # for k, v in zip(range(10), np.tile([0, 1], reps=10 // 2)):

        #     sheet[k] = v
        #
        #
        reply_series = np.tile([0, 1], reps=sheet_size//2)

        self.sheet = {k: v for k, v in zip(
            range(sheet_size),
            np.tile([0, 1], reps=sheet_size//2)
        )}
        # self.reward_vector0 = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
        # self.reward_vector1 = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

        assert list(np.unique(reply_series)) == [0, 1], "Any value can be " \
                                                        "only either 0 or 1"
        self.reward_vector1 = reply_series.copy()
        self.reward_vector0 = (reply_series - 1) * (-1)

    @staticmethod
    def ask():
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
        self.reward_vector = []
        self.cumulative_reward_vector = []
        super().__init__()

    def softmax(self, beta=1):
        """Softmax function as in https://hannekedenouden.ruhosting.nl/
        RLtutorial/html/SoftMax.html"""

        p0 = (math.exp(beta * self.v0)) / (math.exp(beta * self.v0) +
                                           math.exp(beta * self.v1))
        return p0

    def reward(self, reward, alpha=1):
        """Rescorla-Wagner Model function as in https://hannekedenouden
        .ruhosting.nl/RLtutorial/html/RescorlaWagner.html"""

        self.v0 += alpha * (reward - self.v0)
        return self.v0

    def trial(self, p0):
        """Decides the answer using the probability value given by the softmax
        function"""

        # if p0 > 0.5:
        #     answer = 0
        # elif p0 < 0:
        #     answer = 1
        # else:
        #     answer = np.random.randint(low=0, high=2)

        r = np.random.random()
        answer = int(p0 <= r)
        self.answers.append(answer)
        return answer

    def assess(self, teacher_vector, teacher_vector1, n_trial):
        """Assigns a reward value based on which answer was chosen vs. the
        correct answer"""

        answer = self.answers[-1]
        if answer == 0:
            reward = teacher_vector[n_trial]
        elif answer == 1:
            reward = teacher_vector1[n_trial]
        else:
            raise Exception("Error: answer must be 0 or 1")
        return reward

    def learn(self, teacher_vector, teacher_vector1):
        """Start the learning loop using tqdm to track progress"""

        # with tqdm(total=1) as pbar:
        for i in tqdm(range(0, teacher_vector.size)):
            time.sleep(0.075)  # Wastes time for aesthetic reasons right now
            p0 = self.softmax()
            # p0 = self.softmax(self.v0)
            self.trial(p0)
            # self.answer = self.trial(p0)
            # self.answers.append(self.answer)
            reward = self.assess(teacher_vector, teacher_vector1, i)
            self.reward_vector.append(reward)
            if not self.cumulative_reward_vector:
                self.cumulative_reward_vector.append(reward)
            else:
                self.cumulative_reward_vector\
                    .append(max(self.cumulative_reward_vector) + reward)
            self.v0 = self.reward(self.v0, reward)
            # pbar.update(10)

        # Answers per time step plot
        answers_plot = plt.figure(0)
        n_trial = np.arange(0, teacher_vector1.size, 1)
        plt.scatter(n_trial, teacher_vector1, label="Correct", marker="s",
                    alpha=0.5)
        plt.scatter(n_trial, self.answers, label="Student", marker=".")
        plt.title("Answers")
        plt.xlabel("Time")
        plt.ylabel("Reply")
        plt.yticks((0, 1))
        plt.legend()
        answers_plot.show()

        # Success per time step plot
        success_plot = plt.figure(1)
        plt.scatter(n_trial, self.reward_vector)
        plt.plot(n_trial, self.reward_vector, "--")
        plt.title("Success")
        plt.xlabel("Time")
        plt.ylabel("Reply")
        plt.yticks((0, 1))
        success_plot.show()

        # Cumulative success per time step plot
        cumulative_plot = plt.figure(2)
        plt.plot(n_trial, self.cumulative_reward_vector)
        plt.title("Cumulative success")
        plt.xlabel("Time")
        plt.ylabel("Cumulative correct answers")
        cumulative_plot.show()

        # Total accuracy plot
        accuracy_plot = plt.figure(3)
        labels = 'Success', 'Failure'
        sizes = [sum(self.reward_vector) / len(self.reward_vector),
                 1 - sum(self.reward_vector) / len(self.reward_vector)]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.title("Total accuracy")
        accuracy_plot.show()


if __name__ == "__main__":
    main = Main()
    main.reinforcement_learn()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 2019

@author: carlos de la torre
"""

import random

sheet = {1:1, 2:2, 3:3, 4:4, 5:1, 6:2, 7:3, 8:4}
memory = {}


def reset():
    memory = {1:"a", 2:"a", 3:"a", 4:"a", 5:"a", 6:"a", 7:"a", 8:"a"}
    return memory


class Teacher:

    def ask(self):
        question = random.randint(1, 8)
        return question
    
    def answer_check(self, question, answer):
        if answer == sheet[question]:
            memory[question] = answer
        else:
            pass


class Student:
    
    def think(self, question):
        if memory[question] == "a":
            answer = random.randint(1, 4)
        else:
            answer = memory[question]
        return answer
    
    def learn(self):
    
        epoch = 0
        
        print("training begins...")
        
        while "a" in memory.values():
            question = Teacher.ask(self)
            answer = self.think(question)
            Teacher.answer_check(self, question, answer)
            
            epoch += 1
            #print(memory) # Debugging
            print("epochs:", epoch)
            
        
        print("finished training")
        
        print(memory)


memory = reset()

student1 = Student()
student1.learn()


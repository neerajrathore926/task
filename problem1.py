#!/usr/bin/python3
from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
year = int((95-age) + datetime.now().year)

print ('Hey! %s. You are %s years old. You will turn 95 years old in that %s.' % (name, age, year))



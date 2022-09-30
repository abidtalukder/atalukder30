'''
TEAM JAW: William Vongphanith, Abid Talukder, Jonathan Song
SoftDev
K01 -- Choose
2022-09-22

DISCO
___________
- Instead of using the normal open, you can use the csv module to automatically parse the file.
- Each line in the file will be parsed such that each item that is delimited is string in a list
- You can use next(csv_reader) to skip the first line.
- Random.random() returns a float from 0 to 1 excluding 1. It is similar to Java
- 

QCC
___________
- We had an error because we named the file the same thing as the module we were importing.
    If you import csv, dont name your file csv.py

- 

OPS SUMMARY
___________

- To create the dictionary, we put the csv in a csv_reader object. Then, we could parse through each line that was parsed as a list of strings with 
the strings being each item that was separated by the comma. After that, we assigned the first value in the list(the job) with the next value 
the percentage.

- To choose the job with weighted percentage, we generated a number from 1 to 99. After that, we said that if the number was less than the percentage
of the job. It was a candidate that could be chosen. We created a list of candidates, then we chose a random job from there.


'''

import csv
import random


jobs = {} # used to have local access to the csv


# creates the dictionary
def createDict():
    with open('occupations.csv') as f:
        r = csv.reader(f)
        next(r)
        for line in r:
        
            jobs[line[0]] = float(line[1])


# Chooses a random job by percentage
def chooseJob():
    number = random.random() * 100

    possible_jobs = []

    for i in list(jobs.keys()):
        if number <= jobs[i]:
            possible_jobs.append(i)

    return random.choice(possible_jobs)

createDict()
print(chooseJob())



import csv
import random


jobs = {}

def createDict():
    with open('occupations.csv') as f:
        r = csv.reader(f)
        for line in r:
            if line[1] == "Percentage":
                continue
            jobs[line[0]] = float(line[1])

def chooseJob():
    number = random.random() * 100

    possible_jobs = []

    for i in list(jobs.keys()):
        if number <= jobs[i]:
            possible_jobs.append(i)

    return random.choice(possible_jobs)

createDict()
print(chooseJob())



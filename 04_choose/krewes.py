"""
TEAM JAW: William Vongphanith, Abid Talukder, Jonathan Song
SoftDev
K01 -- Choose
2022-09-22

DISCO
___________
- You can use the random module to generate random numbers (generate a number between 0 and 1 and multiply / add as needed)
- Or random.choice: chooses a random element from a list (so you don't have to do the random.randint(0, len(list) - 1) thing)
- You can use the list() function to convert a dictionary into a list of its keys

QCC
___________
- ...

OPS SUMMARY
___________
- Write demo code
- Write function to choose random devos
- main() function and __name__ == "__main__" stuff
- Get actual devos from the care package
"""

import random

krewes = {
        2: ["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
        7: ["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
        8: ["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
}

def chooseRandomDevo():
    teamKeyIndex = random.randint(0, len(krewes) - 1)
    teamKey = list(krewes.keys())[teamKeyIndex]
    teamMemberIndex = random.randint(0, len(krewes[teamKey]) - 1)
    teamMember = krewes[teamKey][teamMemberIndex]
    print("Team " + str(teamKey) + ": " + teamMember)

def main():
    chooseRandomDevo()

if __name__ == "__main__":
    main()

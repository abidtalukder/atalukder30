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
- You can use with open to choose how you want to open a file
- var.write() writes to file with a string as input
- var.read() reads in the entire file and returns a String
- with open, you can in the string "r" for read or "w" for write. However, if you are reading

QCC
___________
- ...

OPS SUMMARY
___________
- Write demo code
- Write function to choose random devos
- main() function and __name__ == "__main__" stuff
- Get actual devos from the care package
- To choose a random person from a random period. To get a random period, we choose a random number from 0 to 2, which we apply to a list 
  keys. After that, we choose a random number for the team member. This random number is chosen by getting from 0 to the length of the list assigned to the period key chosen.
  After that, we just select the random key to get a list, and we select the person from the list index.
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

def writeToFile():
    with open("krewes.txt", "w") as f:
        
        for i in range(3):
            period = list(krewes.keys())[i]

            for j in range(len(krewes[period])):
                f.write(f"{period}$$${krewes[period][j]}$$$BEN")

                if j != len(krewes[period]) -1:
                    f.write("@@@")

    f.close()


def chooseNewDevo():
    with open("krewes.txt") as f:
        txt = f.read()
        txt = txt.split("@@@")

        krewes  = {
            2:[],
            7:[],
            8:[],
        }

        for i in range(len(txt)):
            person = txt[i]
            person = person.split("$$$")


            krewes[int(person[0])].append([person[1],person[2]])

        period = random.choice(list(krewes.keys()))

        person = random.choice(krewes[period])

        print(f"{period} : {person[0]} : {person[1]}")

    f.close()

def main():
    #chooseRandomDevo()
    writeToFile()
    chooseNewDevo()

if __name__ == "__main__":
    main()

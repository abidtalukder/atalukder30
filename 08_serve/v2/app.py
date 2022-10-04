'''
TEAM JAW: William Vongphanith, Abid Talukder, Jonathan Song
SoftDev
K01 -- Choose
2022-10-03
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. We have seen this in Java because it seems that Flask is an object that is being constructed and set to the variable app.
1. We believe that the slash is representative of the root directory of where app.py is being stored. We think this because
   the slash is oftne used to change between directories.
2. We think that will print to the console.
3. We think that this might print the name of the file, or the name of the CPU process that is running this python program.
4. We know that Flask is a web tool so we think that this will open up an HTML page with the return text. We can know this from prior knowledge
   or what Flask even is, and also by running the program.
5. We have seen these constructs in java where the object has a method running by it.
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>

We looked up the Flask documentation and we saw that Flask is used for building web apps. We hypothesized many of our answers just by this simple fact.
We also ran the program to see what it did. This way we can test by changing simple parts of the program such as the return text.


'''
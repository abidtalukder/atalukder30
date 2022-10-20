# TEAM AC: Abid Talukder, Craig Chen
# SoftDev
# K12 -- FlASK-FORMS
# 2022-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    # reqstr = str(request)
    # if reqstr.find("GET") != -1:
    #     reqstr = "GET"
    # else:
    #     reqstr = "POST"
    
    
    # return f'Welcome to the Interweb, {request.form["username"]} <br><br> Your Request Method: ' + reqstr + f'<br><br> We Hope You Love This Website <br><br> '  #response to a form submission
    if request.method == 'POST':
        username = request.form.get('username')
        sub1 = request.form.get('sub1')
        return '''
                <h1>Welcome to the Interwebs</h1>
                
                  <h1> User: {}</h1>
                  <h1>Your Request Method: POST</h1>
                  
                  <h1>The Differences Between the GET and Post Methods</h1>
                  
                  Both GET and POST are used to send and receive data from a server using the HTTP protocol, but a major difference between the two is that data using the GET method is sent through URL strings that are appended to the URL. On the other hand, data with the POST method is sent enclosed in the message body so it is more secure in that the data isn't exposed in the URL so a typical user can't see it.
                  <br>
                  Another difference is that POST can send larger amounts of data than GET can.
                  <br>
                  <br>
                  A third difference is that GET requests are cached while POST requests aren't. When I got POST requests to work with my flask app, everytime I reloaded the page, the browser would ask if I wanted to resubmit the data. This means that with every reload the browser must generate input and output and do the calculations again.
                  <br>
                  <br>
                  When using GET and POST in our Flask app, we noticed the following differences:
                  <ul>
                  
                  <li>The POST request had the message Content-Type: application/x-www-form-urlencoded in the request headers and the request args were not shown. I believe that the Content-Type message is to show that the data is secured in the request message body instead of the request headers or args. </li>
                  <li> When actually handling GET and POST data, we saw that we had to use request.args() for GET and request.form() for POST. To handle which one to use, it was crucial that used if statements to difference what type of request method was actually being used. Otherwise, we would run into errors if we used something like request.form() for the GET method.                  
                  </ul>
                  
                  
                  '''.format(username, sub1)
                  
                
        
        return '''
           <form method = "POST">
             <input type="text" name="username">
            <input type="submit" name="sub1">
            </form>    '''    
                  
# request.args["username"]

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

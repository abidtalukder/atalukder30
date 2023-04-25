/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN
   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //AYO appears in console as expected

var i = "hello"; //this is unused. Why is this here?
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
//objects are a collection of properties (key-value pairs). So objects are python dictionaries
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//looks for an element in the DOM with id "thelist". Creates a list element and inserts the given text into the list. 
//Then parents the new list element to the element with id "thelist". Result is probably <li> text <li>
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

var addFib = function(text) {
  var list = document.getElementById("fiblist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

var addfact = function(text) {
  var list = document.getElementById("factlist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

var gcdFib = function(text) {
  var list = document.getElementById("gcdlist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

addItem("my item") //adds "my item" to the list
addItem(o) //adds [object Object] probably because o is not a string. [object Object] is probably the def string representation of an object
addItem(o["name"]) //adds Thluffy
addItem(o["func"](10)) //adds 40. Numbers get auto converted to strings or numbers can just be displayed no problem
addItem(o["items"]) //Adds the whole list
addItem(o["morestuff"]) //[object Object] as expected

//removes item by index. But this doesn't search for the list with id "thelist" so this just gets all list items
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

removeItem(0) //removes the first list element, which is now "the hidden text" after we changed index.html
removeItem(0) //removes item 0

//adds red to the class name of every list. Does not turn every item red because red is lost priority
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

red() //makes all added items red because the added items have no class to override red

//makes even numbered list elements red, and odd numbered elements blue
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

stripe() //The stripe will only work on the added elements because blue is present in all the others, which will override red

//insert your implementations here for...
// factorial
function fact(a) {
    if (a === 0) {
      return 1;
    } 
    return a * fact(a - 1); // same algorithm from scheme ported to JS
  
  }
  
//fibonacci
function fib(n) {
    if (n === 0) { // return 0, if u are looking for the 0th number in the sequence
    return 0;
    } else if (n === 1) { // 1 if the 1st number
    return 1;
    }
    return fib(n - 1) + fib(n - 2); // every other number is the sum of the previous two numbers in fib sequence
}

// GCD
function gcd(a,b) {
    var c = 1;

    if (a > b){
        c=b;
        b=a;
        a=c;
    }

    if (a===0) {return b;}

    return gcd(b%a,a);
}

addItem("skdljflksdjf") //24
addItem(1293329472398472) //13
addItem(gcd(51, 27)) //3
addItem("hello")
//addFib("hello")
// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  retVal = param1 * param2
  console.log(retVal)
  return retVal;
};

// FIB BUTTONs
var fb = document.getElementById("fibbutton")
fibbutton.addEventListener('click', fibaction)
//addFib("works up to here")

function fibaction() {
  var ans = document.createElement("li")
  //ans.innerHTML = fib(Number(document.getElementById('fibinput').getAttribute()))
  ans.innerHTML= document.getElementById('fibinput').value + ": " + fib(Number(document.getElementById('fibinput').value))
  document.getElementById("fiblist").appendChild(ans)
  //addFib(fib(10))
}

var fb = document.getElementById("factbutton")
fibbutton.addEventListener('click', fibaction)
//addFib("works up to here")

function fibaction() {
  var ans = document.createElement("li")
  //ans.innerHTML = fib(Number(document.getElementById('fibinput').getAttribute()))
  ans.innerHTML= document.getElementById('factinput').value + ": " + fact(Number(document.getElementById('factinput').value))
  document.getElementById("factlist").appendChild(ans)
  //addFib(fib(10))
}

var fb = document.getElementById("gcdbutton")
fibbutton.addEventListener('click', fibaction)
//addFib("works up to here")

function fibaction() {
  var ans = document.createElement("li")
  //ans.innerHTML = fib(Number(document.getElementById('fibinput').getAttribute()))
  ans.innerHTML= document.getElementById('gcdinput').value + ": " + gcd(Number(document.getElementById('gcdinput').value))
  document.getElementById("gcdlist").appendChild(ans)
  //addFib(fib(10))
}


//myFxn = (2, 3) //Error in console says "caught TypeError: Assignment to constant variable."
console.log(myFxn) //This logs the entire function. The code within is shown in console
 
// addItem(myFxn) //The parameters and body of the myFxn function is added to the list
// addItem(fib) //Logs 6 in console and also adds 6 to the list
// addItem(fact)

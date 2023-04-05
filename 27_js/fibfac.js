// Team It's Up to You :: Kevin Li, Abid Talukder
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-03t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

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

console.log(fib(5))
  
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

// linking to HTML elements

const fact1 = document.getElementById("fact1");
const fact2 = document.getElementById("fact2");
const fact3 = document.getElementById("fact3");
const fact4 = document.getElementById("fact4");
const fact5 = document.getElementById("fact5");

// huh u can change properties. text property is display
fact1.textContent = fact(1);
fact2.textContent = fact(2);
fact3.textContent = fact(3);
fact4.textContent = fact(4);
fact5.textContent = fact(5);


// doing same thing for fib
var fib1 = document.getElementById("fib1");
const fib2 = document.getElementById("fib2");
const fib3 = document.getElementById("fib3");
const fib4 = document.getElementById("fib4");
const fib5 = document.getElementById("fib5");

fib1.textContent = fib(1);
fib2.textContent = fib(2);
fib3.textContent = fib(3);
fib4.textContent = fib(4);
fib5.textContent = fib(5);
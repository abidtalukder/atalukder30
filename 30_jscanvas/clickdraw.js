//retrieve node in DOM via ID
var c = document.getElementById("slate");
//console.log(c)

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");
ctx.fillStyle = "red"

//init globar state var
var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
        bToggler.innerHTML = "circ"
    }
    else {
        mode = "rect"
        bToggler.innerHTML = "rect"
    }
}

var drawRect = function(e) {
    //clientX gives coordinates relative to the viewport you're interacting with. This is the same as pageX if the viewport is the page
    //pageX is relative to the page (so excluding bookmarks bar, taskbar, etc). 
    //screenX is relative to your entire screen
    //offsetX is relative to the node you're interacting with

    var mouseX = e.offsetX //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY //gets Y-coor of mouse when event is fired
    //console.log("received mouse coordinates from ", e)
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillRect(mouseX, mouseY, 80, 160)
}

var drawCircle = function(e) {
    var mouseX = e.offsetX 
    var mouseY = e.offsetY 
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.beginPath() //places pen down
    path = ctx.arc(mouseX, mouseY, 40, 0, 2 * Math.PI) //moves pen
    ctx.stroke() //shows result
    ctx.fill(path) //fills in the result
}

var draw = function(e) {
    if (mode === "rect") {
        drawRect(e)
    }
    if (mode === "circ") {
        drawCircle(e)
    }
}

var wipeCanvas = function(e) {
    ctx.clearRect(0, 0, c.width, c.height)
}

var bToggler = document.getElementById("buttonToggle")
bToggler.addEventListener("click", toggleMode)

var clearB = document.getElementById("buttonClear")
clearB.addEventListener("click", wipeCanvas)

c.addEventListener("click", draw) //passes the mouse event as parameter for the function
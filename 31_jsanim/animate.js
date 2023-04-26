var c = document.getElementById("playground") // GET CANVAS
var dotButton = document.getElementById("buttonCircle")
var stopButton = document.getElementById("buttonStop") //get stop button

var ctx = c.getContext("2d") // Your code

ctx.fillStyle = "red"

var width = c.width
var height = c.height

var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,c.width,c.height)
};

var radius = 0;
var growing = true;
var radius = 10;
var stopAnimation = false;
var isDrawing = false;


var drawCircle = function(e) {
    if (growing) {
        if (radius + 1 > height/2){
            radius = height/2
            growing = false
        } else if (radius === height/2) {
            radius -= 1
            growing = false
        } else {
            radius += 1
        }
    } else {
        if (radius - 1 < 10) {
            radius = 10
            growing = true;
        } else if (radius === 10) {
            growing = true;
            radius += 1;
        } else {
            radius -= 1;
        } 
    }
    
    
    //var mouseX = e.offsetX 
    //var mouseY = e.offsetY
    console.log("drawCircle")
    ctx.beginPath() //places pen down
    path = ctx.arc(width/2, height/2, radius, 0, 2 * Math.PI) //moves pen
    ctx.stroke() //shows result
    ctx.fill(path) //fills in the result
};

var dotListener = true;

var drawDot = () => {
    dotButton.removeEventListener("click", drawDot); // you cant click this again once you already clicked it
    dotListener = false
    
    //console.log(requestID-Date.now())
    //stopAnimation = false
    //cancelAnimationFrame(drawDot)
    clear()
    drawCircle()
    if (!stopAnimation) {
        requestAnimationFrame(drawDot)
    } else {
        stopAnimation = false;
        dotButton.addEventListener("click", drawDot);
        dotListener = true
        
    }
    
    /*
        Wipe the canvas
        Repaint the circle,
    */
};

//var stopIt = function ( ) ‹
var stopIt = () => {
    console.log("stopIt invoked..");
    console.log ( requestID );
    stopAnimation = true;    
    stopButton.removeEventListener( "click", stopIt);
    /*YOUR CODE HERE
    •to stop the animation
    You will need window. cancelAnimationFrame ()
    */
};

var change = () => {
    if (dotListener) {
        stopButton.removeEventListener( "click", stopIt); 
    } else {
        stopButton.addEventListener( "click", stopIt);
        stopIt()
    }
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener( "click", stopIt);
stopButton.addEventListener( "click", change);

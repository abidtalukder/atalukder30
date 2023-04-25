var c = document.getElementById("playground") // GET CANVAS
var dotButton = document.getElementById("buttonCircle")
var stopButton = document.getElementById("buttonStop") //get stop button

// Event listeners



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

var drawCircle = function(e) {
    if (growing) {
        if (radius + 5 > height/2){
            radius = height/2
            growing = false
        } else if (radius === height/2) {
            radius -= 5
            growing = false
        } else {
            radius += 5
        }
    } else {
        if (radius - 5 < 10) {
            radius = 10
            growing = true;
        } else if (radius === 10) {
            growing = true;
            radius += 5;
        } else {
            radius -= 5;
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



var drawDot = () => {
    
    
    //drawCircle()
    clear()
    
    /*
        Wipe the canvas
        Repaint the circle,
        
    
    */
   window.requestAnimationFrame(drawCircle)
    
    
};

dotButton.addEventListener("click", drawDot);

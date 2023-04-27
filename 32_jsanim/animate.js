var c = document.getElementById("playground");
var dotbutton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("buttonDvd");
var stopbutton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
ctx.fillStyle = "blue"
var requestID;

var cwidth = c.width
var cheight = c.height

var requestID;

var random = (a,b) => {
    return a + Math.random() * (b - a);
}

var clear = (e) => {
    //e.preventDefault(); // what does this do?
    ctx.clearRect(0, 0, c.width, c.height)
};

var dvdLogoSetup = function () {
    cancelAnimationFrame(requestID);
    var rectWidth = 150
    var rectHeight = 100
    
    var rectX = random(0,cwidth - rectWidth) 
    var rectY = random(0,cheight - rectHeight)
    
    var xVel = 1
    var yVel = 1
    
    var logo = new Image();
    logo.src = "logo_dvd.jpg";
    
    var dvdLogo = function() {
      ctx.clearRect(0,0,c.width,c.height)
      ctx.drawImage(logo,rectX,rectY,rectWidth,rectHeight)
      // Movement and Changing positions
      if (rectX+rectWidth>=cwidth){
        //rectX=cwidth-1
        xVel = -xVel
        console.log("hit edge at x = ", rectX + rectWidth)
      }
      
      if (rectX <= 0) {
        xVel = -xVel
        console.log("hit edge at x = ", rectX)
      }
      
      if (rectY+rectHeight>=cheight){
        //rectY = cheight-1
        yVel = -yVel
        console.log("hit edge at y = ", rectY + rectHeight)
      }
      
      if (rectY <= 0) {
        yVel = -yVel
        console.log("hit edge at y = ", rectY)
      }
      
      rectX += xVel
      rectY += yVel

      // drawRect(rectX, rectY, rectWidth, rectHeight)
      requestID = requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};

var drawRect = (x, y, w, h) => {
    ctx.beginPath()
    ctx.rect(x,y,w,h)
    ctx.stroke()
}

var radius = 0;
var growing = true;

var drawDot = () => {
    stopIt() //stops current animation
    requestID = window.requestAnimationFrame(drawDot) //starts a new animation
    clear() //clear canvas
    drawCircle() //draw image
    if (growing) {
        radius += 1
        if (radius > c.width / 2) {
            growing = false
        }
    } else {
        radius -= 1
        if (radius <= 0) {
            growing = true
        }
    }
}

var drawCircle = () => {
    var x = c.width / 2
    var y = c.height / 2
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, 2 * Math.PI)
    ctx.stroke()
    ctx.fill()
}

var stopIt = () => {
    window.cancelAnimationFrame(requestID) //cancel current animation
}

dotbutton.addEventListener("click", drawDot)
stopbutton.addEventListener("click", stopIt)
dvdButton.addEventListener("click", dvdLogoSetup)
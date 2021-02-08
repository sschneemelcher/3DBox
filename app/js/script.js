function drawLines(coordinates) {
	var c = document.getElementById("myCanvas");
	var ctx = c.getContext("2d");
	ctx.strokeStyle = "green";
	ctx.lineWidth = 5;
	ctx.beginPath();
	ctx.clearRect(0, 0, c.width, c.height);
	coordinates.forEach(function(current) {
		ctx.moveTo(current[0], current[1]);
		ctx.lineTo(current[2], current[3]);
		ctx.stroke();
		});
	}
eel.expose(drawLines);

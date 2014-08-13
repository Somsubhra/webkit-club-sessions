// All variable declarations
var apiRoot = "http://localhost:8080/api";

var overs = 10;

var ctx = document.getElementById("score-chart").getContext("2d");
ctx.canvas.width  = window.innerWidth;
ctx.canvas.height = window.innerHeight;

var optionsNoAnimation = {animation : false}

var scoreChart = new Chart(ctx);

var labels = [];

var graphData = {
	
	labels: labels,	

	datasets : [
		{
			fillColor : "rgba(220, 220, 220, 0.5)",
			strokeColor : "rgba(220, 220, 220, 1)",
			pointColor : "rgba(220, 220, 220, 1)",
			pointStrokeColor : "#fff",
			data : []
		},
		{
			fillColor : "rgba(151, 187, 205, 0.5)",
			strokeColor : "rgba(151, 187, 205, 1)",
			pointColor : "rgba(151, 187, 205, 1)",
			pointStrokeColor : "#fff",
			data : []
		}
	]
}; 

for(var i = 1; i <= overs; i++) {
	labels.push(i.toString());
	graphData.datasets[0].data[i] = 0;
	graphData.datasets[1].data[i] = 0;
}

// The callback function called repititively to fetch scores
function fetchScores() {
	$.getJSON(apiRoot, function(data) {

		for(var i = 0; i < data[0].runs.length; i++) {
			graphData.datasets[0].data[i] = data[0].runs[i];
		}

		for(var i = 0; i < data[1].runs.length; i++) {
			graphData.datasets[1].data[i] = data[1].runs[i];
		}

		scoreChart.Line(graphData, optionsNoAnimation);
	});
}

// The main function
$(function() {
	setInterval(fetchScores, 1000);
	scoreChart.Line(graphData, optionsNoAnimation);
});
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

for(var i = 1 ; i <= overs ; i++) {
	labels.push(i.toString());
	graphData.datasets[0].data[i] = 0;
	graphData.datasets[1].data[i] = 0;
}

// The callback function called repititively to fetch scores
function fetchScores() {
	$.getJSON(apiRoot, function(data) {

		graphData.datasets[0].data[data[0].overs] = data[0].runs;
		graphData.datasets[1].data[data[1].overs] = data[1].runs;

		scoreChart.Line(graphData, optionsNoAnimation);
	});
}

// The main function
$(function() {
	setInterval(fetchScores, 1000);
	scoreChart.Line(graphData, optionsNoAnimation);
});
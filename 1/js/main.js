var apiRoot = "http://localhost:8080/api";

function fetchScores() {
	$.getJSON(apiRoot, function(data) {
		console.log(data[0].name + ":" + data[0].runs);
		console.log(data[1].name + ":" + data[1].runs);
	});
}

$(function() {
	setInterval(fetchScores, 1000);
});
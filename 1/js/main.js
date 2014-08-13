var apiRoot = "http://localhost:8080"

$(function() {
	$.getJSON(apiRoot, function(data) {
		console.log(data);
	})
});
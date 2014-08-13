var apiRoot = "http://localhost:8080/api";

$(function() {
	$.getJSON(apiRoot, function(data) {
		console.log(data);
	})
});
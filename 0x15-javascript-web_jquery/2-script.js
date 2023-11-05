//change header element to red when user clicks on tag
$(document).ready(function() {
	let redHeader = $("#red_header");
	redHeader.click(function() {
		let header = $("header");
		header.css("color", "#FF0000");
	});
});

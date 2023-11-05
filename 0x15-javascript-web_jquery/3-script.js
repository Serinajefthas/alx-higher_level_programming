//adds class red to header element when user clicks on tag
$(document).ready(function() {
        let redHeader = $("#red_header");
        redHeader.click(function() {
		$("header").addClass("red");
        });
});

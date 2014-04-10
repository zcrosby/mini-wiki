$(function() {


/*------BEGIN  role.html functionality--------------------------------*/

	var menu = $("#menu li");

	menu.each(function(index) {
		var link = $(this).children("a");

		link.click(function(event) {
			event.preventDefault();
			var href = $(this).attr("href");

			$.ajax({
				url: href,
				success: function(data) {
					$('#info').html(data);
				}
			});//end ajax

		});//end click event

	});//end each callback

/*------END role.html functionality-----------------------------------*/

});//end doc.read

$(document).ready(function() {
	$(function(){

		$('a').each(function(){
			var hr = $(this).prop('href')
			if (hr === window.location.href) {
				console.log($(this).prop('href'))
				console.log(window.location.href)
				$(this).addClass('active-page');
				$(this).parents('li').addClass('active-page');
			}
			else if (hr + "/" === window.location.href) {
				console.log($(this).prop('href'))
				console.log(window.location.href)
				$(this).addClass('active-page');
				$(this).parents('li').addClass('active-page');
			}
		});
	});


	$(".nav_ico").click(function(){
		$(".main_nav").toggleClass("active");
	});
	$(".main_nav").click(function(){
		$(this).removeClass("active");
	});
	$( ".main_nav ul" ).click(function( event ) {
		event.stopImmediatePropagation();
	});
});


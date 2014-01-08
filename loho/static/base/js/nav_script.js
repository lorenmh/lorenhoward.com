$(document).ready(function(){

/*old color: rgb(155,175,255'}*/

$('.menu_toggle').click(function(e){
	$('.nav').toggleClass('show')
});

var isMobile = (/android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(navigator.userAgent.toLowerCase()));

if(isMobile){
	$('.nav_menu_item').not('.current').click(function(){
		$(this).css({backgroundColor: 'rgb(216, 225, 231)', color: 'rgb(45,65,80)'});
		$('.current').css({backgroundColor: 'rgb(45,65,80)', color: 'rgb(216, 225, 231)'});
	});
}

if (!isMobile){
var click = false;

	$('.nav_menu_item').not('.current', '.nav_transition').hover(
		function(){	
			$(this).stop()	.animate({backgroundColor: 'rgb(216, 225, 231)'}, {queue: false, duration: 400, easing: 'easeOutQuart'})
							.animate({color: 'rgb(45,65,80)'},200, 'easeOutQuart');
			$('.current').stop().animate({backgroundColor: 'rgb(186,195,201)'},1000,'easeOutQuart');
		},
	    function(){	
	    	if (!$(this).hasClass('.nav_transition'))
	    	{
		    	$(this).stop()	.animate({backgroundColor: 'rgb(45,65,80)'}, {queue: false, duration:400, easing: 'easeOutQuart'})
		    					.animate({color: 'rgb(216, 225, 231)'},200, 'easeOutQuart');
				$('.current').stop().animate({backgroundColor: 'rgb(216, 225, 231)'},400,'easeOutQuart');
			}
	});

	$('.nav_menu_item').not('.current').click(
		function(){
			click = true;
			$(this).addClass('.nav_transition');
			$(this).css({backgroundColor: 'rgb(216, 225, 231)'});
		});

}

});
$(document).ready(function(){

	var pros = 0;
	var cons = 0;

	// Item remove
	$(document).on('click','.item', function(){
		if($(this).hasClass('pros-item')) {
			pros--;
		} else {
			cons--;
		}
		$(this).remove();
	});

	$(document).keyup(function(e) {
		if (e.keyCode == 27) {
			console.log("PRESSED");
			if($('#summary-modal').hasClass('fadedown')) {
				$('#summary-close').trigger('click');
			}
		}
	});

	function regraph(proswidth, conswidth) {
			var p = 0;
			var c = 0;
		if(proswidth != 0 || conswidth != 0) {
			p = (proswidth / (proswidth + conswidth)) * 100;
			c = (conswidth / (proswidth + conswidth)) * 100;
		}

		$('.bar.pros-bar').width(p + "%");
		$('.bar.cons-bar').width(c + "%");

		$('.bar.pros-bar').text(p +"%");
		$('.bar.cons-bar').text(c +"%");
	}

	// Item add
	$('.adds').keypress(function(e) {
		if($(this).val().length == 0) {
			return;
		}
		if(e.which == 13) {
			if($(this).attr('id') == 'pros-add') {
				$('#pros-list').append('<div class="item pros-item">' + $(this).val() + '</div>');
				$(this).val('');
				pros++;
			} else {
				$('#cons-list').append('<div class="item cons-item">' + $(this).val() + '</div>');
				$(this).val('');
				cons++;
			}
		}
	});

	$('#summary-close').on('click', function() {
		$('#summary-modal').toggleClass('fadeoutdown').removeClass('fadedown');
		$('#overlay').fadeOut();
	});

	$('#summary').on('click', function(){
		regraph(pros, cons);
		$('#summary-modal').removeClass('fadeoutdown').toggleClass('fadedown');
		$('#overlay').fadeIn();
	});

	var last = 0;

	$('#tiles').click(function() {
		$('.inner-tile').toggleClass('tile-invert');
		if(last == 0) {
			$('.alive .page-container').hide();
			$('.alive').animate({'width': '450px', 'height': '675px'}, function(){
				$(this).removeClass('alive').addClass('tiled').addClass('last-alive');
			});
			$('body').css({'padding': '20px'});
			last = 1;
		} else {
			$('.last-alive').removeClass('tiled').addClass('alive').removeClass('last-alive').animate({'width': window.innerWidth, 'height': 'auto'}, function(){
				$('.alive .page-container').fadeIn();
			});
			$('body').css({'padding': '0px'});
			last = 0;
		}
	});


	$(document).on('click', '.tiled', function(){
		$('.last-active').removeClass('last-active');
		$(this).addClass('.last-active');
		$('#tiles').trigger('click');
	});
});

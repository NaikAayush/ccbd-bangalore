/*
Theme Name: Minel
Description: Minimal Site Template
Author: Erilisdesign
Theme URI: http://erilisdesign.com/preview/themeforest/html/minel/
Author URI: http://themeforest.net/user/erilisdesign
Version: 1.0
License: https://themeforest.net/licenses/standard
*/

(function($) {
	"use strict";

	// Vars
	var body = $('body'),
		animated = $('.animated'),
		headerNav = $('nav.header-nav'),
		headerNavElem = $('nav.header-nav li'),
		headerNavElemHome = $('nav.header-nav li a[href="#home"]'),
		navToggle = $('.nav-toggle'),
		EDHomeBlock = $('div.ed-homeblock'),
		EDSideBlock = $('div.ed-sideblock'),
		target,
		preloader = $('#preloader'),
		preloaderDelay = 350,
		preloaderFadeOutTime = 800,
		btnLoadContent = $('a.load-content'),
		countdown = $('.countdown[data-countdown]');


	// Mobile
	if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
		body.addClass('mobile');
	}

	function detectIE() {
		if (navigator.userAgent.indexOf('MSIE') != -1)
			var detectIEregexp = /MSIE (\d+\.\d+);/ // test for MSIE x.x
		else // if no "MSIE" string in userAgent
			var detectIEregexp = /Trident.*rv[ :]*(\d+\.\d+)/ // test for rv:x.x or rv x.x where Trident string exists

		if (detectIEregexp.test(navigator.userAgent)){ // if some form of IE
			var ieversion=new Number(RegExp.$1) // capture x.x portion and store as a number
			if (ieversion >= 9) {
				return true;
			}
		}
		return false;
	}

	function getWindowWidth() {
		return Math.max( $(window).width(), window.innerWidth);
	}

	function getWindowHeight() {
		return Math.max( $(window).height(), window.innerHeight);
	}

	// Preloader
	function init_ED_Preloader() {

		// Hide Preloader
		preloader.delay(preloaderDelay).fadeOut(preloaderFadeOutTime);

	}


	// Animations
	function init_ED_Animations() {
		if( !body.hasClass('mobile') ) {
			if( detectIE() ) {
				animated.css({
					'display':'block',
					'visibility':'visible'
				});
			} else {
				/* Starting Animation on Load */
				$('.onstart').each( function() {
					var elem = $(this);
					if ( !elem.hasClass('visible') ) {
						var animationDelay = elem.data('animation-delay');
						var animation = elem.data('animation');
						if ( animationDelay ) {
							setTimeout(function(){
								elem.addClass( animation + " visible" );
							}, animationDelay);
						} else {
							elem.addClass( animation + " visible" );
						}
					}
				});
			}
		}
	}
	

	//	Backgrounds
	function init_ED_PageBackground() {
		
		// Slideshow Background
		if (body.hasClass('slideshow-background')) {
			body.vegas({
				preload: true,
				timer: false,
				delay: 5000,
				transition: 'fade',
				transitionDuration: 1000,
				slides: [
					{ src: 'demo/images/image-12.jpg' },
					{ src: 'demo/images/image-2.jpg' },
					{ src: 'demo/images/image-3.jpg' },
					{ src: 'demo/images/image-4.jpg' }
				]
			});
		}
		
		// Slideshow Background - ZoomOut
		if (body.hasClass('slideshow-zoom-background')) {
			body.vegas({
				preload: true,
				timer: false,
				delay: 7000,
				transition: 'zoomOut',
				transitionDuration: 4000,
				slides: [
					{ src: 'demo/images/image-12.jpg' },
					{ src: 'demo/images/image-2.jpg' },
					{ src: 'demo/images/image-3.jpg' },
					{ src: 'demo/images/image-4.jpg' }
				]
			});
		}

		// Slideshow & Video Background
		if (body.hasClass('slideshow-video-background')) {
			body.vegas({
				preload: true,
				timer: false,
				delay: 5000,
				transition: 'fade',
				transitionDuration: 1000,
				slides: [
					{ src: 'demo/images/image-2.jpg' },
					{ src: 'demo/video/marine.jpg',
						video: {
							src: [
								'demo/video/marine.mp4',
								'demo/video/marine.webm',
								'demo/video/marine.ogv'
							],
							loop: false,
							mute: true
						}
					},
					{ src: 'demo/images/image-3.jpg' },
					{ src: 'demo/images/image-4.jpg' },
					{ src: 'demo/images/image-12.jpg' }
				]
			});
		}

		// Kenburns Background
		if (body.hasClass('kenburns-background')) {

			var kenburnsDisplayBackdrops = false;
			var kenburnsBackgrounds = [
				{ src: 'demo/images/image-2.jpg', valign: 'top' },
				{ src: 'demo/images/image-3.jpg', valign: 'top' },
				{ src: 'demo/images/image-9.jpg', valign: 'top' },
				{ src: 'demo/images/image-10.jpg', valign: 'top' }
			];

			body.vegas({
				preload: true,
				transition: 'swirlLeft2',
				transitionDuration: 4000,
				timer: false,
				delay: 10000,
				slides: kenburnsBackgrounds,
				walk: function (nb) {
					if (kenburnsDisplayBackdrops === true) {
						var backdrop;

						backdrop = backdrops[nb];
						backdrop.animation  = 'kenburns';
						backdrop.animationDuration = 20000;
						backdrop.transition = 'fade';
						backdrop.transitionDuration = 1000;

						body
							.vegas('options', 'slides', [ backdrop ])
							.vegas('next');
					}
				}
			});
		}

		// Youtube Video Background
		if ($('#youtube-background').length > 0) {
			var videos = [
				{videoURL: "0pXYp72dwl0", showControls:false, containment:'.overlay-video',autoPlay:true, mute:false, startAt:0,opacity:1, loop:false, showYTLogo:false, realfullscreen: true, addRaster:true}
			];

			$('.player').YTPlaylist(videos, true);
		}
		
		// Youtube Multiple Video Background
		if ($('#youtube-multiple-background').length > 0) {
			
			var videos = [
				{videoURL: "0pXYp72dwl0", showControls:false, containment:'.overlay-video',autoPlay:true, mute:true, startAt:0,opacity:1, loop:false, showYTLogo:false, realfullscreen: true, addRaster:true},
				{videoURL: "9d8wWcJLnFI", showControls:false, containment:'.overlay-video',autoPlay:true, mute:true, startAt:20,opacity:1, loop:false, showYTLogo:false, realfullscreen: true, addRaster:false},
				{videoURL: "nam90gorcPs", showControls:false, containment:'.overlay-video',autoPlay:true, mute:true, startAt:20,opacity:1, loop:false, showYTLogo:false, realfullscreen: true, addRaster:true}
			];

			$('.player').YTPlaylist(videos, true);
			
		}
		
		if(body.hasClass('mobile')) {
			$('.video-wrapper, .player').css('display', 'none');	
		}
		
		// GMap Background
		if($('#gmap-background').length){
			
			var map = new GMaps({
				div: '#gmap-background',
				lat: 37.752797,
				lng: -122.409132,
				zoom: 14,
				scrollwheel: false
			});
			
			map.addMarker({
				lat: 37.752797,
				lng: -122.409132
			});
			
		}
		
		// Parallax Background - only right side
		body.on('scroll resize', function() {
			if(!body.hasClass('mobile')){
				init_ED_Parallax();
			}
		});

	}
	
	
	// Parallax Background
	function init_ED_Parallax(el) {
		var windowHeight = window.innerHeight || document.documentElement.clientHeight,
			scrollTop = el.mcs.top,
			bottomWindow = scrollTop + windowHeight,
			speedDivider = 0.25;
		
		$('.parallax-background').each(function() {
			var parallaxElement = $(this),
				parallaxHeight = parallaxElement.outerHeight(),
				parallaxTop = parallaxElement.offset().top,
				parallaxBottom = parallaxTop + parallaxHeight,
				parallaxWrapper = parallaxElement.parents('.parallax-wrapper'),
				
				section = parallaxElement.parents('section'),
				sectionHeight = parallaxElement.parents('section').outerHeight(),
				offSetTop = scrollTop + section[0].getBoundingClientRect().top,
				offSetPosition = windowHeight + scrollTop - offSetTop;
				
			if (offSetPosition > 0 && offSetPosition < (sectionHeight + windowHeight)) {
				var value = ((offSetPosition - windowHeight) * speedDivider);

				if (Math.abs(value) < (parallaxHeight - sectionHeight)) {
					parallaxElement.css({
						"transform" : "translate3d(0px, " + value + "px, 0px)",
						"-webkit-transform" : "translate3d(0px, " + value + "px, 0px)"
					});
				} else {
					parallaxElement.css({
						"transform" : "translate3d(0px, " + parallaxHeight - sectionHeight + "px, 0px)",
						"-webkit-transform" : "translate3d(0px, " + parallaxHeight - sectionHeight + "px, 0px)"
					});
				}
			}
		});
	}
	
	
	// Fullscreen Sections Fix
	function init_ED_FullscreenFix() {		
		if(!(1024 >= getWindowWidth() || body.hasClass('mobile'))) {
			$('.section.fullscreen-element').each(function(){
				var elem = $(this),
					elemHeight = getWindowHeight(),
					elemContent = elem.find('.table-container'),
					elemContentHeight = elemContent.outerHeight(),
					elemPaddingTop = parseInt(elem.css('padding-top'), 10),
					elemPaddingBottom = parseInt(elem.css('padding-bottom'), 10),
					elemTrueHeight = elemContentHeight + elemPaddingTop + elemPaddingBottom;

				if( elemHeight >= elemTrueHeight ){
					elem.css('height', '100vh');
				} else if( elemHeight < elemTrueHeight ){
					elem.css('height', 'auto');
				}

			});
		} else {
			$('.section.fullscreen-element').each(function(){
				$(this).css('height', 'auto');
			});
		}
	}
	
	
	// Navigation - only for oneblock and onepage layout
	function init_ED_WaypointsNav(el) {
		var scrollblock = el.mcs.content;
		
		scrollblock.find('.section').each(function(){
			var section = $(this);

			var waypoints = section.waypoint(function(direction) {
				var activeSection = section.attr('id');

				if (direction === 'down') {
					init_ED_UpdateWaypointsNav(activeSection);
				}
				
			},{
				offset: '30%',
				context: body,
			});
			
			var waypoints = section.waypoint(function(direction) {
				var activeSection = section.attr('id');
				
				if (direction === 'up') {
					init_ED_UpdateWaypointsNav(activeSection);
				}

			},{
				offset: '-30%',
				context: body,
			});
							
		});
	}
	
	
	// Select target in navigation
	function init_ED_UpdateWaypointsNav(activeSection) {
		if($('.header-nav a[href="#'+ activeSection +'"]').hasClass('load-content')){
			headerNavElem.removeClass('active');
			headerNav.find('a[href="#'+ activeSection +'"]').parents('li').addClass('active');
		}
	}

	
	function init_ED_Navigation() {
		navToggle.off('click');
		btnLoadContent.off('click');
		
		if(!(1024 >= getWindowWidth() || body.hasClass('mobile'))) {
		
			if(body.hasClass('mCS_destroyed') || !body.hasClass('mCustomScrollbar')){
				body.mCustomScrollbar({
					axis: 'y',
					scrollbarPosition: 'inside',
					scrollInertia: 150,
					mouseWheel:{
						enable: true,
						scrollAmount: 100,
						axis: 'y'
					},
					autoHideScrollbar: false,
					alwaysShowScrollbar: 1,
					callbacks:{
						onInit: function(){
							init_ED_Parallax(this);
						},
						onScrollStart: function(){
							init_ED_Parallax(this);
						},
						whileScrolling: function(){
							
							// Show 'back to top' button
							if(this.mcs.top <= -100){
								$('a.backtotop-block').addClass('active');
							} else {
								$('a.backtotop-block').removeClass('active');
							};
							
							init_ED_Parallax(this);
							
						},
						onScroll: function(){
							init_ED_Parallax(this);
							init_ED_WaypointsNav(this);
						}
					}
				});
			}

			if(headerNav.css('display', 'none')){
				headerNav.css('display', 'block');
			}
			
			if(navToggle.hasClass('open')){
				navToggle.removeClass('open');
			}

			// Back to Top in sideblock
			$('a.backtotop-block').on('click', function(e) {
				e.preventDefault();
				if(body.hasClass('sideblock-active')){
					$('body.sideblock-active').mCustomScrollbar('scrollTo',['top',null],{
						scrollInertia: 800
					});
				}
			});
			
			btnLoadContent.on('click', function(e) {
				e.preventDefault();

				var target = $(this).attr('href');

				// Return if target is active
				if($(target).hasClass('active')){
					return true;
				}
				
				if($(target).hasClass('ed-homeblock')){
					body.removeClass('sideblock-active');
					EDSideBlock.removeClass('active');
					$(target).addClass('active');
					if(!body.hasClass('sideblock-active')){
						setTimeout(function(){
							body.mCustomScrollbar('scrollTo',['top',null],{
								scrollInertia: 150
							});
						}, 500);
					}
				} else {
					EDHomeBlock.removeClass('active');
					if(!EDSideBlock.hasClass('active')){
						body.addClass('sideblock-active');
						EDSideBlock.addClass('active');
					}
				}
				
				$('body.sideblock-active').mCustomScrollbar( 'scrollTo', $('body.sideblock-active').find('.mCSB_container').find(target), {
					scrollInertia: 800
				});
				
				// Select target in navigation
				if(headerNav.find('a[href="'+ target +'"]')){
					headerNavElem.removeClass('active');
					headerNav.find('a[href="'+ target +'"]').parents('li').addClass('active');
				}
				
			});
				
		} else {

			if(body.hasClass('mCustomScrollbar')){
				body.mCustomScrollbar('destroy');
			}

			if(headerNav.css('display', 'block')){
				headerNav.css('display', 'none');
			}
			
			if(navToggle.hasClass('open')){
				headerNav.css('display', 'block');
			}
		
			navToggle.on('click', function(e) {
				e.preventDefault();
				if(!$(this).hasClass('open')){
					$(this).addClass('open');
					headerNav.slideDown(500);
				} else {
					headerNav.slideUp(500);
					$(this).removeClass('open');
				}
			});
		
			// Smooth Scroll
			btnLoadContent.on('click', function() {	
				var sScroll = $(this),
					sScroll_target = sScroll.attr('href');					
				if(sScroll_target == null){ sScroll_target = '#'; }
				
				$.smoothScroll({
					offset: 0,
					easing: 'swing',
					speed: 800,
					scrollTarget: sScroll_target,
					preventDefault: false
				});
			});
			
		}
	}

	
	// Portfolio
	function init_ED_MasonryLayout() {
		if ($('.isotope-container').length > 0) {
			var $isotopeContainer = $('.isotope-container');
			var $columnWidth = $isotopeContainer.data('column-width');
			
			if($columnWidth == null){
				var $columnWidth = '.isotope-item';
			}
			
			$isotopeContainer.isotope({
				filter: '*',
				animationEngine: 'best-available',
				resizable: false,
				itemSelector : '.isotope-item',
				masonry: {
					columnWidth: $columnWidth
				},
				animationOptions: {
					duration: 750,
					easing: 'linear',
					queue: false
				}
			});
		}

		$('nav.isotope-filter ul a').on('click', function() {
			var selector = $(this).attr('data-filter');
			$isotopeContainer.isotope({ filter: selector });
			$('nav.isotope-filter ul a').removeClass('active');
			$(this).addClass('active');
			return false;
		});

	}


	// magnificPopup
	function init_ED_MagnificPopup() {
		$('.mfp-image').magnificPopup({
			type:'image',
			closeMarkup: '<button title="%title%" type="button" class="mfp-close"><i class="ion-android-close"></i></button>',
			removalDelay: 300,
			mainClass: 'mfp-fade'
		});
		
		$('.mfp-gallery').each(function() {
			$(this).magnificPopup({
				delegate: 'a',
				type: 'image',
				gallery: {
					enabled: true
				},
				arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',
				closeMarkup: '<button title="%title%" type="button" class="mfp-close"><i class="ion-android-close"></i></button>',
				removalDelay: 300,
				mainClass: 'mfp-fade'
			});
		});
		
		$('.mfp-iframe').magnificPopup({
			type: 'iframe',
			iframe: {
				patterns: {
					youtube: {
						index: 'youtube.com/',
						id: 'v=',
						src: '//www.youtube.com/embed/%id%?autoplay=1' // URL that will be set as a source for iframe.
					},
					vimeo: {
						index: 'vimeo.com/',
						id: '/',
						src: '//player.vimeo.com/video/%id%?autoplay=1'
					},
					gmaps: {
						index: '//maps.google.',
						src: '%id%&output=embed'
					}
				},
				srcAction: 'iframe_src'
			},
			closeMarkup: '<button title="%title%" type="button" class="mfp-close"><i class="ion-android-close"></i></button>',
			removalDelay: 300,
			mainClass: 'mfp-fade'
		});
		
		$('.mfp-ajax').magnificPopup({
			type: 'ajax',
			ajax: {
				settings: null,
				cursor: 'mfp-ajax-cur',
				tError: '<a href="%url%">The content</a> could not be loaded.'
			},
			midClick: true,
			closeMarkup: '<button title="%title%" type="button" class="mfp-close"><i class="ion-android-close"></i></button>',
			removalDelay: 300,
			mainClass: 'mfp-fade',
			callbacks: {
				ajaxContentAdded: function(mfpResponse) {
					initFlexslider();
				}
			}
		});
		
		$('.open-popup-link').magnificPopup({
			type: 'inline',
			midClick: true,
			closeMarkup: '<button title="%title%" type="button" class="mfp-close"><i class="ion-android-close"></i></button>',
			removalDelay: 300,
			mainClass: 'mfp-zoom-in'
		});
	}
	
	// Flexslider
	function init_ED_Flexslider() {
		
		if ($('.bt-flexslider').length > 0) {			
			$('.bt-flexslider').each(function() {
				var $flexsSlider = $(this),
					fs_effect = $flexsSlider.data('effect'),
					fs_easing = $flexsSlider.data('easing'),
					fs_direction = $flexsSlider.data('direction'),
					fs_loop = $flexsSlider.data('loop'),
					fs_smoothHeight = $flexsSlider.data('smooth-height'),
					fs_startAt = $flexsSlider.data('startat'),
					fs_slideshowSpeed = $flexsSlider.data('slideshow-speed'),
					fs_animationSpeed = $flexsSlider.data('animation-speed'),
					fs_randomize = $flexsSlider.data('randomize'),
					fs_video = $flexsSlider.data('video'),
					fs_pagination = $flexsSlider.data('pagination'),
					fs_directionNav = $flexsSlider.data('directionnav'),
					fs_keyboard = $flexsSlider.data('keyboard'),
					fs_pausePlay = $flexsSlider.data('pause-play');
				
				if(fs_effect == null){ fs_effect = 'slide'; }
				if(fs_easing == null){ fs_easing = 'swing'; }
				if(fs_direction == null){ fs_direction = 'horizontal'; }
				if(fs_loop == null){ fs_loop = true; }
				if(fs_smoothHeight == null){ fs_smoothHeight = false; }
				if(fs_startAt == null){ fs_startAt = 0; }
				if(fs_slideshowSpeed == null){ fs_slideshowSpeed = 7000; }
				if(fs_animationSpeed == null){ fs_animationSpeed = 700; }
				if(fs_randomize == null){ fs_randomize = false; }	
				if(fs_video == null){ fs_video = false; }
				if(fs_pagination == null){ fs_pagination = true; }
				if(fs_directionNav == null){ fs_directionNav = true; }
				if(fs_keyboard == null){ fs_keyboard = false; }
				if(fs_pausePlay == null){ fs_pausePlay = false; }
				
				$flexsSlider.flexslider({
					selector: ".slides > div.flex-slide",
					animation: ''+ fs_effect +'',
					easing: ''+ fs_easing +'',
					direction: ''+ fs_direction +'',
					animationLoop: fs_loop,
					smoothHeight: fs_smoothHeight,
					startAt: fs_startAt,
					slideshow: true,
					slideshowSpeed: fs_slideshowSpeed,
					animationSpeed: fs_animationSpeed,
					randomize: fs_randomize,
					pauseOnAction: true,
					pauseOnHover: false,
					video: fs_video,
					controlNav: fs_pagination,
					directionNav: fs_directionNav,
					prevText: "<i class='fa fa-angle-left'></i>",
					nextText: "<i class='fa fa-angle-right'></i>",
					keyboard: fs_keyboard,
					pausePlay: fs_pausePlay,
					pauseText: 'Pause',
					playText: 'Play'
				});
			});
		}
		
	}
	
	function init_ED_Plugins() {
	
		// Responsive Video - FitVids
		$('.video-container').fitVids();
		
		// Countdown
		if (countdown.length > 0) {			
			countdown.each(function() {
				var $countdown = $(this),
					finalDate = $countdown.data('countdown');
				$countdown.countdown(finalDate, function(event) {
					$countdown.html(event.strftime(
						'<div class="counter-container"><div class="counter-box first"><div class="number">%-D</div><span>Day%!d</span></div><div class="counter-box"><div class="number">%H</div><span>Hours</span></div><div class="counter-box"><div class="number">%M</div><span>Minutes</span></div><div class="counter-box last"><div class="number">%S</div><span>Seconds</span></div></div>'
					));
				});
			});
		}

		// Placeholder
		$('input, textarea').placeholder();
		
		// Tooltip
		$('[data-toggle="tooltip"]').tooltip();
		
		// Popover
		$('[data-toggle="popover"]').popover();
	
	}

		
	function init_ED_Mailchimp() {
		$('.subscribe-form').ajaxChimp({
			callback: mailchimpCallback,
			url: "mailchimp-post-url" //Replace this with your own mailchimp post URL. Don't remove the "". Just paste the url inside "".  
		});

		function mailchimpCallback(resp) {
			 if (resp.result === 'success') {
				$('.subscribe-result').html(resp.msg).fadeIn(1000);
				setTimeout(function(){
					$('.subscribe-result').fadeOut();
					$('.subscribe-form input[type="email"]').val('');
				}, 3000);
			} else if(resp.result === 'error') {
				$('.subscribe-result').html(resp.msg).fadeIn(1000);
			}  
		}

		$('.subscribe-form input[type="email"]').focus(function(){
			$('.subscribe-result').fadeOut();
		});

		$('.subscribe-form input[type="email"]').on('keydown', function(){
			$('.subscribe-result').fadeOut();
		});
		
	}
	
	
	// Map
	function init_ED_Maps() {
		var gmap = $('.gmap');
		
		if (gmap.length > 0) {
			gmap.each(function() {
				var map_height = $(this).data('height');
				
				if (map_height){
					gmap.css('height',map_height);
				}
			});
		}
		
		// GMap Contact
		if($('#gmap-contact').length){
			
			var map = new GMaps({
				div: '#gmap-contact',
				lat: 37.752797,
				lng: -122.409132,
				zoom: 14,
				scrollwheel: false
			});
			
			map.addMarker({
				lat: 37.752797,
				lng: -122.409132,
				title: 'Lunar',
				infoWindow: {
					content: '<p class="mb-0">Cali Agency</p>'
				}
			});
			
		}
	}


	// Contact Form
	function init_ED_ContactForm() {
		var $contactForm = $('.contact-forn');
		if( $contactForm.length < 1 ){ return true; }

		$contactForm.each( function(){
			var element = $(this),
				elementAlert = element.attr('data-alert-type'),
				elementResult = element.find('.contact-form-result');

			element.find('form').validate({
				submitHandler: function(form) {
					elementResult.hide();

					$(form).ajaxSubmit({
						target: elementResult,
						dataType: 'json',
						success: function( data ) {
							elementResult.html( data.message ).fadeIn( 400 );
							if( data.alert != 'error' ) { $(form).clearForm(); }
						}
					});
				}
			});

		});
	}

	// window load function
	$(window).on('load', function() {
		init_ED_FullscreenFix();
		init_ED_Preloader();
		init_ED_Animations();
		init_ED_MasonryLayout();
		body.addClass('loaded');
	});
	
	// document.ready function
	jQuery(document).ready(function($) {
		init_ED_PageBackground();
		init_ED_Navigation();
		init_ED_MagnificPopup();
		init_ED_Flexslider();
		init_ED_Plugins();
		init_ED_Mailchimp();
		init_ED_Maps();
		init_ED_ContactForm();
	});
	
	// window.resize function
	$(window).on('resize', function () {		
		init_ED_Navigation();
		init_ED_FullscreenFix();
		init_ED_MasonryLayout();
	});

})(jQuery);
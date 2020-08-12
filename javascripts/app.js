jQuery.extend({
	randomColor: function () {
		return "#" + Math.floor(Math.random() * 256 * 256 * 256).toString(16)
	}
});
(function (removeClass) {
	jQuery.fn.removeClass = function (value) {
		if (value && typeof value.test === "function") {
			for (var i = 0; i < this.length; i++) {
				var elem = this[i];
				if (elem.nodeType === 1 && elem.className) {
					var classNames = elem.className.split(/\s+/);
					for (var n = 0; n < classNames.length; n++) {
						if (value.test(classNames[n])) {
							classNames.splice(n, 1)
						}
					}
					elem.className = jQuery.trim(classNames.join(" "))
				}
			}
		} else {
			removeClass.call(this, value)
		}
		return this
	}
})(jQuery.fn.removeClass);
jQuery(document).ready(function () {
	jQuery("html").removeClass("no-js")
});
jQuery(document).foundation();
(function ($) {
	"use strict";
	$(document).ready(function () {
		$("video").each(function () {
			this.muted = true
		});
		$(".fadeinleft, .fadeinright, .fadein, .popin").appear(function () {
			var delay = $(this).data("delay");
			var that = this;
			setTimeout(function () {
				$(that).addClass("appear")
			}, delay)
		});
		$(window).scroll(function () {
			var scroll = $(window).scrollTop();
			if (scroll >= 40) {
				$("body").addClass("shrink")
			} else {
				$("body").removeClass("shrink")
			}
		});
		if ($(".masonry-container").length > 0) {
			$(".masonry-container").each(function () {
				var that = $(this);
				$(that).imagesLoaded(function () {
					setTimeout(function () {
						window.msnry = new Masonry($(that)[0], {
							itemSelector: ".mod",
							gutter: 30
						})
					}, 10)
				})
			})
		}
    if($('.js-masonry')[0]) {
      var masonry = $('.js-masonry').isotope({
        layoutMode: 'fitRows'
      });
      $('.js-masonry').imagesLoaded(function () {
				masonry.isotope('layout')
			});

			var $galleryNav = $('.gallery-nav');

      $galleryNav.find(' a').on('click', function(e){
        e.preventDefault();
				$(this).parent().toggleClass('current');

				if($(this).data('cat') == 'all') {
	        $(this).parent().siblings().removeClass('current');
	      }else {
	        $(this).parent().parent().find('[data-cat="all"]').parent().removeClass('current');
	      }

				if(!$galleryNav.find('li.current')[0]) {
	        $galleryNav.find('[data-cat="all"]').parent().addClass('current');
	      }

	      var filtersArray = [];
	      $galleryNav.find('li.current').each(function(i, el) {
					var cat = $(el).find('a').data('cat');
					if(cat == 'all') {
						filtersArray.push('*');
					}else {
						filtersArray.push('.' + $(el).find('a').data('cat'));
					}
	      });

				masonry.isotope({ filter: filtersArray.join('') });

        // $(this).parent().addClass('current').siblings().removeClass('current');
				//
        // var filter = $(this).data('cat');
        // if(filter == 'all') {
        //   masonry.isotope({ filter: '*' });
        // }else {
        //   masonry.isotope({ filter: '.' + filter });
        // }
      });
    }
		if ($("nav.top-bar.onepage").length > 0) {
			$(".top-bar-section a[href=#top]").closest("li").addClass("active");
			var ctx = $("nav.top-bar.onepage");
			var headerHeight = 59;
			var clickScrolling = false;
			var currentAnchorId;
			$(".top-bar-section a", ctx).click(function (event) {
				$(".top-bar-section a", ctx).closest("li").removeClass("active");
				$(this).closest("li").addClass("active");
				clickScrolling = true;
				try {
					if ($(this).attr("href") == "#top") {
						var distance = 0
					} else {
						var distance = $($(this).attr("href")).offset().top - headerHeight + "px"
					}
					$("html, body").stop().animate({
						scrollTop: distance
					}, {
						duration: 1200,
						easing: "easeInOutExpo",
						complete: function () {
							clickScrolling = false
						}
					});
					event.preventDefault()
				} catch (e) {}
			});
			var anchors = $(".top-bar-section a", ctx).map(function () {
				var href = $(this).attr("href");
				if (href.match(/^#/)) {
					var anchor = $($(this).attr("href"));
					if (anchor.length) {
						return anchor
					}
				}
			});
			$(window).scroll(function () {
				if (clickScrolling) return false;
				var fromTop = $(this).scrollTop();
				var passedAnchors = anchors.map(function () {
					if (fromTop + headerHeight + 1 >= $(this).offset().top) return this
				});
				var currentAnchor = passedAnchors[passedAnchors.length - 1];
				if (currentAnchor) {
					if (currentAnchorId !== currentAnchor.attr("id")) {
						currentAnchorId = currentAnchor.attr("id");
						$(".top-bar-section a", ctx).closest("li").removeClass("active");
						$(".top-bar-section a[href=#" + currentAnchorId + "]", ctx).closest("li").addClass("active")
					}
				}
			})
		}
	})
})(jQuery);
(function ($) {
	Tc.Module.BarGraph = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			$(".bars", $ctx).each(function () {
				$("> li > .highlighted", $(this)).each(function () {
					$(this).appear(function () {
						var percent = $(this).attr("data-percent");
						$(this).animate({
							width: percent + "%"
						}, 1700, function () {
							$(this).css("overflow", "visible")
						})
					})
				})
			})
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.BlogPost = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			if ($ctx.find("img, .images").length == 0) {
				$ctx.addClass("no-media")
			}
			$(".images", $ctx).slick({
				autoplay: true,
				pauseOnHover: false,
				dots: true,
				speed: 1500,
				arrows: false
			})
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.BoxedSlider = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			$(".slides", $ctx).slick({
				autoplay: true,
				pauseOnHover: false,
				dots: true,
				speed: 1500,
				arrows: false
			})
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.BoxedTextSlider = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			var $slider = $(".boxes", $ctx);
			$slider.slick({
				slidesToShow: 3,
				dots: true,
				slidesToScroll: 1,
				autoplay: true,
				autoplaySpeed: 3e3,
				pauseOnHover: false,
				responsive: [{
					breakpoint: 1024,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1
					}
				}, {
					breakpoint: 568,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1
					}
				}]
			});

			$slider.on('click', '.slick-dots button', function() {
				$slider.slick('slickPause');
			});

			$slider.on('swipe', function() {
				$slider.slick('slickPause');
			});
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.CallToAction = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.Clients = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			var slides_to_show = $ctx.data("slides_to_show");
			$(".clients", $ctx).slick({
				slidesToShow: slides_to_show,
				slidesToScroll: 1,
				autoplay: true,
				autoplaySpeed: 2e3,
				pauseOnHover: false,
				responsive: [{
					breakpoint: 767,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1
					}
				}, {
					breakpoint: 480,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1
					}
				}]
			})
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.DefaultSlider = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			var options = {
				nextButton: true,
				prevButton: true,
				autoPlay: true,
				autoPlayDelay: 3e3,
				pauseButton: true,
				cycle: true,
				animateStartingFrameIn: true,
				pagination: true,
				reverseAnimationsWhenNavigatingBackwards: true,
				preventDelayWhenReversingAnimations: true,
				fadeFrameWhenSkipped: false,
				swipeEvents: {
					left: "next",
					right: "prev"
				},
				pauseOnHover: false
			};
			var autostop = $(".sequence", $ctx).data("autostop") == "on" ? true : false;
			var timeout = $(".sequence", $ctx).data("timeout");
			if (timeout == "0") {
				options.autoPlay = false
			} else {
				options.autoPlay = true;
				options.autoPlayDelay = parseInt(timeout)
			}
			if (autostop) {
				options.autoStop = true
			} else {
				options.autoStop = false
			}
			var sequence = $(".sequence", $ctx).sequence(options).data("sequence");
			sequence.beforeCurrentFrameAnimatesOut = function () {
				var sequence = this;
				var removeStatic = function () {
					jQuery(".frame.static").removeClass("static");
					if (!window.sequenceAutoStarted && sequence.settings.autoPlay) {
						sequence.startAutoPlay(sequence.settings.autoPlayDelay);
						window.sequenceAutoStarted = true
					}
				};
				setTimeout(removeStatic, 1e3);
				if (sequence.nextFrameID == sequence.frames.length && options.autoStop) {
					sequence.stopAutoPlay()
				}
			}
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.FullscreenSlider = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			var fullscreen_slide = function () {
				$(".fullscreen_slideshow", $ctx).width($(window).width());
				if ($ctx.hasClass("force")) {
					$(".fullscreen_slideshow", $ctx).height($(window).height())
				} else {
					$(".fullscreen_slideshow", $ctx).height($(window).height() - $(".top-bar").height())
				}
			};
			fullscreen_slide();
			$(window).on("resize", fullscreen_slide);
			var options = {
				nextButton: true,
				prevButton: true,
				autoPlay: false,
				autoStop: true,
				autoPlayDelay: 3e3,
				pauseButton: true,
				cycle: true,
				animateStartingFrameIn: true,
				pagination: true,
				reverseAnimationsWhenNavigatingBackwards: true,
				preventDelayWhenReversingAnimations: true,
				fadeFrameWhenSkipped: false,
				swipeEvents: {
					left: "next",
					right: "prev"
				},
				pauseOnHover: false
			};
			var autostop = jQuery(".fullscreen_slideshow", $ctx).data("autostop") == "on" ? true : false;
			var timeout = jQuery(".fullscreen_slideshow", $ctx).data("timeout");
			if (timeout == "0" || !timeout) {
				options.autoPlay = false
			} else {
				options.autoPlay = true;
				options.autoPlayDelay = parseInt(timeout)
			}
			if (autostop) {
				options.autoStop = true
			} else {
				options.autoStop = false
			}
			var fullscreen = jQuery(".fullscreen_slideshow", $ctx).sequence(options).data("sequence");
			fullscreen.beforeCurrentFrameAnimatesOut = function () {
				var sequence = this;
				var removeStatic = function () {
					jQuery(".frame.static").removeClass("static");
					if (!window.fullSequenceAutoStarted && sequence.settings.autoPlay) {
						sequence.startAutoPlay(sequence.settings.autoPlayDelay);
						window.fullSequenceAutoStarted = true
					}
				};
				setTimeout(removeStatic, 1e3);
				if (sequence.nextFrameID == sequence.frames.length && options.autoStop) {
					sequence.stopAutoPlay()
				}
			}
		}
	})
})(Tc.$);
// (function ($) {
// 	Tc.Module.Gallery = Tc.Module.extend({
// 		init: function ($ctx, sandbox, modId) {
// 			this._super($ctx, sandbox, modId)
// 		},
// 		dependencies: function () {},
// 		onBinding: function () {
// 			var $ctx = this.$ctx;
// 			$(".gallery-nav ul li a", $ctx).click(function () {
// 				$(".gallery-nav ul li").removeClass("current");
// 				$(this).closest("li").addClass("current");
// 				var cat = $(this).attr("data-cat");
// 				var gallery = $(".gallery-nav").closest(".modGallery").find("ul.gallery");
// 				if (cat === "all") {
// 					$("li", gallery).removeClass("hidden")
// 				} else {
// 					$("li", gallery).each(function () {
// 						if ($(this).hasClass(cat)) {
// 							$(this).removeClass("hidden")
// 						} else {
// 							$(this).addClass("hidden")
// 						}
// 					})
// 				}
// 				return false
// 			})
// 		}
// 	})
// })(Tc.$);
(function ($) {
	Tc.Module.IconText = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.MasonryGallery = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			var items = $(".gallery li", $ctx);
			items.each(function (index, value) {
				$(this).data("masonry-id", index)
			});
			var msnry = new Masonry($(".gallery")[0], {
				itemSelector: "li",
				gutter: 0,
				isInitLayout: false
			});
			window.msnry = msnry;
			$(".gallery", $ctx).imagesLoaded(function () {
				msnry.layout()
			});
			$(".gallery-nav ul li a", $ctx).click(function () {
				$(".gallery-nav ul li").removeClass("current");
				$(this).closest("li").addClass("current");
				var cat = $(this).attr("data-cat");
				var gallery = $(".gallery-nav").closest(".mod").find("ul.gallery");
				if (cat === "all") {
					var exists = $(".gallery li", $ctx);
					var elems = [];
					$(items).each(function () {
						var item = this;
						var skip = false;
						exists.each(function () {
							if ($(item).data("masonry-id") == $(this).data("masonry-id")) {
								skip = true
							}
						});
						if (!skip) {
							$(".gallery", $ctx)[0].appendChild($(this)[0]);
							elems.push($(this)[0])
						}
					});
					msnry.prepended(elems)
				} else {
					$("li", gallery).each(function () {
						if (!$(this).hasClass(cat)) {
							msnry.remove($(this))
						}
					});
					var exists = $(".gallery li", $ctx);
					var elems = [];
					$(items).each(function () {
						var item = this;
						var skip = false;
						exists.each(function () {
							if ($(item).data("masonry-id") == $(this).data("masonry-id")) {
								skip = true
							}
						});
						if ($(this).hasClass(cat) && !skip) {
							$(".gallery", $ctx)[0].appendChild($(this)[0]);
							elems.push($(this)[0])
						}
					});
					msnry.appended(elems)
				}
				msnry.layout();
				return false
			})
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.Milestone = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			$ctx.appear(function () {
				$("strong", $ctx).countTo({
					speed: 1400
				})
			})
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.PriceBox = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.SectionHeader = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.TeamMember = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx
		}
	})
})(Tc.$);
(function ($) {
	Tc.Module.Testimonials = Tc.Module.extend({
		init: function ($ctx, sandbox, modId) {
			this._super($ctx, sandbox, modId)
		},
		dependencies: function () {},
		onBinding: function () {
			var $ctx = this.$ctx;
			var show_dots = true;
			if ($ctx.hasClass("simple")) {
				show_dots = false
			}
			$(".items", $ctx).slick({
				autoplay: true,
				pauseOnHover: false,
				dots: show_dots,
				speed: 1500,
				arrows: false
			})
		}
	})
})(Tc.$);

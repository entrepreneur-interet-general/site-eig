jQuery(function () {
    const $ = jQuery;

    const selector = ".gallery-nav li a";

    if ($(selector).length) {
        $("body").append($('<div class="backToTop" title="Back to top">⤒</div>'))
    }

    $(selector).click((e) => {
        const cat = $(e.target).data("cat");
        if (cat === "tous") return;

        const el = $(`.gallery .${cat}`).first();
        const h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
        const p = el.position();

        if (p.top > h) {

            let scrollTime = Math.round((p.top - h) / 3);
            scrollTime = Math.min(scrollTime, 800);
            scrollTime = Math.max(scrollTime, 300);
            // 300 < scrollTime < 800 (ms)

            $([document.documentElement, document.body]).animate({
                scrollTop: el.offset().top - 100
            }, scrollTime);
        }
    });

    $(window).scroll((e) => {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            $(".backToTop").fadeIn(250);
            $(".backToTop").css("display", "flex")
        } else {
            $(".backToTop").fadeOut(250);
        }
    })

    $(".backToTop").click(() => {
        $([document.documentElement, document.body]).animate({
            scrollTop: 0
        }, 500);
    })
});
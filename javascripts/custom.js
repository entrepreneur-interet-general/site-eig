jQuery(function () {
    const $ = jQuery;
    $(".gallery-nav li a").click((e) => {
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
});
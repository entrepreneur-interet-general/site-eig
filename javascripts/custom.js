jQuery(function () {
    const $ = jQuery;
    $(".gallery-nav li a").click((e) => {
        const cat = $(e.target).data("cat");
        if ([2017, 2018].indexOf(cat) > -1) {
            const el = $(`.gallery .${cat}`).first();
            const scrollTime = cat === 2017 ? 800 : 500;
            $([document.documentElement, document.body]).animate({
                scrollTop: el.offset().top - 100
            }, scrollTime);
        }
    });
});
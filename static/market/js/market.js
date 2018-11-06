$(function () {
    $('.market').width(innerWidth);
    // 每次获取 上次点击分类的位置
    typeIndex = $.cookie('typeIndex');
    if (typeIndex) {
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    } else {

        $('.type-slider .type-item:first').addClass('active')
    }
    // 每次点击记录点击分类的位置
    $('.type-item').click(function () {
        $.cookie('typeIndex', $(this).index(), {expires: 1, path: '/'})
    });


    // 分类按钮
    let categoryBt = false; // 默认隐藏
    $('#categoryBt').click(function () {
        // 取反
        categoryBt = !categoryBt;
        categoryBt ? categoryViewShow() : categoryViewHide()
    });

    // 排序按钮
    let sortBt = false;  // 默认是隐藏
    $('#sortBt').click(function () {
        // 取反
        sortBt = !sortBt;
        sortBt ? sortViewShow() : sortViewHide()
    });
    // 灰色蒙层
    $('.bounce-view').click(function () {
        sortBt = false;
        sortViewHide();
        categoryBt = false;
        categoryViewHide()
    });

    function categoryViewShow() {
        sortBt = false;
        sortViewHide();
        $('.bounce-view.category-view').show();
        $('#categoryBt i').removeClass('glyphicon-triangle-top').addClass('glyphicon-triangle-bottom')
    }

    function categoryViewHide() {
        $('.bounce-view.category-view').hide();
        $('#categoryBt i').removeClass('glyphicon-triangle-bottom').addClass('glyphicon-triangle-top')
    }

    function sortViewShow() {
        categoryBt = false;
        categoryViewHide();
        $('.bounce-view.sort-view').show();
        $('#sortBt i').removeClass('glyphicon-triangle-top').addClass('glyphicon-triangle-bottom')
    }

    function sortViewHide() {
        $('.bounce-view.sort-view').hide();
        $('#sortBt i').removeClass('glyphicon-triangle-bottom').addClass('glyphicon-triangle-top')
    }

    // 购物车操作
    $('.bt-wrapper .glyphicon-minus').hide();
    $('.bt-wrapper .num').hide();

    //加操作
    $('.bt-wrapper .glyphicon-plus').click(function () {
        var goodsid = $(this).attr('goodsid');
        var $that = $(this);
        $.get('/addcart/',{'goodsid':goodsid}, function (response) {
            if (response.status === -1){ // 未登录
                window.open('/login/', target="_self")
            } else if (response.status ===1){   // 添加成功
                $that.prev().show().html(response.number);
                $that.prev().prev().show()
            }
        })
    })
});
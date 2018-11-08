$(function () {
    $('.cart').width(innerWidth);


    //单个
    $('.cart .confirm-wrapper').click(function () {
        var cartid = $(this).attr('cartid');
        var $that = $(this);
        $.get('/changecartstatus/',{'cartid':cartid},function (response) {
            console.log(response);
            if (response.status == 1){
                var isselect = response.isselect;
                $that.attr('isselect',isselect);
                $that.children().remove();  //清空
                if (isselect){
                    $that.append('<span class="glyphicon glyphicon-ok"></span>')
                }else {
                    $that.append('<span class="no"></span>')
                }
                                // 总计
                total()
            }
        })
    });

    //全选
    $('.cart .all').click(function () {
        var isselect = $(this).attr('isselect');
        isselect = (isselect === 'false');
        $(this).attr('isselect',isselect);
        console.log(1111111)
        if (isselect){
            $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
        }
         $.get('/changecartselect/', {'isselect':isselect}, function (response) {
            if (response.status == 1){
                // 遍历
                $('.confirm-wrapper').each(function () {
                    $(this).attr('isselect', isselect);
                    if (isselect){
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                });
                 // 总计
                total()
            }
        })
    });
    function total() {
        var sum = 0;
         // 遍历操作
        $('.goods').each(function () {
            var $confirm = $(this).find('.confirm-wrapper');
            var $content = $(this).find('.content-wrapper');
             if ($confirm.find('.glyphicon-ok').length) {
                var price = $content.find('.price').attr('price');
                var num = $content.find('.num').attr('number');
                sum += price * num
            }
        });
         // 显示
        $('.bill .total b').html(parseInt(sum))
    }

});
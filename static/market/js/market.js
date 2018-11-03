$(function(){
    $('.market').width(innerWidth);
    // 每次获取 上次点击分类的位置
    typeIndex = $.cookie('typeIndex');
    if (typeIndex){
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    } else {

        $('.type-slider .type-item:first').addClass('active')
    }
    // 每次点击记录点击分类的位置
    $('.type-item').click(function () {
       $.cookie('typeIndex', $(this).index(), {expires:1, path:'/'})
    })

});
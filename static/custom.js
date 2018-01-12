$(document).ready(function() {
    $(document).on('click', '.nav-item a', function (e) {
        $(this).parent().addClass('active').siblings().removeClass('active');
    });
});
// $(document).ready(function() {
//     $('li.active').removeClass('active');
//     $('a[id="' + location.pathname + '"]').closest('li').addClass('active'); 
//   });

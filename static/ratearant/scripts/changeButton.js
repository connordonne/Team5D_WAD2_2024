$(document).ready(function() {
    
    $('.btn-light').hover(
        function() {
            $(this).addClass('btnRedChange');
        },
        function() {
            $(this).removeClass('btnRedChange');
        }
    );
});
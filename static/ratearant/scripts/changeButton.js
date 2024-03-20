$(document).ready(function() {
    
    $('.btn-light').hover(
        function() {
            $(this).addClass('btnGreen');
        },
        function() {
            $(this).removeClass('btnGreen');
        }
    );
});
$(document).ready(function() {
    
    $('.btn-light').hover(
        function() {
            $(this).addClass('btnRed');
        },
        function() {
            $(this).removeClass('btnRed');
        }
    );
});
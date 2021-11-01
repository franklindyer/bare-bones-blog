$(document).ready(function() { 
var input_id;

$("[data-audio-url]").each(
    function(){
        $(this).on('click', function() {
            var mp3Url = $(this).attr('data-audio-url');
            var a = new Audio(mp3Url);
            a.play();
        });
    }
);

})

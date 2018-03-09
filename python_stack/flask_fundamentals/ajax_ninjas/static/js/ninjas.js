$(document).ready(function(){
    $(document).on('click', 'button', function(){
        if ($(this).text() === 'Enter'){
            var color_pick = $("#buttons > input").val()
            $("#buttons > input").val("")
        }
        else {
            var color_pick = $(this).text()
        }
        $.ajax({
            data : {
                    color : color_pick,
            },
            type : 'POST',
            url : '/',
    })
    .done(function(data) {
        $('#images').html("")
        if (data.april_url) {
            $('#images').append("<h1>There's no ninja in that color!</h1>")
            $('#images').append('<img src="' + data.april_url + '" alt="April">')
        }
        else {
            $('#images').append("<h1>You chose " + data.name + "!</h1>")
            $("#images").append('<img src="' + data.url + '" alt="' + data.name + '">')
        }
    });
    });
});
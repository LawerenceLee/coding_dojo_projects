$(document).ready(function(){
    $(document).on("click", "button", function(){
        if ($(this).text() == "Post a message" && $("#posting>textarea").val()) {
            var message_txt = $("#posting>textarea").val()
            $("#posting>textarea").val("")
            $.ajax({
                data : {message_text : message_txt},
                type: "POST",
                url: "/ajax_message",
            }).done(function(data){
                var message = '<div class="message_wrapper"><h3 class="message_info">' + data.message_info
                message += '</h3><p class="message">' + data.message + '</p></div>'
                message += '<div id="commenting"><h3>Post a comment</h2>'
                message += '<textarea name="comment" id="message" cols="100" rows="3"'
                message += 'message-id="' + data.message_id +'"'
                message += '></textarea><button>Post a comment</button></div>'
                $("#messages_box").prepend(message)
            });
        }
        else if ($(this).text() == "Post a comment" && $("#commenting>textarea").val()) {
            var comment_txt = $("#commenting>textarea").val()
            var message_identifier = $("#commenting>textarea").attr("message-id")
            $("#commenting>textarea").val("")
            $.ajax({
                data : {comment_text : comment_txt, message_id : message_identifier},
                type: "POST",
                url: "/ajax_comment",
            }).done(function(data){
                var comment = '<h4 class="comment_info">' + data.comment_info + "</h4>"
                comment += '<p class="comment">'+ data.comment + '</p>'
                $("#commenting").before(comment)
            });
        }
    });
});
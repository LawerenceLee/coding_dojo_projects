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
                var message = '<div class="message_wrapper"><div class="message_block">'
                message += '<h3 class="message_info deleteable" style="display:inline-block;">' + data.message_info
                message += '</h3><button class="deleteable delete_button" message-id="'
                message += data.message_id + '" style="display:inline-block;vertical-align:text-bottom;">'
                message += 'DELETE</button><p class="message">' + data.message
                message += '</p></div><div class="comments_wrapper"></div><div class="commenting"><h3>Post a comment</h2>'
                message += '<textarea name="comment" cols="100" rows="1"'
                message += '></textarea><button message-id="' + data.message_id +'">Post a comment</button></div></div>'
                $("#messages_box").prepend(message)
            });
        }
        else if ($(this).text() == "Post a comment" && $(this).siblings("textarea").val()) {

            var comment_txt = $(this).siblings("textarea").val()
            var message_identifier = $(this).attr("message-id")
            $(this).siblings("textarea").val("")

            $.ajax({
                data : {comment_text : comment_txt, message_id : message_identifier},
                type: "POST",
                url: "/ajax_comment",
            }).done(function(data){
                var comment = '<div class="comment_block"><h4 class="comment_info">' + data.comment_info + "</h4>"
                comment += '<p class="comment">'+ data.comment + '</p></div>'
                $("#"+message_identifier).append(comment)
            });
        }
        else if ($(this).text() == "DELETE") {
            var delete_button = $(this)
            var message_identifier = $(this).attr("message-id")

            $.ajax({
                data : {message_id : message_identifier},
                type: "POST",
                url: "/delete_message",
            }).done(function(){
                console.log($(this).closest("div"))
                $(delete_button).closest(".message_wrapper").html("")
            });
        }
    });
});
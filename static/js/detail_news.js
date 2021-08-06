$(function () {
    console.log(1111111111111111111)
    // 写入csrf
    $.getScript("/static/js/csrftoken.js");

    // 点赞
    $("#like").click(function(){
      var news_id = $("#like").attr("video-id");
      $.ajax({
            url: '/newsApp/like/',
            data: {
                news_id: news_id,
                'csrf_token': csrftoken
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                var code = data.code
                if(code == 0){
                    var likes = data.likes
                    var user_liked = data.user_liked
                    $('#like-count').text(likes)
                    if(user_liked == 0){
                        $('#like').removeClass("grey").addClass("red")
                    }else{
                        $('#like').removeClass("red").addClass("grey")
                    }
                }else{
                    var msg = data.msg
                    alert(msg)
                }

            },
            error: function(data){
              alert("Likes failed")
            }
        });
    });

     // 收藏
    $("#star").click(function(){
      var news_id = $("#star").attr("video-id");
      $.ajax({
            url: '/newsApp/collect/',
            data: {
                news_id: news_id,
                'csrf_token': csrftoken
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                var code = data.code
                if(code == 0){
                    var collects = data.collects
                    var user_collected = data.user_collected
                    $('#collect-count').text(collects)
                    if(user_collected == 0){
                        $('#star').removeClass("grey").addClass("red")
                    }else{
                        $('#star').removeClass("red").addClass("grey")
                    }
                }else{
                    var msg = data.msg
                    alert(msg)
                }

            },
            error: function(data){
              alert("Collection Failed")
            }
        });
    });


    // 提交评论
    var frm = $('#comment_form')
    frm.submit(function () {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            dataType:'json',
            data: frm.serialize(),
            success: function (data) {
                var code = data.code
                var msg = data.msg
                if(code == 0){
                    $('#id_content').val("")
                    $('.comment-list').prepend(data.html);
                    $('#comment-result').text("Comment Successful")
                    $('.info').show().delay(2000).fadeOut(800)
                }else{
                    $('#comment-result').text(msg)
                    $('.info').show().delay(2000).fadeOut(800);
                }
            },
            error: function(data) {
            }
        });
        return false;
    });

})






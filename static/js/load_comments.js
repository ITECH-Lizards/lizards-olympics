
$(function(){
    // Pages
    var page = 0;
    // 15 each page
    var page_size = 15;

    // dropload
    $('.comments').dropload({
        scrollArea : window,
        loadDownFn : function(me){
            page++;

            $.ajax({
                type: 'GET',
                url: comments_url,
                data:{
                     video_id: video_id,
                     page: page,
                     page_size: page_size
                },
                dataType: 'json',
                success: function(data){
                    var code = data.code
                    var count = data.comment_count
                    if(code == 0){
                        $('#id_comment_label').text(count + "Comments");
                        $('.comment-list').append(data.html);
                        me.resetload();
                    }else{
                        me.lock();
                        me.noData();
                        me.resetload();
                    }
                },
                error: function(xhr, type){
                    me.resetload();
                }
            });
        }
    });
});
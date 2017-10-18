// Please include or add javascript to this file
//import $ from "jquery";
var likedBooks = [];
var commentedBooks = [];
$( document ).ready(function() {
	window.liked = function(bookId) {
        if(likedBooks.indexOf(bookId) !== -1) {
            alert('You already liked This!');
            return; 
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: 'like',
            type: 'post',
            data: {
                bookId: bookId
            },
            success: function(data) {
                $(".count").html("Likes: "+data.likes);
                console.log(data);
                likedBooks.push(bookId);
            },
            error: function(data) {
                console.log("HELLO");
            }
        });
    };

    $('#comment-form').submit(function() { 
        var name = $('#name').val();
        var comment = $('#comment-body').val();
        var bookId = $('#book-id-value').val();
        var csrftoken = $('#comment-form [name=csrfmiddlewaretoken]').val();
        console.log(csrftoken);
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
        $.ajax({
            url: 'comment',
            type: 'post',
            data:  {
                bookId: bookId,
                name: name,
                comment: comment
            },
            success: function(response) {
                $('#comment-text-field').val("");
                $('#user-text-field').val("");
            },
            error: function(response) {
                alert("Unable to add comment");
            }
        });
        return false;
    });

    function getCookie(c_name) {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

});
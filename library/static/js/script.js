$(document).ready(function(){

    var check_view_comment = false;

    $('.view-review').click(function (){

        if(!check_view_comment){

            let commentDate = (new Date()).toLocaleString('en-US');

            var username = $(this).attr('data-user-name');
            var item_id = $(this).attr('data-item-id');
            var ajax_url = $(this).attr('data-ajax-url');

            // Using the core $.ajax() method
            $.ajax({

                // The URL for the request
                url: ajax_url,

                // The data to send (will be converted to a query string)
                data: {
                    _id: item_id
                },

                // Whether this is a POST or GET request
                type: "GET",

                headers: {'X-CSRFToken': csrftoken},

                // The type of data we expect back
                dataType: "json",

                context: this
            })
                // Code to run if the request succeeds (is done);
                // The response is passed to the function
                .done(function (json) {
                    //alert("request received successfully")
                    if (json.success == 'success') {
                        if (json.review.length == 0) {
                            var newCommentFormat = `<div class = "comments-recorded"> <p class="user-comment-recorded"> No Comments available </p>
                            </div>`;

                            $(".user-commented").append(newCommentFormat);
                            check_view_comment = true;
                        }
                        else{
                            for (i=0; i<json.review.length; i++){
                                if(username == json.review[i].user){
                                    var newCommentFormat = `<div class = "comments-recorded"> <p class="user-comment-recorded"> ${json.review[i].review} </p>
                                    <p class="user-comment-time">Commented on: ${json.review[i].date}</p>
                                    <p>Commented By: <a href="/users/profile/${json.review[i].user}">${json.review[i].user}</a></p>
                                    <input type="hidden" class="hidden-id" value="${json.review[i].id}">
                                    <button class="edit-button">Edit</button>
                                    <button class="delete-button">Delete</button> </div>`;
                                }
                                else{
                                    var newCommentFormat = `<div class = "comments-recorded"> <p class="user-comment-recorded"> ${json.review[i].review} </p>
                                    <p class="user-comment-time">Commented on: ${json.review[i].date}</p>
                                    <p>Commented By: <a href="/users/profile/${json.review[i].user}">${json.review[i].user}</a></p>
                                    <input type="hidden" class="hidden-id" value="${json.review[i].id}"></div>`;

                                }

                                $(".user-commented").append(newCommentFormat);
                                check_view_comment = true;
                            }
                        }
                    }

                })
                // Code to run if the request fails; the raw request and
                // status codes are passed to the function
                .fail(function (xhr, status, errorThrown) {
                    alert("Sorry, there was a problem!");
                    console.log("Error: " + errorThrown);

                })
                // Code to run regardless of success or failure;
                .always(function (xhr, status) {
                    // alert("The request is complete!");
                });
        }
    });

    var userCommentID = 1
    //Delete Comment
    $('.user-commented').on('click', '.edit-button', function (){
       var userCommentElement = $("#createUserComment");
       let existingComment =$(this).siblings(('.user-comment-recorded')).html();
       userCommentElement.val(existingComment);
       editCommentHTMLElement = $(this).parent();
       userCommentID = $(this).siblings(".hidden-id").val();
    });

    //User Interaction - 1: on Submit button a new element will be
    //added and modifying an existing element
    var editCommentHTMLElement = false;

    $('.user-commented').on('click', '.delete-button', function (){
       var comment_id = $(this).siblings(".hidden-id").val();
       // var ajax_url = $(this).attr('data-ajax-url2');
        $.ajax({

            // The URL for the request
            url: "/todo/delete/comment",

            // The data to send (will be converted to a query string)
            data: {
                _comment_id: comment_id,
            },

            // Whether this is a POST or GET request
            type: "POST",

            headers: {'X-CSRFToken': csrftoken},

            // The type of data we expect back
            dataType: "json",

            context: this
        })
        .done(function (json) {
                $(this).siblings().remove();
                $(this).remove();
            })
            // Code to run if the request fails; the raw request and
            // status codes are passed to the function
            .fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem!");
                console.log("Error: " + errorThrown);

            })
            // Code to run regardless of success or failure;
            .always(function (xhr, status) {
                // alert("The request is complete!");
            });
    });

    $(".submit-button").click(function(){

        var createUserCommentElement = $("#createUserComment");
        var userComment = createUserCommentElement.val();

        //if the comment length is zero then alert the user when
        //clicking on submit button
        if(userComment.length <= 0){
            alert('No Comment added');
        }
        //if the comment is already posted then comment will either be added or modified
        else {
            let commentDate = (new Date()).toLocaleString('en-US');

            if(!editCommentHTMLElement) {


                var item_id = $(this).attr('data-item-id');
                var ajax_url = $(this).attr('data-ajax-url');

                // Using the core $.ajax() method
                $.ajax({

                    // The URL for the request
                    url: ajax_url,

                    // The data to send (will be converted to a query string)
                    data: {
                        _id: item_id,
                        _user_review: $("#createUserComment").val()
                    },

                    // Whether this is a POST or GET request
                    type: "POST",

                    headers: {'X-CSRFToken': csrftoken},

                    // The type of data we expect back
                    dataType: "json",

                    context: this
                })
                    // Code to run if the request succeeds (is done);
                    // The response is passed to the function
                    .done(function (json) {
                        //alert("request received successfully")
                        if (json.success == 'success') {
                            for (i=0; i<json.comment.length; i++){
                                var newCommentFormat = `<div class = "comments-recorded"> <p class="user-comment-recorded"> ${json.comment[i].review} </p>
                                <p class="user-comment-time">Commented on: ${json.comment[i].date}</p>
                                <input type="hidden" class="hidden-id" value="${json.comment[i].id}">
                                <p>Commented By: <a href="/users/profile/${json.comment[i].user}">${json.comment[i].user}</a></p>
                                <button class="edit-button">Edit</button>
                                <button class="delete-button">Delete</button></div>`;
                            }
                            $(".user-commented").append(newCommentFormat);
                        }

                    })
                    // Code to run if the request fails; the raw request and
                    // status codes are passed to the function
                    .fail(function (xhr, status, errorThrown) {
                        alert("Sorry, there was a problem!");
                        console.log("Error: " + errorThrown);

                    })
                    // Code to run regardless of success or failure;
                    .always(function (xhr, status) {
                        // alert("The request is complete!");
                    });
            }

            else{
                editCommentHTMLElement.find('.user-comment-recorded').html(userComment);


                let notifySuccess = $('<p class = ".user-comment"> Comment edited successfully</p>');

                //successfully EDITED comment message for users
                $(notifySuccess).appendTo($(".user-comment")).fadeOut('slow', function(){
                        $(this).remove();
                });

                var comment_id = userCommentID;
                var ajax_url = $(this).attr('data-ajax-url2');
                $.ajax({

                    // The URL for the request
                    url: ajax_url,

                    // The data to send (will be converted to a query string)
                    data: {
                        _comment_id: comment_id,
                        _new_comment: userComment
                    },

                    // Whether this is a POST or GET request
                    type: "POST",

                    headers: {'X-CSRFToken': csrftoken},

                    // The type of data we expect back
                    dataType: "json",

                    context: this
                })
                .done(function (json) {
                        alert("request received successfully")
                    })
                    // Code to run if the request fails; the raw request and
                    // status codes are passed to the function
                    .fail(function (xhr, status, errorThrown) {
                        alert("Sorry, there was a problem!");
                        console.log("Error: " + errorThrown);

                    })
                    // Code to run regardless of success or failure;
                    .always(function (xhr, status) {
                        // alert("The request is complete!");
                    });
            }
            editCommentHTMLElement = false;
            createUserCommentElement.val("");
        }

    });

    //Calling the simulated search method
    checkQueryString();
});


//Simulated Search Result method
function checkQueryString(){
    var searchQuery = window.location.search;
    var urlParams = new URLSearchParams(searchQuery);
    var searchKey = urlParams.get("search-result"); //Parsing the search phrases.

    if (searchKey == 'harry'){//Search Result for search phrase "harry"
        window.alert("success");
        var searchItem = $('<div class="column">' + '<div class="card">'
                            + '<img class="book_img" src="img/harry.jpg" alt="book1"><h2>Harry Potter</h2>'
                            + '<p><b>by J.K. Rowling</b></p>'
                            + '<span><b>Rating : 4.5</b></span>'
                            + '<p><b>Buy for <img class="icon" src="img/dollar-currency-symbol.png" alt="icon">16.5</b></p>'
                            + '</div>'
                            + '</div>'+

                            '<div class="column">' + '<div class="card">'
                            + '<img class="book_img" src="img/harry2.jpg" alt="book1"><h2>Harry Potter</h2>'
                            + '<p><b>by J.K. Rowling</b></p>'
                            + '<span><b>Rating : 4.5</b></span>'
                            + '<p><b>Buy for <img class="icon" src="img/dollar-currency-symbol.png" alt="icon">16.5</b></p>'
                            + '</div>'
                            + '</div>'+

                            '<div class="column">' + '<div class="card">'
                            + '<img class="book_img" src="img/harry3.jpg" alt="book1"><h2>Harry Potter</h2>'
                            + '<p><b>by J.K. Rowling</b></p>'
                            + '<span><b>Rating : 4.5</b></span>'
                            + '<p><b>Buy for <img class="icon" src="img/dollar-currency-symbol.png" alt="icon">16.5</b></p>'
                            + '</div>'
                            + '</div>');
        $(".content-book").append(searchItem);
    }

    else if(searchKey == 'hobbit'){//Search Result for search phrase "hobbit"
        window.alert("success");
        var searchItem = $('<div class="column">' + '<div class="card">'
                            + '<img class="book_img" src="img/hobbit1.jpg" alt="book1"><h2>The Hobbit</h2>'
                            + '<p><b>by J.R.R Tolkien</b></p>'
                            + '<span><b>Rating : 4.5</b></span>'
                            + '<p><b>Buy for <img class="icon" src="img/dollar-currency-symbol.png" alt="icon">16.5</b></p>'
                            + '</div>'
                            + '</div>'+

                            '<div class="column">' + '<div class="card">'
                            + '<img class="book_img" src="img/hobbit2.jpg" alt="book1"><h2>The Hobbit</h2>'
                            + '<p><b>by J.R.R Tolkien</b></p>'
                            + '<span><b>Rating : 4.5</b></span>'
                            + '<p><b>Buy for <img class="icon" src="img/dollar-currency-symbol.png" alt="icon">16.5</b></p>'
                            + '</div>'
                            + '</div>'+

                            '<div class="column">' + '<div class="card">'
                            + '<img class="book_img" src="img/hobbit3.jpg" alt="book1"><h2>The Hobbit</h2>'
                            + '<p><b>by J.R.R Tolkien</b></p>'
                            + '<span><b>Rating : 4.5</b></span>'
                            + '<p><b>Buy for <img class="icon" src="img/dollar-currency-symbol.png" alt="icon">16.5</b></p>'
                            + '</div>'
                            + '</div>');
        $(".content-book").append(searchItem);
    }

    else {  //This message will get displayed for the search phrases other than the mentioned ones.
        var searchItem = $('<h1 class="search-not-exist"> No Search Result </h1>');
        $(".content-book").append(searchItem);
    }

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

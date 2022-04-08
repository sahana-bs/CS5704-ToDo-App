$(document).ready(function(){
    //This method is used to to disable all the fields after the click of a button
    // and for printing the success message
    $('button.add-review').click(function (){
        //Traversing through all the fields and disabling them.
        $(".review-info").each(function (){
                $(this).prop("disabled", true);
        });
        var successMsg = $('<p class="review-success">Review has been added successfully</p>');
        $(successMsg).appendTo( $(".form-center") ).fadeOut(5000, function (){
            $(this).remove();
        });
        //$("#review-form :input").prop("disabled", true);
    });

    //This method is used for adding a new field on the change of an existing field
    // and it will change the css of the existing filed as well.
    $('.row').on("change", "#rating", function (){
        var ratingVal = $(this).val();
        var extraItem = $('<div class="row" id="extra-item">' + '<div class="col-25">'
                            + '<label for="review">Reason:</label>'
                            + '</div>' + '<div class="col-75">'
                            + '<input class="review-info" type="text" id="reason" name="Reason" placeholder="Reason of low rating">'
                            + '</div>' + '</div>');

        if (ratingVal < 2){ //if the rating is less than 2 then extra field will get added and the border color will also turn red.
            $(extraItem).appendTo( $(".container-form"));
            $("#rating").css("border","1px solid red");
        }

        else{ //the extra field will get removed and the border color will also turn to its original color.
            $("#extra-item").remove();
            $("#rating").css("border","1px solid #ccc");
        }
    });
    checkSearchQuery();
});

//This method is written to implement the simulated search.
//using two search phrases : "harry" and "hobbit"
function checkSearchQuery(){
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


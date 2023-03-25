console.log("funcionou")


$(document).ready(function(){
    $(".hamburger").click(function(){
       $(".wrapper").toggleClass("collapse");
    });
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
    searchForm.submit();
    });
});






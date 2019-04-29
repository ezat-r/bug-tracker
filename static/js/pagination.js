// Script to handle pagination for bugs

// get total number of bugs 
var numberOfItems = $(".bug-item").length;

// limit for number of bugs visible per pagination page
var numberLimit = 10;

paginate();

function paginate(){
    // check if the number of Bugs is higher than the page view limit
    if(numberOfItems > numberLimit){
        // number of bugs is higher than limit, so perform pagination

        // begin by bringing into view 10 bugs and hiding the rest using the jquery 'gt()' method
        $(`.bug-item:gt(${numberLimit - 1})`).hide();
        
        // calculate number of pagination links needed
        var numberPaginationLinks = 0;

        if((numberOfItems / numberLimit) % 1 >= 0.5 || (numberOfItems / numberLimit) % 1 == 0){
            // if decimal part of the division is bigger than 0.5 or there is no remainder, then do a simple math.round
            numberPaginationLinks = Math.round(numberOfItems / numberLimit);
        }else{
            // otherwise perform a math.round and add 1 to it, to make sure correct number of pagination links are shown
            numberPaginationLinks = Math.round(numberOfItems / numberLimit) + 1;
        }
        

        for(var i=1; i<numberPaginationLinks; i++){
            // keep inserting li tag after the last li element in the ul element
            $(".pag-item").last().after(`<li class="waves-effect pag-item"><a>${i+1}</a></li>`);
        }
    }else{
        // otherwise hide pagination
        $("#pag-container").addClass("pag-hide");
    }
}

// pagination numbered buttons 'on click' handler
$(".pag-item").on("click", function(){
    if($(this).hasClass("active") == false){
        // remove the active class from all pagination list elements
        $(".pag-item").removeClass("active");

        // add the active class to the selected li element
        $(this).addClass("active");

        // call hideShowBugs with the index of the current 'active' item as the parameter
        hideShowBugs($("li.pag-item.active").index());
    }
});

// pagination left button 'on click' handler
$("#pag-left").on("click", function(){
    if($(".pag-item").first().hasClass("active") == false){
        // variable to hold the list item of interest
        var targetItem = $("li.pag-item.active").prev();

        // remove active class from all list elements
        $(".pag-item").removeClass("active");

        // add active class to the target list item
        targetItem.addClass("active");

        // call hideShowBugs with the index of the current 'active' item as the parameter
        hideShowBugs($("li.pag-item.active").index());
    }
});

// pagination right button 'on click' handler
$("#pag-right").on("click", function(){
    if($(".pag-item").last().hasClass("active") == false){
        // variable to hold the list item of interest
        var targetItem = $("li.pag-item.active").next();

        // remove active class from all list elements
        $(".pag-item").removeClass("active");

        // add active class to the target list item
        targetItem.addClass("active");

        // call hideShowBugs with the index of the current 'active' item as the parameter
        hideShowBugs($("li.pag-item.active").index());
    }
});

function hideShowBugs(currentPagNum){
    // start off by hiding all recipes from view
    $(`.bug-item`).hide();
    
    // calculate number of bugs viewed so far so if current pagination number is 2
    // and limit per page is 5 then total number of possible recipes viewed so far is 10 etc.
    var bugsViewedSoFar = currentPagNum * numberLimit;

    // calculate the index number of first bug to be shown on current pagination page, a take-away 
    // operation is carried out using the page limit and the 'bugsViewedSoFar' variable to ensure correct set of recipes is shown
    var startingRecipeNum = bugsViewedSoFar - numberLimit;

    for(var i=startingRecipeNum; i<bugsViewedSoFar; i++){
        // show relevant bugs using the 'eq()' jquery method
        $(`.bug-item:eq(${i})`).show();
    }
}

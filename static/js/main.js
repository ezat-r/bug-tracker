
$(function(){

    if(document.title == "Create New Issue"){
        // JS for the 'create-new-issue.html' page

        // Materialize CSS - Form Select tag initialisation
        $('select').formSelect();

        // Hide/show helper message for 'recipe_ingredients' textarea
        $("#description").focusin(function(){
            $("#form-helper1").toggleClass("element-hide");
        });

        $("#description").focusout(function(){
            $("#form-helper1").toggleClass("element-hide");
        });

        // select element event handler for the 'issue_type' - change prefix icon according to element selected
        $("#issueType").on("change", function(){
            var value = $("#issueType").val();

            if(value == "bug"){
                $("#issue_type_icon").removeClass("fa-plus").removeClass("green-icon");
                $("#issue_type_icon").addClass("fa-minus-square").addClass("red-icon");
            }else{
                $("#issue_type_icon").removeClass("fa-minus-square").removeClass("red-icon");
                $("#issue_type_icon").addClass("fa-plus").addClass("green-icon");
            }
        });

        // select element event handler for the 'issue_priority' - change prefix icon according to element selected
        $("#issuePriority").on("change", function(){
            var value = $("#issuePriority").val();

            $("#issue_priority_icon").removeClass();

            if(value == "triage_required"){
                $("#issue_priority_icon").addClass("fa fa-minus-circle red-icon prefix");
            }else if(value == "severe"){
                $("#issue_priority_icon").addClass("fa fa-ban red-icon prefix");
            }else if(value == "must_fix"){
                $("#issue_priority_icon").addClass("fa fa-arrow-up red-icon prefix");
            }else if(value == "desirable"){
                $("#issue_priority_icon").addClass("fa fa-angle-double-up red-icon prefix");
            }else if(value == "unlikely"){
                $("#issue_priority_icon").addClass("fa fa-angle-double-down green-icon prefix");
            }
        });
    }else if(document.title == "Bug Tracker - Sign In"){
        $("#id_username").addClass("validate");
        $("#id_password").addClass("validate");
        
    }else if(document.title == "All Issues"){
        // show priority icons instead of the actual values.
        // Icons will be displayed in the table.

        liVals = $(".priority");
        console.log(liVals)

        for(var i=0; i< liVals.length; i++){
            val = liVals[i]
            if($(val).hasClass("triage_required")){
                $(val).addClass("fa fa-minus-circle red-icon prefix");

            }else if($(val).hasClass("severe")){
                $(val).addClass("fa fa-ban red-icon prefix");

            }else if($(val).hasClass("must_fix")){
                $(val).addClass("fa fa-arrow-up red-icon prefix");

            }else if($(val).hasClass("desirable")){
                $(val).addClass("fa fa-angle-double-up red-icon prefix");

            }else if($(val).hasClass("unlikely")){

                $(val).addClass("fa fa-angle-double-down green-icon prefix");
            }
        }
    }

    statusMessageHandler();

    function statusMessageHandler(){
        // if form error or success message is shown, then hide it after 2 seconds
        if($("#error-message").html()){

            setTimeout(function(){
                $("#error-message").fadeOut();
            }, 2000);

        } else if($("#success-message").html()){

            setTimeout(function(){
                $("#success-message").fadeOut();
            }, 2000);
        }
    }
});
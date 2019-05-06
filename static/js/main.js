
$(function(){

    if(document.title == "Create New Issue" || document.title == "Edit Issue"){

        // Materialize CSS - Form Select tag initialisation
        $('select').formSelect();

        // Hide/show helper message for 'recipe_ingredients' textarea
        $("#description").focusin(function(){
            $("#form-helper1").toggleClass("element-hide");
        });

        $("#description").focusout(function(){
            $("#form-helper1").toggleClass("element-hide");
        });

        // select element event handler for the 'issue_type'
        $("#issueType").on("change", function(){

            issueTypeIconHandler("#issueType");
        });

        if(document.title == "Edit Issue"){
            // pre-select the correct 'projectName' value
            var projectVal = $("#projectName").data("value");
            $("#projectName").val(projectVal);
            $("#projectName").click().click();

            // pre-select the correct 'issueType' value
            var issueTypeVal = $("#issueType").data("value");
            $("#issueType").val(issueTypeVal);
            $("#issueType").click().click();
            issueTypeIconHandler("#issueType");

        }

    }else if(document.title == "Bug Tracker - Sign In"){
        $("#id_username").addClass("validate");
        $("#id_password").addClass("validate");
        
    }else if(document.title == "View Issue"){
        // Initialize all modals
        $('.modal').modal();

        // Materialize CSS - Form Select tag initialisation
        $('select').formSelect();

        // correct the issueType text value
        if($("#issueTypeVal").text() == "bug"){
            $("#issueTypeVal").text("Bug");
        }else{
            $("#issueTypeVal").text("Feature Request")
        }

    } else if(document.title == "Make Payment"){
        // Materialize CSS - Form Select tag initialisation
        $('select').formSelect();
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

    // change prefix icon according to element selected - bug or improvement
    function issueTypeIconHandler(id){
        var value = $(id).val();

        if(value == "bug"){
            $("#issue_type_icon").removeClass("fa-plus").removeClass("green-icon");
            $("#issue_type_icon").addClass("fa-minus-square").addClass("red-icon");
        }else{
            $("#issue_type_icon").removeClass("fa-minus-square").removeClass("red-icon");
            $("#issue_type_icon").addClass("fa-plus").addClass("green-icon");
        }
    }
});
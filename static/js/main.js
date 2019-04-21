
$(function(){

    if(document.title == "Create New Issue"){
        // JS for the 'create-new-issue.html' page

        // Materialize CSS - Form Select tag initialisation
        $('select').formSelect();

        // Hide/show helper message for 'recipe_ingredients' textarea
        $("#issue_description").focusin(function(){
            $("#form-helper1").toggleClass("element-hide");
        });

        $("#issue_description").focusout(function(){
            $("#form-helper1").toggleClass("element-hide");
        });

        // select element event handler for the 'issue_type' - change prefix icon according to element selected
        $("#issue_type").on("change", function(){
            var value = $("#issue_type").val();

            if(value == "bug"){
                $("#issue_type_icon").removeClass("fa-plus").removeClass("green-icon");
                $("#issue_type_icon").addClass("fa-minus-square").addClass("red-icon");
            }else{
                $("#issue_type_icon").removeClass("fa-minus-square").removeClass("red-icon");
                $("#issue_type_icon").addClass("fa-plus").addClass("green-icon");
            }
        });

        // select element event handler for the 'issue_priority' - change prefix icon according to element selected
        $("#issue_priority").on("change", function(){
            var value = $("#issue_priority").val();

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
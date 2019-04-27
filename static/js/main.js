
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

        // select element event handler for the 'issue_priority'
        $("#issuePriority").on("change", function(){
            // call iconCorrector function to correctly set priority icon correctly
            issuePriorityIconHandler("#issuePriority");

        });

        if(document.title == "Edit Issue"){
            var projectVal = $("#projectName").data("value");
            $("#projectName").val(projectVal);
            $("#projectName").click().click();

            var issueTypeVal = $("#issueType").data("value");
            $("#issueType").val(issueTypeVal);
            $("#issueType").click().click();
            issueTypeIconHandler("#issueType");

            var priorityVal = $("#issuePriority").data("value");
            $("#issuePriority").val(priorityVal);
            $(".select-dropdown.dropdown-trigger").click().click();
            issuePriorityIconHandler("#issuePriority");

        }

    }else if(document.title == "Bug Tracker - Sign In"){
        $("#id_username").addClass("validate");
        $("#id_password").addClass("validate");
        
    }else if(document.title == "All Issues"){
        // show priority icons instead of the actual values.
        // Icons will be displayed in the table.

        liVals = $(".priority");

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
    }else if(document.title == "View Issue"){
        // Initialize all modals
        $('.modal').modal();

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

    // change prefix icon according to selected option for the issuePriority select element
    function issuePriorityIconHandler(id){
        var value = $(id).val();

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
    }

    function selectElementCorrector(iconId, selectId, template){
        $(selectId).remove();

    }
});
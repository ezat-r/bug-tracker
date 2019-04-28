from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from .models import Issue, IssueComments
from .forms import IssueForm, IssueCommentsForm
from datetime import datetime


### Login, Logout & New User Registration Handling

# Login handling
def login(request):

    # clear any messages
    clearMessages(request)

    # check if user is already logged in
    if request.user.is_authenticated:
        # user is already logged in, so redirect to home page
        return redirect(reverse("all_issues"))

    # check if a login has been tried
    if request.method == "POST":

        # create a new form using POST data
        loginForm = UserLoginForm(request.POST)

        if loginForm.is_valid():
            # check if user exists in the user db
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password"])

            if user:
                # user is valid so login user and send a success message
                auth.login(user=user, request=request)

                return redirect(reverse("all_issues"))
            else:
                # user either doesn't exist or details incorrect so send error message
                messages.error(request, "Your username or password is incorrect!")

    else:
        # create a new empty form and send it across to the page
        loginForm = UserLoginForm()

    return render(request, "bug-tracker/login.html", {"loginForm": loginForm})


# Log out handling
@login_required
def logout(request):

    # clear any messages
    clearMessages(request)

    # log the user out
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")

    return redirect(reverse("login"))


# new user registration handling
def registration(request):
    clearMessages(request)

    if request.user.is_authenticated:
        # user is logged in already, redirect to index view
        return redirect(reverse("all_issues"))

    if request.method == "POST":
        # instantiate a form using POST data
        registerationForm = UserRegistrationForm(request.POST)

        # check if form is valid
        if registerationForm.is_valid():
            # it's valid, so save it
            registerationForm.save()

            user = auth.authenticate(username=request.POST["username"], password=request.POST["password1"])

            # check if user is created fine
            if user:
                # created fine, so display a success message
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!")

                # re-direct to 'all_issues' page
                return redirect(reverse("all_issues"))
            else:
                # error, so display a error message
                messages.error(request, "Unable to register your account!")

    else:
        # return an empty form
        registerationForm = UserRegistrationForm()

    return render(request, "bug-tracker/user-registration.html", {"registerationForm": registerationForm})


### Issue view handling

# all issues view handler
def allIssuesView(request):

    # check if user is already logged in
    if request.user.is_authenticated == False:
        # user is not logged in, so redirect to login page
        return redirect(reverse("login"))
    
    # grab all issues and sort them by the 'updatedDate' property
    issues = Issue.objects.order_by("-updatedDate")

    issueEntries = {"issues": issues}

    # pass off all issues to a render
    return render(request, "bug-tracker/all-issues.html", issueEntries)


# individual issue detailed view handler
@login_required
def issueDetailedView(request, id):
    
    # get issue from db by using the id from the request
    issue = get_object_or_404(Issue, pk=id)
    
    # grab all comments from db
    allComments = IssueComments.objects.order_by("-commentDate")

    issueComments = []

    # loop through comments and grab all comments associated with the selected issue
    for i in range(0, len(allComments)):
        if allComments[i].issueId == issue:
            issueComments.append(allComments[i])
    
    # check if user has attempted to add a new comment.
    if request.method == "POST":

        # new comment added, so create a new 'IssueCommentsForm' instance using POST data
        commentForm = IssueCommentsForm(request.POST)

        # check form is valid
        if commentForm.is_valid():

            # form is valid, perform a save, but before the save is applied, update a couple of comment properties
            comForm = commentForm.save(commit=False)

            # assign the currently logged in user as the comments author/user
            comForm.user = request.user

            # assign current issue as the 'issueId'
            comForm.issueId = issue

            # update the 'updatedTime' property for the current issue & save the current issue
            issue.updatedDate = datetime.now()
            issue.save()

            # go ahead and apply the save
            comForm.save()

            # give a success message and reload the current page
            messages.success(request, "Comment added successfully!")

            return redirect("detailed_view", id=id)
        
        else:
            # form is not valid so send an error message and reload current page
            messages.error(request, "Comment added successfully!")

            return redirect("detailed_view", id=id)

    else:
        # no attempt has been made to add a new comment, so send a blank form to view
        commentForm = IssueCommentsForm()

    issueEntry = {"issue": issue, "comments": issueComments, "commentsForm": commentForm}


    return render(request, "bug-tracker/bug-detailed-view.html", issueEntry)


### Editing an existing issue

# edit issue handler
def editIssue(request, id):

    if request.user.is_authenticated == False:
        # user is not logged in, redirect to login view
        return redirect(reverse("login"))
    
    issue = get_object_or_404(Issue, pk=id)

    if request.method == "POST":
        formDict = getFormDict(request.POST)

        updatedIssue = IssueForm(formDict, instance=issue)

        if updatedIssue.is_valid():
            issueInstance = updatedIssue.save(commit=False)
            issueInstance.updatedDate = datetime.now()
            issueInstance.save()
            
            # give a success message and reload back to detailed issue view
            messages.success(request, "Issue updated successfully!")

            return redirect("detailed_view", id=id)
        else:
            # give a error message and reload back to detailed issue view
            messages.error(request, "Error: Unable to update issue!")

            return redirect("detailed_view", id=id)

    return render(request, "bug-tracker/edit-issue.html", {"issue": issue})

# Resolving an issue
def resolveIssue(request, id):

    if request.user.is_authenticated == False:
        # user is not logged in, redirect to login view
        return redirect(reverse("login"))

    issue = get_object_or_404(Issue, pk=id)

    if request.method == "POST":
        issueComment = IssueCommentsForm({"comment": request.POST["comment"]})

        if issueComment.is_valid():
            commInstance = issueComment.save(commit=False)
            commInstance.issueId = issue
            commInstance.user = request.user
            commInstance.save()

            issue.updatedDate = datetime.now()
            issue.resolution = request.POST["resolution"]
            issue.status = "Resolved"
            issue.save()

            # give a success message and reload back to detailed issue view
            messages.success(request, "Issue resolved successfully!")

            return redirect("detailed_view", id=id)
        
        else:
            # give a error message and reload back to detailed issue view
            messages.error(request, "Error: Unable to resolve issue!")

            return redirect("detailed_view", id=id)


# Closing an issue
def closeIssue(request, id):
    if request.user.is_authenticated == False:
        # user is not logged in, redirect to login view
        return redirect(reverse("login"))

    issue = get_object_or_404(Issue, pk=id)

    if request.method == "POST":
        issueComment = IssueCommentsForm({"comment": request.POST["comment"]})

        if issueComment.is_valid():
            commInstance = issueComment.save(commit=False)
            commInstance.issueId = issue
            commInstance.user = request.user
            commInstance.save()

            issue.updatedDate = datetime.now()

            issue.status = "Closed"
            issue.save()

            # give a success message and reload back to detailed issue view
            messages.success(request, "Issue closed successfully!")

            return redirect("detailed_view", id=id)
        
        else:
            # give a error message and reload back to detailed issue view
            messages.error(request, "Error: Unable to close issue!")

            return redirect("detailed_view", id=id)


# Re-opening of an issue
def reOpenIssue(request, id):
    if request.user.is_authenticated == False:
        # user is not logged in, redirect to login view
        return redirect(reverse("login"))

    issue = get_object_or_404(Issue, pk=id)

    if request.method == "POST":
        issueComment = IssueCommentsForm({"comment": request.POST["comment"]})

        if issueComment.is_valid():
            commInstance = issueComment.save(commit=False)
            commInstance.issueId = issue
            commInstance.user = request.user
            commInstance.save()

            issue.updatedDate = datetime.now()

            issue.status = "Re-Opened"
            issue.resolution = "Unresolved"
            issue.save()

            # give a success message and reload back to detailed issue view
            messages.success(request, "Issue re-opened successfully!")

            return redirect("detailed_view", id=id)
        
        else:
            # give a error message and reload back to detailed issue view
            messages.error(request, "Error: Unable to re-open issue!")

            return redirect("detailed_view", id=id)

### New issue creation

# create Issue handling
def createTicket(request):

    if request.user.is_authenticated == False:
        # user is not logged in, redirect to login view
        return redirect(reverse("login"))

    clearMessages(request)

    # check if form has been submitted
    if request.method == "POST":
        # Form submitted, so instantiate a form using POST data

        formDict = getFormDict(request.POST)
        issueForm = IssueForm(formDict)

        # check if form is valid
        if issueForm.is_valid():
            # it's valid, so save it
            
            instance = issueForm.save(commit=False)
            instance.reporter = request.user
            instance.save()

            messages.success(request, "Created new Issue successfully!")

            return redirect(reverse("all_issues")) 
        else:
            # failed so display an error
            messages.error(request, "Unable to create Issue!")

    else:
        # otherwise, return an empty form
        issueForm = IssueForm()

    return render(request, "bug-tracker/create-new-issue.html", {"issueForm": issueForm})


## Generic

# method used to clear messages
def clearMessages(request):
    storage = messages.get_messages(request)
    storage.used = True


# method to assign dict value - which will be passed along to either update
# or create a new issue
def getFormDict(requestForm):

    formDict ={
            "projectName": requestForm["projectName"],
            "issueType": requestForm["issueType"],
            "issuePriority": requestForm["issuePriority"],
            "title": requestForm["title"],
            "affectsVersion": requestForm["affectsVersion"],
            "foundInBuild": requestForm["foundInBuild"],
            "description": requestForm["description"]
        }
    
    return formDict

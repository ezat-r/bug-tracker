from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from .models import Issue
from .forms import IssueForm


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


# Bugs view handling

@login_required
def bugsView(request):
    
    issues = Issue.objects.order_by("-updatedDate")

    issueEntries = {"issues": issues}

    return render(request, "bug-tracker/all-issues.html", issueEntries)


# create Issue handling
@login_required
def createTicket(request):

    clearMessages(request)

    # check if form has been submitted
    if request.method == "POST":
        # Form submitted, so instantiate a form using POST data

        formDict ={
            "projectName": request.POST["projectName"],
            "issueType": request.POST["issueType"],
            "issuePriority": request.POST["issuePriority"],
            "title": request.POST["title"],
            "affectsVersion": request.POST["affectsVersion"],
            "foundInBuild": request.POST["foundInBuild"],
            "description": request.POST["description"],
            "status": "Open",
            "reporter": request.user.username,
        }

        issueForm = IssueForm(formDict)

        # check if form is valid
        if issueForm.is_valid():
            # it's valid, so save it
            
            issueForm.save()

            messages.success(request, "Created new Issue successfully!")

            return redirect(reverse("all_issues")) 
        else:
            # failed so display an error
            messages.error(request, "Unable to create Issue!")

    else:
        # otherwise, return an empty form
        issueForm = IssueForm()

    return render(request, "bug-tracker/create-new-issue.html", {"issueForm": issueForm})

# method used to clear messages
def clearMessages(request):
    storage = messages.get_messages(request)
    storage.used = True


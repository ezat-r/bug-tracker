from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm

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


@login_required
def logout(request):

    # clear any messages
    clearMessages(request)

    # log the user out
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")

    return redirect(reverse("login"))


def bugsView(request):

    return render(request, "bug-tracker/all-issues.html")

def createTicket(request):

    return render(request, "bug-tracker/create-new-issue.html")

# method used to clear messages
def clearMessages(request):
    storage = messages.get_messages(request)
    storage.used = True


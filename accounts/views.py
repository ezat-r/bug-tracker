from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm

### Login, Logout & New User Registration Handling

# Login handling
def login(request):

    # check if user is already logged in
    if request.user.is_authenticated:
        # user is already logged in, so redirect to home page
        return redirect(reverse("analytics"))

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

                return redirect(reverse("analytics"))
            else:
                # user either doesn't exist or details incorrect so send error message
                messages.error(request, "Your username or password is incorrect!")

    else:
        # create a new empty form and send it across to the page
        loginForm = UserLoginForm()

    return render(request, "accounts/login.html", {"loginForm": loginForm})


# Log out handling
@login_required
def logout(request):

    # log the user out
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")

    return redirect(reverse("login"))


# new user registration handling
def registration(request):

    if request.user.is_authenticated:
        # user is logged in already, redirect to index view
        return redirect(reverse("analytics"))

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
                return redirect(reverse("analytics"))
            else:
                # error, so display a error message
                messages.error(request, "Unable to register your account!")

    else:
        # return an empty form
        registerationForm = UserRegistrationForm()

    return render(request, "accounts/user-registration.html", {"registerationForm": registerationForm})

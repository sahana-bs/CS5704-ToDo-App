from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from actions.models import Action
from .models import UserProfiles

# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
        login_user(request)

        messages.add_message(request, messages.SUCCESS, "You successfully created an account with the username: %s" % user.username)

        return redirect('library:home')
    else:
        return render(request,
                      "users/user/registration.html",
                      )


def profile(request, username):
    user = get_object_or_404(User, username=username)
    action = Action.objects.filter(user_id=user.id).order_by("-created")

    return render(request,
                  "users/user/profile.html",
                  {"user":user,
                   "actions":action}
                  )


# function to render to the login page.
def library_login(request):
    return render(request,
                  "library/library_store/login.html")


# function to perform login operations based on two user types admin and regular users
def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.userprofiles.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully.")
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return redirect("library:home")


# function to logout from the webapp.
def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('library:home')


# controller to navigate to the edit item view
def profile_edit(request, username):
    all_users = User.objects.all()
    if "username" in request.session:
        for user in all_users:
            if user.username == username:
                break
        return render(request, "users/user/profileEdit.html", {"user_list": user})

    else:
        return redirect('marketplace:marketplace_home_page')


# controller to edit detail of an item
def edit_detail(request, username):
    user1 = User.objects.get(username=request.session.get("username"))
    user = User.objects.get(username=username)

    if request.method == 'POST':
        _firstname = request.POST.get("firstname")
        _lastname = request.POST.get("lastname")
        _email = request.POST.get("email")
        _profilepicture = request.POST.get("profile-picture")
        _gender = request.POST.get("gender")
        _password = request.POST.get("password")

        role = user.userprofiles.role
        if request.session['role'] == "admin":
            _role = request.POST.get("role")
            user.userprofiles.role = _role

        user.first_name = _firstname
        user.last_name = _lastname
        user.email = _email
        if _password:
            user.set_password(_password)
        user.userprofiles.gender = _gender

        if _profilepicture != "":
            user.userprofiles.profile_pic = "img/" + _profilepicture

        user.save()
        userID = User.objects.get(username=username).id
        userProfile = UserProfiles.objects.get(user_id=userID)

        #log the change role action
        if request.session['role'] == "admin" and role != _role:
            action = Action(
                user = user1,
                verb = "Changed the user role to " + _role + " for ",
                target = userProfile
            )
            action.save()
        messages.add_message(request, messages.INFO,
                             "You have successfully edited your information")

        return redirect('users:profile', user.username)
    else:
        return redirect('users:profile', user.username)
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from recipes.models import Recipe


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if empty_field(name):
            messages.error(request, "O campo name não pode ficar em branco")
            return redirect("register")
        if empty_field(email):
            messages.error(request, "O campo email não pode ficar em branco")
            return redirect("register")
        if not same_password(password, password2):
            messages.error(request, "As senhas não são iguais")
            return redirect("register")
        if email_exists(email) or username_exists(name):
            messages.error(request, "Usuário já cadastrado")
            return redirect("register")

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso")

        return redirect("login")
    else:
        return render(request, "users/register.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if empty_field(email) or empty_field(password):
            messages.error(
                request, "Os campos de email e senha não podem ficar em branco"
            )
            return redirect("login")
        if email_exists(email):
            username = (
                User.objects.filter(email=email)
                .values_list("username", flat=True)
                .get()
            )
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login realizado com sucesso")
                return redirect("dashboard")

    return render(request, "users/login.html")


def logout(request):
    auth.logout(request)
    return redirect("index")


def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        recipes = Recipe.objects.order_by("-created_at").filter(user=user_id)
        data = {
            "recipes": recipes,
        }
        return render(request, "users/dashboard.html", data)
    else:
        return redirect("index")


def empty_field(field):
    return not field.strip()


def same_password(password1, password2):
    return password1 == password2


def email_exists(email):
    return User.objects.filter(email=email).exists()


def username_exists(username):
    return User.objects.filter(username=username).exists()

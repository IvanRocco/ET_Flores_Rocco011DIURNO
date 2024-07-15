from django.shortcuts import render, redirect
from .models import Beat
from .forms import BeatForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q


# Create your views here.
def home(request):
	beats= Beat.objects.all()

	return render(request, 'home.html',context={'datos':beats})


def form_beat(request):
    if request.method == "POST":
        beat_form = BeatForm(request.POST)
        if beat_form.is_valid():
            beat_form.save()
            return redirect("tracklist")
    else:
        beat_form = BeatForm()
    return render(request, "core/form_beat.html", {"beat_form": beat_form})


def eliminar(request, id):
    beatEliminado = Beat.objects.get(idBeat=id)
    beatEliminado.delete()
    return redirect("tracklist")


def modificar(request, id):
    beatModificado = Beat.objects.get(idBeat=id)
    datos = {"form": BeatForm(instance=beatModificado)}
    if request.method == "POST":
        formulario = BeatForm(data=request.POST, instance=beatModificado)
        if formulario.is_valid:
            formulario.save()
        return redirect("tracklist")
    return render(request, "modificar.html", datos)


def ventana_inicio(request):
    # Aquí puedes agregar lógica adicional si es necesaria
    return render(request, "ventana_inicio.html")


def ventana_info(request):
    return render(request, "ventana_info.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("tracklist")
            except:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "Usuario ya existe"},
                )
        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "Contraseñas no coinciden "},
        )


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user= authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],)
        if user is None:
                return render(request, "signin.html", {"form": AuthenticationForm,'error': 'Usuario o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('tracklist')
        
def listado_beats(request):
    beats = Beat.objects.all()

    # Obtener el parámetro de búsqueda desde la URL
    query = request.GET.get('buscar')
    if query:
        beats = beats.filter(nombreBeat__icontains=query)

    context = {
        'datos': beats,
        'user': request.user
    }
    return render(request, 'home.html', context)


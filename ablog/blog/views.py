from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Form
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.

def show_form(request):
    obsah = [
        {"image": "static/images/python-florian-klauer.jpg", "description": "Python", "title": "Python",
                 "text": "Language that Harry Potter didn´t have to learn"},
        # linux: {image: "static/images/linux-dylan-shaw.jpg", description: "Linux", title: "Linux",
        #         text: "Interesting linux topics"},
        # security: {image: "static/images/security-markus-winkler.jpg", description: "Security", title: "Security",
        #            text: "See and not to be seen"}
    ]
    text = "Dnes je krásný den"
    return render(request, "templates/obsah-stranky.html", {"obsah" : obsah, "text" : text})
#form = []
def submit_form(request):
    form_title = request.POST["Title"]
    form_text = request.POST["Text"]
    Vytvoreni_instance= Form(title = form_title, text = form_text)
    Vytvoreni_instance.save()
    #form.append({"title": form_title, "text": form_text})
    return redirect("/show_content/")

def show_content(request):
    #Načtení instance z db - list objektu, načtou se všechny řádky z tab
    Nacteni_instance = Form.objects.all()
    return render(request, "templates/vypis_formulare.html",
                  #{"form": form}
                  #form stejné jméno jak v vypis_formulare.html, odkazuju se na klíč
                  {"form" : Nacteni_instance }
                  )


def show_about(request):
    http_response = HttpResponse()
    odstavec = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dol"]
    return render(request, "templates/about.html", context={"odstavec": odstavec, "user": "Sarka"})


# class based view
# class HomeView(ListView):
# model = Post()
# template_name = 'obsah-stranky.html'

# class AddPostView(CreateView):
# model = AddPostView
# template_name = 'add_post.html'
# fields = '__all__'


def show_add_post(request, *args, **kwargs):
    http_response = HttpResponse()
    return render(request, "templates./add_post.html", {})
